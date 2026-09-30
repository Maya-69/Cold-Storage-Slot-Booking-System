package com.coldstorage.controller;

import com.coldstorage.model.Booking;
import com.coldstorage.model.Chamber;
import com.coldstorage.service.BookingService;
import com.coldstorage.service.ChamberService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api")
public class ApiController {

    private final ChamberService chamberService;
    private final BookingService bookingService;

    public ApiController(ChamberService chamberService, BookingService bookingService) {
        this.chamberService = chamberService;
        this.bookingService = bookingService;
    }

    @GetMapping("/metrics")
    public ResponseEntity<Map<String, Object>> getMetrics() {
        int total = chamberService.getTotalCapacity();
        int available = chamberService.getAvailableCapacity();
        int booked = total - available;
        long active = bookingService.getActiveReservationsCount();

        Map<String, Object> metrics = new HashMap<>();
        metrics.put("totalCapacitySlots", total);
        metrics.put("availableCapacitySlots", available);
        metrics.put("bookedCapacitySlots", booked);
        metrics.put("activeReservations", active);
        metrics.put("status", "UP");

        return ResponseEntity.ok(metrics);
    }

    @GetMapping("/chambers")
    public ResponseEntity<List<Chamber>> getChambers() {
        return ResponseEntity.ok(chamberService.getAllChambers());
    }

    @GetMapping("/bookings")
    public ResponseEntity<List<Booking>> getBookings() {
        return ResponseEntity.ok(bookingService.getAllBookings());
    }
}
