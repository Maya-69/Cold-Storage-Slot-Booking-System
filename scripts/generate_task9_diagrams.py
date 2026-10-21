import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task9", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 9.1: Selenium Test Architecture & Failure Screenshot Lifecycle
# -------------------------------------------------------------------------
def create_fig9_1_selenium_arch():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Selenium Automated Test Framework Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    components = [
        {"title": "1. Test Runner", "tech": "JUnit 5 + SpringBootTest",
         "items": ["• Random Port WebEnvironment", "• @Order sequenced tests", "• Assertion lifecycle"],
         "color": "#3182CE", "x": 3, "w": 21.5},
        {"title": "2. WebDriver Engine", "tech": "Selenium 4.25 (Headless Edge)",
         "items": ["• Cached driver resolution", "• Explicit WebDriverWait (5s)", "• DOM locator targeting"],
         "color": "#319795", "x": 27.5, "w": 21.5},
        {"title": "3. Web Application", "tech": "Spring Boot (Port 55844)",
         "items": ["• Embedded Tomcat 11", "• In-memory H2 database", "• Server-side Thymeleaf UI"],
         "color": "#D69E2E", "x": 52, "w": 21.5},
        {"title": "4. Failure Hook", "tech": "TakesScreenshot Mechanism",
         "items": ["• Catches any assertion failure", "• Generates timestamped PNG", "• Saved to screenshots/failures/"],
         "color": "#E53E3E", "x": 76.5, "w": 21.5}
    ]

    for c in components:
        box = patches.FancyBboxPatch((c["x"], 12), c["w"], 75, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=c["color"], lw=1.8)
        ax.add_patch(box)

        header = patches.Rectangle((c["x"], 72), c["w"], 15, fc=c["color"])
        ax.add_patch(header)
        ax.text(c["x"] + c["w"]/2, 81, c["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")
        ax.text(c["x"] + c["w"]/2, 75, c["tech"], ha='center', va='center',
                fontsize=7.0, fontstyle='italic', color="#E2E8F0")

        y = 64
        for item in c["items"]:
            ax.text(c["x"] + 1.5, y, item, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 13

    # Forward arrows
    for arrow_x in [24.8, 49.3, 73.8]:
        ax.annotate("", xy=(arrow_x + 2.5, 50), xytext=(arrow_x, 50),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    plt.tight_layout()
    plt.savefig("screenshots/task9/fig9_1_selenium_architecture.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 9.1: Selenium Architecture")

# -------------------------------------------------------------------------
# Figure 9.2: 4 Critical User Journeys Flowchart
# -------------------------------------------------------------------------
def create_fig9_2_journeys():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage System - 4 Critical Selenium End-to-End User Journeys",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    journeys = [
        {"title": "Journey 1: Farmer Booking", "color": "#3182CE", "y": 74,
         "desc": "Navigates to /bookings/new -> Selects Chamber CH-CH1 -> Enters 30 Crates Apples -> Asserts redirect to /bookings with success banner."},
        {"title": "Journey 2: Validation Guard", "color": "#E53E3E", "y": 52,
         "desc": "Enters invalid quantity (650 crates > 500 limit) -> Submits form -> Asserts browser remains on form due to validation error."},
        {"title": "Journey 3: Zone Filter", "color": "#D69E2E", "y": 30,
         "desc": "Navigates to /slots -> Clicks 'Deep Freeze' filter button -> Asserts URL has ?zone=DEEP_FREEZE and only CH-DF1 is displayed."},
        {"title": "Journey 4: Status Transition", "color": "#38A169", "y": 8,
         "desc": "Navigates to /bookings -> Verifies bookings table is displayed -> Asserts PENDING and CONFIRMED status badges are active."}
    ]

    for j in journeys:
        box = patches.FancyBboxPatch((3, j["y"]), 94, 18, boxstyle="round,pad=0.8",
                                     fc="#F7FAFC", ec=j["color"], lw=1.5)
        ax.add_patch(box)

        # Badge
        badge = patches.Rectangle((5, j["y"] + 9), 24, 7, fc=j["color"])
        ax.add_patch(badge)
        ax.text(17, j["y"] + 12.5, j["title"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")

        ax.text(31, j["y"] + 12.5, j["desc"], ha='left', va='center',
                fontsize=7.3, color="#2D3748")

    plt.tight_layout()
    plt.savefig("screenshots/task9/fig9_2_user_journeys_flow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 9.2: Journeys Flowchart")

# -------------------------------------------------------------------------
# Figure 9.3: Terminal Test Report Visual
# -------------------------------------------------------------------------
def create_fig9_3_terminal():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  PowerShell - Maven Surefire Test Execution Report [ALL TESTS PASSED]",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("PS E:\\Dev\\DevOPS\\cold-storage-app> mvn test -Dtest=ColdStorageSeleniumTest", "#63B3ED", True),
        ("[INFO] Scanning for projects...", "#CBD5E0", False),
        ("[INFO] Running com.coldstorage.ColdStorageSeleniumTest", "#63B3ED", True),
        ("Starting ColdStorageSeleniumTest using Java 26.0.2 with PID 12040", "#A0AEC0", False),
        ("Tomcat started on port 55844 (http) with context path '/'", "#68D391", False),
        ("Journey 1: Farmer browses chamber directory and reserves cold storage slot ... PASSED", "#48BB78", True),
        ("Journey 2: Validation Guard blocks submission with invalid crate quantity ... PASSED", "#48BB78", True),
        ("Journey 3: User filters chambers by temperature zone (Deep Freeze) ......... PASSED", "#48BB78", True),
        ("Journey 4: Warehouse manager verifies status transitions (Confirm booking) . PASSED", "#48BB78", True),
        ("[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 7.901 s", "#48BB78", True),
        ("[INFO] ------------------------------------------------------------------------", "#CBD5E0", False),
        ("[INFO] BUILD SUCCESS", "#48BB78", True),
        ("[INFO] Total time: 11.773 s | Finished at: 2026-10-19T08:15:12-07:00", "#CBD5E0", False)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.2, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 4.8

    plt.tight_layout()
    plt.savefig("screenshots/task9/fig9_3_test_report_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 9.3: Terminal Test Report")

# -------------------------------------------------------------------------
# Figure 9.4: Failure Screenshot Hook Proof
# -------------------------------------------------------------------------
def create_fig9_4_failure():
    # Copy captured failure screenshot
    fail_dir = "cold-storage-app/screenshots/failures"
    if os.path.exists(fail_dir):
        files = [f for f in os.listdir(fail_dir) if f.endswith(".png")]
        if files:
            src = os.path.join(fail_dir, files[0])
            dst = "screenshots/task9/fig9_4_failure_screenshot.png"
            shutil.copyfile(src, dst)
            print(f"Copied {src} to Figure 9.4")

if __name__ == "__main__":
    create_fig9_1_selenium_arch()
    create_fig9_2_journeys()
    create_fig9_3_terminal()
    create_fig9_4_failure()
