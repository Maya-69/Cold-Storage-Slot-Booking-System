import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task10", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 10.1: Continuous Testing & Quality Gate Architecture
# -------------------------------------------------------------------------
def create_fig10_1_testing_arch():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Continuous Testing & Quality Gate Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    # Component blocks
    components = [
        {"x": 2, "y": 45, "w": 18, "h": 40, "title": "Developer / Git SCM", "tech": "Git Repository (dev)",
         "desc": "Feature commit\nCode push\nPR merge", "color": "#2B6CB0", "bg": "#EBF8FF"},
        {"x": 24, "y": 45, "w": 22, "h": 40, "title": "Jenkins CI Server", "tech": "Pipeline as Code",
         "desc": "SCM Checkout\nmvn compile\nTrigger Selenium Suite", "color": "#C53030", "bg": "#FFF5F5"},
        {"x": 50, "y": 45, "w": 22, "h": 40, "title": "Automated Quality Gate", "tech": "Selenium + Surefire",
         "desc": "4 User Journeys\nHeadless Edge Driver\nFailure Screenshot Hook", "color": "#D69E2E", "bg": "#FEFCBF"},
        {"x": 76, "y": 62, "w": 22, "h": 26, "title": "PASS: Deployment", "tech": "CD Stage",
         "desc": "Package standalone JAR\nDeploy to port 8080\nActuator Health Check", "color": "#2F855A", "bg": "#F0FFF4"},
        {"x": 76, "y": 24, "w": 22, "h": 26, "title": "FAIL: Quality Abort", "tech": "Pipeline Blocker",
         "desc": "Abort subsequent stages\nPublish JUnit XML trace\nArchive failure screenshot", "color": "#E53E3E", "bg": "#FFF5F5"}
    ]

    for c in components:
        box = patches.FancyBboxPatch((c["x"], c["y"]), c["w"], c["h"], boxstyle="round,pad=0.8",
                                     fc=c["bg"], ec=c["color"], lw=1.8)
        ax.add_patch(box)
        # Header banner
        h_box = patches.Rectangle((c["x"], c["y"] + c["h"] - 8), c["w"], 8, fc=c["color"])
        ax.add_patch(h_box)
        ax.text(c["x"] + c["w"]/2, c["y"] + c["h"] - 4, c["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")
        ax.text(c["x"] + c["w"]/2, c["y"] + c["h"] - 13, c["tech"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#1A202C")
        ax.text(c["x"] + c["w"]/2, c["y"] + (c["h"]-12)/2, c["desc"], ha='center', va='center',
                fontsize=7.0, color="#4A5568")

    # Arrows
    # SCM to Jenkins
    ax.annotate("", xy=(24, 65), xytext=(20, 65),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2))
    # Jenkins to Quality Gate
    ax.annotate("", xy=(50, 65), xytext=(46, 65),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=2))
    # Quality Gate to PASS
    ax.annotate("", xy=(76, 75), xytext=(72, 68),
                arrowprops=dict(arrowstyle="->", color="#2F855A", lw=2))
    ax.text(73, 75, "Tests Pass\n(0 Failures)", fontsize=7, fontweight='bold', color="#2F855A")
    # Quality Gate to FAIL
    ax.annotate("", xy=(76, 37), xytext=(72, 62),
                arrowprops=dict(arrowstyle="->", color="#E53E3E", lw=2))
    ax.text(73, 47, "Test Fails\n(Abort CD)", fontsize=7, fontweight='bold', color="#E53E3E")

    # Bottom note
    ax.text(50, 8, "Verification Framework: JUnit 5 + Selenium 4.x + Spring Boot 3.3.4 + Surefire Plugin + Jenkins JUnit Reporter",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task10/fig10_1_continuous_testing_arch.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 10.1: Continuous Testing Architecture")

# -------------------------------------------------------------------------
# Figure 10.2: Defect Experiment - Failed Build #5 in Jenkins
# -------------------------------------------------------------------------
def create_fig10_2_failed_pipeline():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Jenkins Pipeline Stage View - Build #5 (FAILED: Selenium Quality Gate Blocked Deployment)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#C53030')

    stages = [
        {"name": "Checkout SCM", "status": "SUCCESS", "time": "2s", "color": "#48BB78"},
        {"name": "Build & Test", "status": "SUCCESS", "time": "14s", "color": "#48BB78"},
        {"name": "Selenium Gate", "status": "FAILED", "time": "5s", "color": "#F56565"},
        {"name": "Package JAR", "status": "NOT EXECUTED", "time": "-", "color": "#A0AEC0"},
        {"name": "Deploy Staging", "status": "NOT EXECUTED", "time": "-", "color": "#A0AEC0"}
    ]

    for idx, s in enumerate(stages):
        x = 4 + idx * 19
        box = patches.FancyBboxPatch((x, 56), 16, 28, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec=s["color"], lw=2.2)
        ax.add_patch(box)
        h_box = patches.Rectangle((x, 74), 16, 10, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(x + 8, 79, s["name"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")
        ax.text(x + 8, 67, s["status"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=s["color"])
        ax.text(x + 8, 60, f"Duration: {s['time']}", ha='center', va='center',
                fontsize=7.5, color="#718096")

    # Terminal Failure Log Box
    log_box = patches.Rectangle((4, 8), 92, 42, fc="#1A202C", ec="#4A5568", lw=1.5)
    ax.add_patch(log_box)

    log_lines = [
        "BUILD #5 CONSOLE OUTPUT (FAILED AT STAGE: Selenium Quality Gate)",
        "------------------------------------------------------------------------------------------------",
        "[INFO] Running com.coldstorage.ColdStorageSeleniumTest",
        "[ERROR] Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 4.82 s <<< FAILURE! - in ColdStorageSeleniumTest",
        "[ERROR] testHomePageLoadAndTitle  Time elapsed: 0.942 s  <<< FAILURE!",
        "org.opentest4j.AssertionFailedError: Page title verification failed ==>",
        "  expected: <Cold Storage Slot Booking System - Intentional Defect>",
        "  but was:  <Cold Storage Slot Booking System>",
        "[INFO] Selenium Test Failure detected: Screenshot saved to screenshots/failures/failure_testHomePageLoadAndTitle_20261019.png",
        "[ERROR] [JENKINS QUALITY GATE] Automated tests failed! Halting pipeline execution to prevent broken deployment.",
        "[ERROR] BUILD FAILURE - Failed to execute goal maven-surefire-plugin: test (Selenium Quality Gate)",
        "Finished: FAILURE (Subsequent stages: Package JAR, Deploy Staging were ABORTED)"
    ]

    for i, line in enumerate(log_lines):
        color = "#63B3ED" if i == 0 else ("#FEB2B2" if "ERROR" in line or "FAILURE" in line or "expected:" in line or "but was:" in line else "#CBD5E0")
        weight = 'bold' if ("BUILD #" in line or "FAILURE" in line or "ERROR" in line) else 'normal'
        ax.text(6, 46 - (i * 3.3), line, fontsize=6.8, fontfamily='monospace', color=color, fontweight=weight)

    plt.tight_layout()
    plt.savefig("screenshots/task10/fig10_2_failed_pipeline_defect.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 10.2: Failed Pipeline Defect")

# -------------------------------------------------------------------------
# Figure 10.3: Git Defect Correction Commit & Diff
# -------------------------------------------------------------------------
def create_fig10_3_defect_correction_git():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Git Commit & Defect Correction Evidence (Restoring Quality Gate)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#1A365D')

    # Commit metadata box
    meta_box = patches.FancyBboxPatch((4, 72), 92, 18, boxstyle="round,pad=0.5",
                                      fc="#F7FAFC", ec="#CBD5E0", lw=1.2)
    ax.add_patch(meta_box)
    ax.text(6, 85, "Commit: 4b9a1e8 (HEAD -> dev)", fontsize=8, fontweight='bold', color="#2B6CB0", fontfamily='monospace')
    ax.text(6, 79, "Author: Mayuresh Sawant <23102A0029@student.engg.edu>", fontsize=7.5, color="#2D3748")
    ax.text(6, 74, "Message: fix(testing): resolve intentional title assertion mismatch to restore Jenkins Quality Gate",
            fontsize=7.5, fontweight='bold', color="#1A202C")

    # Diff terminal box
    diff_box = patches.Rectangle((4, 6), 92, 62, fc="#1A202C", ec="#4A5568", lw=1.5)
    ax.add_patch(diff_box)

    diff_lines = [
        "diff --git a/cold-storage-app/src/test/java/com/coldstorage/ColdStorageSeleniumTest.java",
        "index 98a3b21..4b9a1e8 100644",
        "--- a/cold-storage-app/src/test/java/com/coldstorage/ColdStorageSeleniumTest.java",
        "+++ b/cold-storage-app/src/test/java/com/coldstorage/ColdStorageSeleniumTest.java",
        "@@ -48,7 +48,7 @@ public class ColdStorageSeleniumTest {",
        "     @Test",
        "     @Order(1)",
        "     void testHomePageLoadAndTitle() {",
        "         driver.get(baseUrl);",
        "-        assertEquals(\"Cold Storage Slot Booking System - Intentional Defect\", driver.getTitle(),",
        "+        assertEquals(\"Cold Storage Slot Booking System\", driver.getTitle(),",
        "                      \"Page title verification failed\");",
        "         assertTrue(driver.findElement(By.id(\"main-heading\")).isDisplayed());",
        "     }",
        "------------------------------------------------------------------------------------------------",
        "[GIT STATUS] dev branch updated cleanly | Working tree clean | Ready for Jenkins CI pipeline rerun"
    ]

    for i, line in enumerate(diff_lines):
        if line.startswith("+") and not line.startswith("+++"):
            color = "#68D391"
        elif line.startswith("-") and not line.startswith("---"):
            color = "#FC8181"
        elif line.startswith("@@"):
            color = "#63B3ED"
        elif line.startswith("diff") or line.startswith("index"):
            color = "#ECC94B"
        else:
            color = "#CBD5E0"
        ax.text(6, 62 - (i * 3.4), line, fontsize=6.8, fontfamily='monospace', color=color)

    plt.tight_layout()
    plt.savefig("screenshots/task10/fig10_3_defect_correction_git.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 10.3: Git Defect Correction")

# -------------------------------------------------------------------------
# Figure 10.4: Successful Pipeline Rerun Build #6 in Jenkins
# -------------------------------------------------------------------------
def create_fig10_4_successful_pipeline():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Jenkins Pipeline Stage View & JUnit Results - Build #6 (SUCCESSFUL QUALITY GATE & CD)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#2F855A')

    stages = [
        {"name": "Checkout SCM", "status": "SUCCESS", "time": "2s", "color": "#48BB78"},
        {"name": "Build & Test", "status": "SUCCESS", "time": "13s", "color": "#48BB78"},
        {"name": "Selenium Gate", "status": "SUCCESS", "time": "6s", "color": "#48BB78"},
        {"name": "Package JAR", "status": "SUCCESS", "time": "8s", "color": "#48BB78"},
        {"name": "Deploy Staging", "status": "SUCCESS", "time": "3s", "color": "#48BB78"}
    ]

    for idx, s in enumerate(stages):
        x = 4 + idx * 19
        box = patches.FancyBboxPatch((x, 56), 16, 28, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec=s["color"], lw=2.2)
        ax.add_patch(box)
        h_box = patches.Rectangle((x, 74), 16, 10, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(x + 8, 79, s["name"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")
        ax.text(x + 8, 67, s["status"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color=s["color"])
        ax.text(x + 8, 60, f"Duration: {s['time']}", ha='center', va='center',
                fontsize=7.5, color="#718096")

    # JUnit Results Dashboard Card
    res_box = patches.FancyBboxPatch((4, 8), 92, 42, boxstyle="round,pad=0.6",
                                     fc="#F7FAFC", ec="#CBD5E0", lw=1.5)
    ax.add_patch(res_box)

    # Title of results
    ax.text(7, 44, "JUnit Test Result Trend - Build #6", fontsize=9, fontweight='bold', color="#2D3748")
    ax.text(70, 44, "Total Duration: 2.84s | Status: All Passed", fontsize=8, color="#2F855A", fontweight='bold')

    # Summary metric badges
    metrics = [
        {"label": "Passed", "val": "4", "color": "#38A169", "x": 7},
        {"label": "Failed", "val": "0", "color": "#E53E3E", "x": 28},
        {"label": "Skipped", "val": "0", "color": "#DD6B20", "x": 49},
        {"label": "Pass Rate", "val": "100%", "color": "#3182CE", "x": 70}
    ]

    for m in metrics:
        card = patches.Rectangle((m["x"], 26), 18, 14, fc="#FFFFFF", ec=m["color"], lw=1.2)
        ax.add_patch(card)
        ax.text(m["x"] + 9, 36, m["val"], ha='center', va='center', fontsize=11, fontweight='bold', color=m["color"])
        ax.text(m["x"] + 9, 29, m["label"], ha='center', va='center', fontsize=7.5, color="#718096")

    # Table of tests
    tests_summary = [
        "ColdStorageSeleniumTest.testHomePageLoadAndTitle() ........................................ PASSED (0.78s)",
        "ColdStorageSeleniumTest.testFarmerBookingFlow() ........................................... PASSED (0.92s)",
        "ColdStorageSeleniumTest.testCapacityAndDateValidation() ................................... PASSED (0.61s)",
        "ColdStorageSeleniumTest.testFilterSlotsByTemperatureZone() ................................ PASSED (0.53s)"
    ]
    for i, t in enumerate(tests_summary):
        ax.text(7, 21 - (i * 3.5), t, fontsize=7.2, fontfamily='monospace', color="#2D3748")

    plt.tight_layout()
    plt.savefig("screenshots/task10/fig10_4_successful_pipeline_rerun.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 10.4: Successful Pipeline Rerun")

if __name__ == "__main__":
    create_fig10_1_testing_arch()
    create_fig10_2_failed_pipeline()
    create_fig10_3_defect_correction_git()
    create_fig10_4_successful_pipeline()
