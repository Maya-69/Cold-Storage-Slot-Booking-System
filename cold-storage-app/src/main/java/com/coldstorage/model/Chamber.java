package com.coldstorage.model;

import jakarta.persistence.*;
import java.math.BigDecimal;

@Entity
@Table(name = "chambers")
public class Chamber {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String chamberCode;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String zoneType; // DEEP_FREEZE, CHILLED, CONTROLLED_ATMOSPHERE

    private double minTemperature;
    private double maxTemperature;

    private String suitableCommodities;

    private int totalSlots;
    private int availableSlots;

    private BigDecimal pricePerDayPerCrate;

    public Chamber() {}

    public Chamber(String chamberCode, String name, String zoneType, double minTemperature, double maxTemperature,
                   String suitableCommodities, int totalSlots, int availableSlots, BigDecimal pricePerDayPerCrate) {
        this.chamberCode = chamberCode;
        this.name = name;
        this.zoneType = zoneType;
        this.minTemperature = minTemperature;
        this.maxTemperature = maxTemperature;
        this.suitableCommodities = suitableCommodities;
        this.totalSlots = totalSlots;
        this.availableSlots = availableSlots;
        this.pricePerDayPerCrate = pricePerDayPerCrate;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getChamberCode() { return chamberCode; }
    public void setChamberCode(String chamberCode) { this.chamberCode = chamberCode; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getZoneType() { return zoneType; }
    public void setZoneType(String zoneType) { this.zoneType = zoneType; }

    public double getMinTemperature() { return minTemperature; }
    public void setMinTemperature(double minTemperature) { this.minTemperature = minTemperature; }

    public double getMaxTemperature() { return maxTemperature; }
    public void setMaxTemperature(double maxTemperature) { this.maxTemperature = maxTemperature; }

    public String getSuitableCommodities() { return suitableCommodities; }
    public void setSuitableCommodities(String suitableCommodities) { this.suitableCommodities = suitableCommodities; }

    public int getTotalSlots() { return totalSlots; }
    public void setTotalSlots(int totalSlots) { this.totalSlots = totalSlots; }

    public int getAvailableSlots() { return availableSlots; }
    public void setAvailableSlots(int availableSlots) { this.availableSlots = availableSlots; }

    public BigDecimal getPricePerDayPerCrate() { return pricePerDayPerCrate; }
    public void setPricePerDayPerCrate(BigDecimal pricePerDayPerCrate) { this.pricePerDayPerCrate = pricePerDayPerCrate; }
}
