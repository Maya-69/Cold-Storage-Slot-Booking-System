package com.coldstorage.controller;

import com.coldstorage.service.BookingService;
import com.coldstorage.service.ChamberService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class DashboardController {

    private final ChamberService chamberService;
    private final BookingService bookingService;

    public DashboardController(ChamberService chamberService, BookingService bookingService) {
        this.chamberService = chamberService;
        this.bookingService = bookingService;
    }

    @GetMapping("/")
    public String index(Model model) {
        int totalCapacity = chamberService.getTotalCapacity();
        int availableCapacity = chamberService.getAvailableCapacity();
        int bookedSlots = totalCapacity - availableCapacity;
        long activeReservations = bookingService.getActiveReservationsCount();

        model.addAttribute("totalCapacity", totalCapacity);
        model.addAttribute("availableCapacity", availableCapacity);
        model.addAttribute("bookedSlots", bookedSlots);
        model.addAttribute("activeReservations", activeReservations);
        model.addAttribute("chambers", chamberService.getAllChambers());
        model.addAttribute("recentBookings", bookingService.getAllBookings());

        return "dashboard";
    }
}
