package com.coldstorage.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import java.math.BigDecimal;
import java.time.LocalDate;

@Entity
@Table(name = "bookings")
public class Booking {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String bookingReference;

    @NotBlank(message = "Farmer / Trader name is required")
    private String farmerName;

    @NotBlank(message = "Contact phone number is required")
    private String contactNumber;

    @NotBlank(message = "Commodity type is required")
    private String commodityType; // Fruits, Vegetables, Dairy, Meat/Seafood

    @Min(value = 1, message = "Quantity must be at least 1 crate")
    @Max(value = 500, message = "Quantity cannot exceed 500 crates per booking")
    private int cratesCount;

    @NotNull(message = "Check-in date is required")
    private LocalDate checkInDate;

    @NotNull(message = "Check-out date is required")
    private LocalDate checkOutDate;

    private BigDecimal totalCost;

    @Column(nullable = false)
    private String status = "PENDING"; // PENDING, CONFIRMED, CHECKED_IN, COMPLETED, CANCELLED

    @NotBlank(message = "Chamber selection is required")
    private String chamberCode;

    private String slotNumber;

    public Booking() {}

    public Booking(String bookingReference, String farmerName, String contactNumber, String commodityType,
                   int cratesCount, LocalDate checkInDate, LocalDate checkOutDate, BigDecimal totalCost,
                   String status, String chamberCode, String slotNumber) {
        this.bookingReference = bookingReference;
        this.farmerName = farmerName;
        this.contactNumber = contactNumber;
        this.commodityType = commodityType;
        this.cratesCount = cratesCount;
        this.checkInDate = checkInDate;
        this.checkOutDate = checkOutDate;
        this.totalCost = totalCost;
        this.status = status;
        this.chamberCode = chamberCode;
        this.slotNumber = slotNumber;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getBookingReference() { return bookingReference; }
    public void setBookingReference(String bookingReference) { this.bookingReference = bookingReference; }

    public String getFarmerName() { return farmerName; }
    public void setFarmerName(String farmerName) { this.farmerName = farmerName; }

    public String getContactNumber() { return contactNumber; }
    public void setContactNumber(String contactNumber) { this.contactNumber = contactNumber; }

    public String getCommodityType() { return commodityType; }
    public void setCommodityType(String commodityType) { this.commodityType = commodityType; }

    public int getCratesCount() { return cratesCount; }
    public void setCratesCount(int cratesCount) { this.cratesCount = cratesCount; }

    public LocalDate getCheckInDate() { return checkInDate; }
    public void setCheckInDate(LocalDate checkInDate) { this.checkInDate = checkInDate; }

    public LocalDate getCheckOutDate() { return checkOutDate; }
    public void setCheckOutDate(LocalDate checkOutDate) { this.checkOutDate = checkOutDate; }

    public BigDecimal getTotalCost() { return totalCost; }
    public void setTotalCost(BigDecimal totalCost) { this.totalCost = totalCost; }

    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }

    public String getChamberCode() { return chamberCode; }
    public void setChamberCode(String chamberCode) { this.chamberCode = chamberCode; }

    public String getSlotNumber() { return slotNumber; }
    public void setSlotNumber(String slotNumber) { this.slotNumber = slotNumber; }
}
