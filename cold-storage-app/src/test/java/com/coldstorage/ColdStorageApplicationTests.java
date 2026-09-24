package com.coldstorage;

import com.coldstorage.model.Booking;
import com.coldstorage.model.Chamber;
import com.coldstorage.service.BookingService;
import com.coldstorage.service.ChamberService;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class ColdStorageApplicationTests {

    @Autowired
    private ChamberService chamberService;

    @Autowired
    private BookingService bookingService;

    @Test
    @DisplayName("Context loads successfully")
    void contextLoads() {
        assertNotNull(chamberService);
        assertNotNull(bookingService);
    }

    @Test
    @DisplayName("Chambers are pre-seeded with temperature zones")
    void testChambersSeeded() {
        List<Chamber> chambers = chamberService.getAllChambers();
        assertFalse(chambers.isEmpty(), "Chambers should be seeded on startup");
        assertTrue(chambers.stream().anyMatch(c -> "DEEP_FREEZE".equals(c.getZoneType())));
        assertTrue(chambers.stream().anyMatch(c -> "CHILLED".equals(c.getZoneType())));
        assertTrue(chambers.stream().anyMatch(c -> "CONTROLLED_ATMOSPHERE".equals(c.getZoneType())));
    }

    @Test
    @DisplayName("Booking creation successfully enforces cost and pending status")
    void testBookingCreation() {
        Booking booking = new Booking();
        booking.setFarmerName("Test Farmer");
        booking.setContactNumber("9988776655");
        booking.setCommodityType("Apples");
        booking.setCratesCount(20);
        booking.setChamberCode("CH-CH1");
        booking.setCheckInDate(LocalDate.now().plusDays(10));
        booking.setCheckOutDate(LocalDate.now().plusDays(20));

        Booking created = bookingService.createBooking(booking);

        assertNotNull(created.getId());
        assertNotNull(created.getBookingReference());
        assertEquals("PENDING", created.getStatus());
        assertTrue(created.getTotalCost().compareTo(BigDecimal.ZERO) > 0);
    }

    @Test
    @DisplayName("Booking status transitions adhere to lifecycle rules")
    void testBookingStatusLifecycle() {
        Booking booking = new Booking();
        booking.setFarmerName("Lifecycle Farmer");
        booking.setContactNumber("9988112233");
        booking.setCommodityType("Dairy");
        booking.setCratesCount(15);
        booking.setChamberCode("CH-CH1");
        booking.setCheckInDate(LocalDate.now().plusDays(25));
        booking.setCheckOutDate(LocalDate.now().plusDays(35));

        Booking created = bookingService.createBooking(booking);
        assertEquals("PENDING", created.getStatus());

        Booking confirmed = bookingService.updateStatus(created.getId(), "CONFIRMED");
        assertEquals("CONFIRMED", confirmed.getStatus());

        Booking checkedIn = bookingService.updateStatus(created.getId(), "CHECKED_IN");
        assertEquals("CHECKED_IN", checkedIn.getStatus());

        Booking completed = bookingService.updateStatus(created.getId(), "COMPLETED");
        assertEquals("COMPLETED", completed.getStatus());
    }
}
