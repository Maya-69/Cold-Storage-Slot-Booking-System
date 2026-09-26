package com.coldstorage.model;

import jakarta.persistence.*;

@Entity
@Table(name = "slots")
public class Slot {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String slotNumber;

    @Column(nullable = false)
    private String chamberCode;

    private boolean available = true;

    private int maxCratesCapacity = 100;

    public Slot() {}

    public Slot(String slotNumber, String chamberCode, boolean available, int maxCratesCapacity) {
        this.slotNumber = slotNumber;
        this.chamberCode = chamberCode;
        this.available = available;
        this.maxCratesCapacity = maxCratesCapacity;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getSlotNumber() { return slotNumber; }
    public void setSlotNumber(String slotNumber) { this.slotNumber = slotNumber; }

    public String getChamberCode() { return chamberCode; }
    public void setChamberCode(String chamberCode) { this.chamberCode = chamberCode; }

    public boolean isAvailable() { return available; }
    public void setAvailable(boolean available) { this.available = available; }

    public int getMaxCratesCapacity() { return maxCratesCapacity; }
    public void setMaxCratesCapacity(int maxCratesCapacity) { this.maxCratesCapacity = maxCratesCapacity; }
}
