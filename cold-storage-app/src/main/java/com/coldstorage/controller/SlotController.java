package com.coldstorage.controller;

import com.coldstorage.service.ChamberService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class SlotController {

    private final ChamberService chamberService;

    public SlotController(ChamberService chamberService) {
        this.chamberService = chamberService;
    }

    @GetMapping("/slots")
    public String viewSlots(@RequestParam(required = false) String zone,
                            @RequestParam(required = false) String commodity,
                            Model model) {
        if (commodity != null && !commodity.isBlank()) {
            model.addAttribute("chambers", chamberService.getChambersByCommodity(commodity));
            model.addAttribute("selectedCommodity", commodity);
            model.addAttribute("selectedZone", "ALL");
        } else if (zone != null && !zone.isBlank() && !"ALL".equalsIgnoreCase(zone)) {
            model.addAttribute("chambers", chamberService.getChambersByZone(zone.toUpperCase()));
            model.addAttribute("selectedZone", zone.toUpperCase());
            model.addAttribute("selectedCommodity", "");
        } else {
            model.addAttribute("chambers", chamberService.getAllChambers());
            model.addAttribute("selectedZone", "ALL");
            model.addAttribute("selectedCommodity", "");
        }
        model.addAttribute("slots", chamberService.getAllSlots());
        return "slots";
    }
}
