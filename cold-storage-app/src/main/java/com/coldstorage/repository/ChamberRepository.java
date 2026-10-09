package com.coldstorage.repository;

import com.coldstorage.model.Chamber;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface ChamberRepository extends JpaRepository<Chamber, Long> {
    Optional<Chamber> findByChamberCode(String chamberCode);
    List<Chamber> findByZoneType(String zoneType);
}
