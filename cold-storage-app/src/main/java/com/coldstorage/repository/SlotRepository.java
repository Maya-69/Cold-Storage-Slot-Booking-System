package com.coldstorage.repository;

import com.coldstorage.model.Slot;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface SlotRepository extends JpaRepository<Slot, Long> {
    List<Slot> findByChamberCode(String chamberCode);
    Optional<Slot> findBySlotNumber(String slotNumber);
    List<Slot> findByAvailableTrue();
}
