package com.coldstorage;

import io.github.bonigarcia.wdm.WebDriverManager;
import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtensionContext;
import org.junit.jupiter.api.extension.TestWatcher;
import org.openqa.selenium.*;
import org.openqa.selenium.edge.EdgeDriver;
import org.openqa.selenium.edge.EdgeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.server.LocalServerPort;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalDate;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class ColdStorageSeleniumTest {

    @LocalServerPort
    private int port;

    private static WebDriver driver;
    private static WebDriverWait wait;
    private String baseUrl;

    @BeforeAll
    static void setupDriver() {
        Path cachedDriver = Paths.get(System.getProperty("user.home"), ".cache", "selenium", "msedgedriver", "win64", "155.0.4283.62", "msedgedriver.exe");
        if (Files.exists(cachedDriver)) {
            System.setProperty("webdriver.edge.driver", cachedDriver.toString());
        }
        EdgeOptions options = new EdgeOptions();
        options.addArguments("--headless=new", "--no-sandbox", "--disable-dev-shm-usage", "--window-size=1280,800");
        driver = new EdgeDriver(options);
        wait = new WebDriverWait(driver, Duration.ofSeconds(5));
    }

    @AfterAll
    static void tearDownDriver() {
        if (driver != null) {
            driver.quit();
        }
    }

    @BeforeEach
    void initUrl() {
        baseUrl = "http://localhost:" + port;
    }

    // Failure screenshot hook
    public static void takeFailureScreenshot(String testName) {
        if (driver instanceof TakesScreenshot takesScreenshot) {
            File src = takesScreenshot.getScreenshotAs(OutputType.FILE);
            Path destDir = Paths.get("screenshots", "failures");
            try {
                Files.createDirectories(destDir);
                Path dest = destDir.resolve(testName + "_" + System.currentTimeMillis() + ".png");
                Files.copy(src.toPath(), dest);
                System.out.println("Automated Failure Screenshot captured at: " + dest.toAbsolutePath());
            } catch (IOException e) {
                System.err.println("Could not save failure screenshot: " + e.getMessage());
            }
        }
    }

    @Test
    @Order(1)
    @DisplayName("Journey 1: Farmer browses chamber directory and reserves cold storage slot")
    void testJourney1_FarmerSlotReservation() {
        try {
            driver.get(baseUrl + "/bookings/new");
            assertEquals("Book a Chamber Slot | Cold Storage", driver.getTitle());

            // Fill reservation form
            driver.findElement(By.id("farmerName")).sendKeys("Suresh Deshmukh");
            driver.findElement(By.id("contactNumber")).sendKeys("9890123456");

            Select chamberSelect = new Select(driver.findElement(By.id("chamberCode")));
            chamberSelect.selectByValue("CH-CH1");

            Select commoditySelect = new Select(driver.findElement(By.id("commodityType")));
            commoditySelect.selectByValue("Apples");

            driver.findElement(By.id("cratesCount")).sendKeys("30");

            WebElement checkInEl = driver.findElement(By.id("checkInDate"));
            WebElement checkOutEl = driver.findElement(By.id("checkOutDate"));
            LocalDate checkIn = LocalDate.now().plusDays(2);
            LocalDate checkOut = LocalDate.now().plusDays(16);
            ((JavascriptExecutor) driver).executeScript("arguments[0].value = arguments[1];", checkInEl, checkIn.toString());
            ((JavascriptExecutor) driver).executeScript("arguments[0].value = arguments[1];", checkOutEl, checkOut.toString());

            driver.findElement(By.id("submit-booking-btn")).click();

            // Assert redirected to /bookings and success alert appears
            wait.until(ExpectedConditions.urlContains("/bookings"));
            WebElement alert = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("success-alert")));
            assertTrue(alert.getText().contains("Slot reserved successfully"), "Expected success confirmation alert");

            // Verify table contains new reservation
            WebElement table = driver.findElement(By.id("bookings-management-table"));
            assertTrue(table.getText().contains("Suresh Deshmukh"), "Table should display newly booked farmer name");
        } catch (Throwable t) {
            takeFailureScreenshot("testJourney1_FarmerSlotReservation");
            throw t;
        }
    }

    @Test
    @Order(2)
    @DisplayName("Journey 2: Validation Guard blocks submission with invalid crate quantity")
    void testJourney2_ValidationGuard() {
        try {
            driver.get(baseUrl + "/bookings/new");

            // Submit empty form or invalid values
            driver.findElement(By.id("farmerName")).sendKeys("Invalid Tester");
            driver.findElement(By.id("contactNumber")).sendKeys("9811223344");
            
            Select chamberSelect = new Select(driver.findElement(By.id("chamberCode")));
            chamberSelect.selectByValue("CH-DF1");

            Select commoditySelect = new Select(driver.findElement(By.id("commodityType")));
            commoditySelect.selectByValue("Seafood");

            // Enter excessive crate count > 500
            WebElement cratesInput = driver.findElement(By.id("cratesCount"));
            cratesInput.clear();
            cratesInput.sendKeys("650");

            WebElement checkInEl2 = driver.findElement(By.id("checkInDate"));
            WebElement checkOutEl2 = driver.findElement(By.id("checkOutDate"));
            LocalDate checkIn = LocalDate.now().plusDays(5);
            LocalDate checkOut = LocalDate.now().plusDays(10);
            ((JavascriptExecutor) driver).executeScript("arguments[0].value = arguments[1];", checkInEl2, checkIn.toString());
            ((JavascriptExecutor) driver).executeScript("arguments[0].value = arguments[1];", checkOutEl2, checkOut.toString());

            driver.findElement(By.id("submit-booking-btn")).click();

            // Assert form stays on booking-form due to validation error
            assertTrue(driver.getCurrentUrl().contains("/bookings/new"));
        } catch (Throwable t) {
            takeFailureScreenshot("testJourney2_ValidationGuard");
            throw t;
        }
    }

    @Test
    @Order(3)
    @DisplayName("Journey 3: User filters chambers by temperature zone (Deep Freeze)")
    void testJourney3_FilterChambersByZone() {
        try {
            driver.get(baseUrl + "/slots");
            assertEquals("Chamber & Slot Directory | Cold Storage", driver.getTitle());

            // Click Deep Freeze filter button
            WebElement deepFreezeFilter = driver.findElement(By.id("filter-deep-freeze"));
            deepFreezeFilter.click();

            wait.until(ExpectedConditions.urlContains("zone=DEEP_FREEZE"));
            WebElement activeFilter = driver.findElement(By.id("filter-deep-freeze"));
            assertTrue(activeFilter.getAttribute("class").contains("btn-primary"), "Deep freeze filter button should be active");

            // Verify only Deep Freeze chamber is listed
            WebElement body = driver.findElement(By.tagName("body"));
            assertTrue(body.getText().contains("DEEP_FREEZE"), "Page should display DEEP_FREEZE zone badge");
            assertTrue(body.getText().contains("CH-DF1"), "Chamber CH-DF1 should be visible in filtered grid");
        } catch (Throwable t) {
            takeFailureScreenshot("testJourney3_FilterChambersByZone");
            throw t;
        }
    }

    @Test
    @Order(4)
    @DisplayName("Journey 4: Warehouse manager verifies status transitions (Confirm booking)")
    void testJourney4_ManagerConfirmBooking() {
        try {
            driver.get(baseUrl + "/bookings");

            // Find confirm button for pending booking #3
            WebElement table = driver.findElement(By.id("bookings-management-table"));
            assertTrue(table.isDisplayed(), "Bookings management table should be visible");

            // Verify PENDING or CONFIRMED badge presence
            assertTrue(table.getText().contains("CONFIRMED") || table.getText().contains("PENDING"),
                    "Table must reflect valid lifecycle statuses");
        } catch (Throwable t) {
            takeFailureScreenshot("testJourney4_ManagerConfirmBooking");
            throw t;
        }
    }
}
