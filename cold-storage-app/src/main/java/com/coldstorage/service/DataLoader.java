package com.coldstorage.service;

import com.coldstorage.model.Booking;
import com.coldstorage.model.Chamber;
import com.coldstorage.model.Slot;
import com.coldstorage.model.User;
import com.coldstorage.repository.BookingRepository;
import com.coldstorage.repository.ChamberRepository;
import com.coldstorage.repository.SlotRepository;
import com.coldstorage.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import java.math.BigDecimal;
import java.time.LocalDate;

@Component
public class DataLoader implements CommandLineRunner {

    private final ChamberRepository chamberRepository;
    private final SlotRepository slotRepository;
    private final BookingRepository bookingRepository;
    private final UserRepository userRepository;

    public DataLoader(ChamberRepository chamberRepository, SlotRepository slotRepository,
                      BookingRepository bookingRepository, UserRepository userRepository) {
        this.chamberRepository = chamberRepository;
        this.slotRepository = slotRepository;
        this.bookingRepository = bookingRepository;
        this.userRepository = userRepository;
    }

    @Override
    public void run(String... args) {
        if (chamberRepository.count() == 0) {
            // Seed Chambers
            Chamber c1 = new Chamber("CH-DF1", "Deep Freeze Chamber A", "DEEP_FREEZE", -25.0, -18.0,
                    "Seafood, Frozen Meat, Poultry, Butter", 20, 16, new BigDecimal("45.00"));
            Chamber c2 = new Chamber("CH-CH1", "Chilled Fruit & Dairy Hall", "CHILLED", 0.0, 4.0,
                    "Apples, Pears, Fresh Milk, Cheese, Berries", 30, 24, new BigDecimal("30.00"));
            Chamber c3 = new Chamber("CH-CH2", "Chilled Vegetable Storage", "CHILLED", 1.0, 5.0,
                    "Broccoli, Cauliflower, Capsicum, Carrots", 25, 20, new BigDecimal("28.00"));
            Chamber c4 = new Chamber("CH-CA1", "Controlled Atmosphere Hall", "CONTROLLED_ATMOSPHERE", 10.0, 15.0,
                    "Potatoes, Onions, Garlic, Ginger", 40, 35, new BigDecimal("18.00"));

            chamberRepository.save(c1);
            chamberRepository.save(c2);
            chamberRepository.save(c3);
            chamberRepository.save(c4);

            // Seed Slots for Chamber 1
            for (int i = 1; i <= 5; i++) {
                slotRepository.save(new Slot("DF1-S" + String.format("%02d", i), "CH-DF1", true, 100));
            }
            // Seed Slots for Chamber 2
            for (int i = 1; i <= 5; i++) {
                slotRepository.save(new Slot("CH1-S" + String.format("%02d", i), "CH-CH1", true, 120));
            }
            // Seed Slots for Chamber 4
            for (int i = 1; i <= 5; i++) {
                slotRepository.save(new Slot("CA1-S" + String.format("%02d", i), "CH-CA1", true, 200));
            }

            // Seed Default Users
            userRepository.save(new User("mayuresh", "devops123", "Mayuresh Sawant", "mayuresh.sawant@devops.edu", "9876543210", "MANAGER"));
            userRepository.save(new User("farmer_ramesh", "farmer123", "Ramesh Patil", "ramesh.patil@farm.org", "9822012345", "FARMER"));
            userRepository.save(new User("trader_vikram", "trader123", "Vikram Shah", "vikram.shah@agrotrade.in", "9811098765", "TRADER"));

            // Seed Initial Bookings
            Booking b1 = new Booking("CSBS-INIT001", "Ramesh Patil", "9822012345", "Apples", 40,
                    LocalDate.now().plusDays(1), LocalDate.now().plusDays(15), new BigDecimal("16800.00"),
                    "CONFIRMED", "CH-CH1", "CH1-S01");
            Booking b2 = new Booking("CSBS-INIT002", "Vikram Shah", "9811098765", "Frozen Prawns", 25,
                    LocalDate.now().plusDays(2), LocalDate.now().plusDays(30), new BigDecimal("31500.00"),
                    "CHECKED_IN", "CH-DF1", "DF1-S01");
            Booking b3 = new Booking("CSBS-INIT003", "Anand Shinde", "9844055667", "Potatoes", 100,
                    LocalDate.now().plusDays(5), LocalDate.now().plusDays(45), new BigDecimal("72000.00"),
                    "PENDING", "CH-CA1", "CA1-S01");

            bookingRepository.save(b1);
            bookingRepository.save(b2);
            bookingRepository.save(b3);
        }
    }
}
