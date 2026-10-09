package com.coldstorage.service;

import com.coldstorage.model.Booking;
import com.coldstorage.model.Chamber;
import com.coldstorage.repository.BookingRepository;
import com.coldstorage.repository.ChamberRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.math.BigDecimal;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class BookingService {

    private final BookingRepository bookingRepository;
    private final ChamberRepository chamberRepository;

    public BookingService(BookingRepository bookingRepository, ChamberRepository chamberRepository) {
        this.bookingRepository = bookingRepository;
        this.chamberRepository = chamberRepository;
    }

    public List<Booking> getAllBookings() {
        return bookingRepository.findAll();
    }

    public List<Booking> getBookingsByStatus(String status) {
        return bookingRepository.findByStatus(status);
    }

    public Optional<Booking> getBookingById(Long id) {
        return bookingRepository.findById(id);
    }

    public Optional<Booking> getBookingByReference(String reference) {
        return bookingRepository.findByBookingReference(reference);
    }

    @Transactional
    public Booking createBooking(Booking booking) {
        // Validation: Dates
        if (booking.getCheckInDate() == null || booking.getCheckOutDate() == null) {
            throw new IllegalArgumentException("Check-in and Check-out dates are strictly required.");
        }
        if (!booking.getCheckOutDate().isAfter(booking.getCheckInDate())) {
            throw new IllegalArgumentException("Check-out date must be strictly after check-in date.");
        }

        // Validation: Chamber existence
        Chamber chamber = chamberRepository.findByChamberCode(booking.getChamberCode())
                .orElseThrow(() -> new IllegalArgumentException("Selected chamber does not exist: " + booking.getChamberCode()));

        if (chamber.getAvailableSlots() <= 0) {
            throw new IllegalStateException("Selected chamber has no available slots left.");
        }

        // Validation: Slot Number allocation & Overlap checking
        String slotNum = booking.getSlotNumber();
        if (slotNum == null || slotNum.isBlank()) {
            // Auto-assign slot
            slotNum = booking.getChamberCode() + "-SLOT-" + (100 + bookingRepository.findAll().size() + 1);
            booking.setSlotNumber(slotNum);
        }

        List<Booking> overlaps = bookingRepository.findOverlappingBookings(
                slotNum, booking.getCheckInDate(), booking.getCheckOutDate());
        if (!overlaps.isEmpty()) {
            throw new IllegalStateException("Slot " + slotNum + " is already reserved for overlapping dates.");
        }

        // Resolved Conflict: Standardize reference with CSBS-2026-RES- combining year and reservation tag
        String ref = "CSBS-2026-RES-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
        booking.setBookingReference(ref);

        // Calculate Cost: days * crates * pricePerCrate
        long days = ChronoUnit.DAYS.between(booking.getCheckInDate(), booking.getCheckOutDate());
        if (days <= 0) days = 1;
        BigDecimal dailyRate = chamber.getPricePerDayPerCrate();
        BigDecimal total = dailyRate.multiply(BigDecimal.valueOf(booking.getCratesCount()))
                                    .multiply(BigDecimal.valueOf(days));
        booking.setTotalCost(total);
        booking.setStatus("PENDING");

        // Decrement chamber available slots
        chamber.setAvailableSlots(chamber.getAvailableSlots() - 1);
        chamberRepository.save(chamber);

        return bookingRepository.save(booking);
    }

    @Transactional
    public Booking updateStatus(Long bookingId, String newStatus) {
        Booking booking = bookingRepository.findById(bookingId)
                .orElseThrow(() -> new IllegalArgumentException("Booking not found: " + bookingId));

        String currentStatus = booking.getStatus();

        // Validate lifecycle transition
        if ("CANCELLED".equals(newStatus)) {
            if ("COMPLETED".equals(currentStatus)) {
                throw new IllegalStateException("Cannot cancel an already completed booking.");
            }
            booking.setStatus("CANCELLED");
            // Free slot
            chamberRepository.findByChamberCode(booking.getChamberCode()).ifPresent(c -> {
                c.setAvailableSlots(c.getAvailableSlots() + 1);
                chamberRepository.save(c);
            });
        } else if ("CONFIRMED".equals(newStatus)) {
            if (!"PENDING".equals(currentStatus)) {
                throw new IllegalStateException("Only PENDING bookings can be CONFIRMED.");
            }
            booking.setStatus("CONFIRMED");
        } else if ("CHECKED_IN".equals(newStatus)) {
            if (!"CONFIRMED".equals(currentStatus)) {
                throw new IllegalStateException("Only CONFIRMED bookings can be CHECKED_IN.");
            }
            booking.setStatus("CHECKED_IN");
        } else if ("COMPLETED".equals(newStatus)) {
            if (!"CHECKED_IN".equals(currentStatus)) {
                throw new IllegalStateException("Only CHECKED_IN bookings can be COMPLETED.");
            }
            booking.setStatus("COMPLETED");
            // Free slot
            chamberRepository.findByChamberCode(booking.getChamberCode()).ifPresent(c -> {
                c.setAvailableSlots(c.getAvailableSlots() + 1);
                chamberRepository.save(c);
            });
        } else {
            booking.setStatus(newStatus);
        }

        return bookingRepository.save(booking);
    }

    public long getActiveReservationsCount() {
        return bookingRepository.findAll().stream()
                .filter(b -> !"CANCELLED".equals(b.getStatus()) && !"COMPLETED".equals(b.getStatus()))
                .count();
    }
}
