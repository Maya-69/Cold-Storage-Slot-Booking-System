package com.coldstorage.service;

import com.coldstorage.model.Chamber;
import com.coldstorage.model.Slot;
import com.coldstorage.repository.ChamberRepository;
import com.coldstorage.repository.SlotRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class ChamberService {

    private final ChamberRepository chamberRepository;
    private final SlotRepository slotRepository;

    public ChamberService(ChamberRepository chamberRepository, SlotRepository slotRepository) {
        this.chamberRepository = chamberRepository;
        this.slotRepository = slotRepository;
    }

    public List<Chamber> getAllChambers() {
        return chamberRepository.findAll();
    }

    public Optional<Chamber> getChamberByCode(String code) {
        return chamberRepository.findByChamberCode(code);
    }

    public List<Chamber> getChambersByZone(String zoneType) {
        return chamberRepository.findByZoneType(zoneType);
    }

    public List<Chamber> getChambersByCommodity(String commodity) {
        if (commodity == null || commodity.isBlank()) {
            return chamberRepository.findAll();
        }
        return chamberRepository.findAll().stream()
                .filter(c -> c.getSuitableCommodities() != null &&
                             c.getSuitableCommodities().toLowerCase().contains(commodity.toLowerCase()))
                .toList();
    }

    public List<Slot> getSlotsByChamber(String chamberCode) {
        return slotRepository.findByChamberCode(chamberCode);
    }

    public List<Slot> getAllSlots() {
        return slotRepository.findAll();
    }

    public List<Slot> getAvailableSlots() {
        return slotRepository.findByAvailableTrue();
    }

    public int getTotalCapacity() {
        return chamberRepository.findAll().stream().mapToInt(Chamber::getTotalSlots).sum();
    }

    public int getAvailableCapacity() {
        return chamberRepository.findAll().stream().mapToInt(Chamber::getAvailableSlots).sum();
    }
}
