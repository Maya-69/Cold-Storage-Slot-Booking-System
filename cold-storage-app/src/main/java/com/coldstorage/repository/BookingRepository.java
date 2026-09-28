package com.coldstorage.repository;

import com.coldstorage.model.Booking;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@Repository
public interface BookingRepository extends JpaRepository<Booking, Long> {
    Optional<Booking> findByBookingReference(String bookingReference);
    List<Booking> findByStatus(String status);
    List<Booking> findByFarmerNameContainingIgnoreCase(String farmerName);

    @Query("SELECT b FROM Booking b WHERE b.slotNumber = :slotNumber " +
           "AND b.status NOT IN ('CANCELLED', 'COMPLETED') " +
           "AND (:newCheckIn <= b.checkOutDate AND :newCheckOut >= b.checkInDate)")
    List<Booking> findOverlappingBookings(@Param("slotNumber") String slotNumber,
                                         @Param("newCheckIn") LocalDate newCheckIn,
                                         @Param("newCheckOut") LocalDate newCheckOut);
}
