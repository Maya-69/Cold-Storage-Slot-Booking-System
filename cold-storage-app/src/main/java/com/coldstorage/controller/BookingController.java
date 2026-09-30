package com.coldstorage.controller;

import com.coldstorage.model.Booking;
import com.coldstorage.service.BookingService;
import com.coldstorage.service.ChamberService;
import jakarta.validation.Valid;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("/bookings")
public class BookingController {

    private final BookingService bookingService;
    private final ChamberService chamberService;

    public BookingController(BookingService bookingService, ChamberService chamberService) {
        this.bookingService = bookingService;
        this.chamberService = chamberService;
    }

    @GetMapping
    public String listBookings(@RequestParam(required = false) String status, Model model) {
        if (status != null && !status.isBlank() && !"ALL".equalsIgnoreCase(status)) {
            model.addAttribute("bookings", bookingService.getBookingsByStatus(status.toUpperCase()));
            model.addAttribute("selectedStatus", status.toUpperCase());
        } else {
            model.addAttribute("bookings", bookingService.getAllBookings());
            model.addAttribute("selectedStatus", "ALL");
        }
        return "bookings";
    }

    @GetMapping("/new")
    public String showBookingForm(Model model) {
        if (!model.containsAttribute("booking")) {
            model.addAttribute("booking", new Booking());
        }
        model.addAttribute("chambers", chamberService.getAllChambers());
        return "booking-form";
    }

    @PostMapping("/new")
    public String processBooking(@Valid @ModelAttribute("booking") Booking booking,
                                 BindingResult result,
                                 Model model,
                                 RedirectAttributes redirectAttributes) {
        if (result.hasErrors()) {
            model.addAttribute("chambers", chamberService.getAllChambers());
            return "booking-form";
        }

        try {
            Booking saved = bookingService.createBooking(booking);
            redirectAttributes.addFlashAttribute("successMessage",
                    "Slot reserved successfully! Booking Reference: " + saved.getBookingReference() + 
                    " | Total Cost: Rs. " + saved.getTotalCost());
            return "redirect:/bookings";
        } catch (IllegalArgumentException | IllegalStateException ex) {
            model.addAttribute("errorMessage", ex.getMessage());
            model.addAttribute("chambers", chamberService.getAllChambers());
            return "booking-form";
        }
    }

    @PostMapping("/{id}/confirm")
    public String confirmBooking(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        try {
            bookingService.updateStatus(id, "CONFIRMED");
            redirectAttributes.addFlashAttribute("successMessage", "Booking #" + id + " has been successfully CONFIRMED.");
        } catch (Exception ex) {
            redirectAttributes.addFlashAttribute("errorMessage", ex.getMessage());
        }
        return "redirect:/bookings";
    }

    @PostMapping("/{id}/checkin")
    public String checkinBooking(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        try {
            bookingService.updateStatus(id, "CHECKED_IN");
            redirectAttributes.addFlashAttribute("successMessage", "Booking #" + id + " produce has arrived and CHECKED-IN.");
        } catch (Exception ex) {
            redirectAttributes.addFlashAttribute("errorMessage", ex.getMessage());
        }
        return "redirect:/bookings";
    }

    @PostMapping("/{id}/cancel")
    public String cancelBooking(@PathVariable Long id, RedirectAttributes redirectAttributes) {
        try {
            bookingService.updateStatus(id, "CANCELLED");
            redirectAttributes.addFlashAttribute("successMessage", "Booking #" + id + " has been CANCELLED and slot freed.");
        } catch (Exception ex) {
            redirectAttributes.addFlashAttribute("errorMessage", ex.getMessage());
        }
        return "redirect:/bookings";
    }
}
