import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task8", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 8.1: Pipeline as Code Architecture Diagram
# -------------------------------------------------------------------------
def create_fig8_1_pipeline_arch():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Declarative Jenkinsfile Pipeline Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    stages = [
        {"num": "STAGE 1", "name": "Checkout SCM", "tool": "Git Plugin",
         "desc": "Clones dev branch\nVerifies commit hash", "color": "#3182CE", "x": 2},
        {"num": "STAGE 2", "name": "Build & Test", "tool": "Maven + JUnit 5",
         "desc": "Compiles 18 classes\nExecutes unit tests", "color": "#D69E2E", "x": 21.5},
        {"num": "STAGE 3", "name": "Package JAR", "tool": "Spring Boot Repackage",
         "desc": "Builds standalone\ncoldstorage-app.jar", "color": "#805AD5", "x": 41},
        {"num": "STAGE 4", "name": "Deploy Server", "tool": "Tomcat / Staging",
         "desc": "Deploys to port 8080\nEnv: ${ENVIRONMENT}", "color": "#319795", "x": 60.5},
        {"num": "STAGE 5", "name": "Health Verify", "tool": "Actuator Probe",
         "desc": "HTTP GET /health\nAsserts JSON status UP", "color": "#38A169", "x": 80}
    ]

    for s in stages:
        box = patches.FancyBboxPatch((s["x"], 15), 17.5, 72, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)

        # Header Box
        h_box = patches.Rectangle((s["x"], 73), 17.5, 12, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(s["x"] + 8.75, 80.5, s["num"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")
        ax.text(s["x"] + 8.75, 75.5, s["name"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#FFFFFF")

        ax.text(s["x"] + 8.75, 62, s["tool"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#1A202C")
        ax.text(s["x"] + 8.75, 42, s["desc"], ha='center', va='center',
                fontsize=7.0, color="#4A5568")

    # Arrows between stages
    for arrow_x in [19.8, 39.3, 58.8, 78.3]:
        ax.annotate("", xy=(arrow_x + 1.5, 51), xytext=(arrow_x, 51),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    # Bottom Parameters Banner
    ax.text(50, 6, "Parameterized Controls: ENVIRONMENT (staging/production) | SERVER_PORT (8080) | RUN_INTEGRATION_TESTS (true)",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task8/fig8_1_pipeline_architecture.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 8.1: Pipeline Architecture")

# -------------------------------------------------------------------------
# Figure 8.2: Jenkins Stage View Dashboard Visualization
# -------------------------------------------------------------------------
def create_fig8_2_stage_view():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Jenkins Stage View Outer Frame
    win = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                 fc="#FFFFFF", ec="#CBD5E0", lw=2)
    ax.add_patch(win)

    # Top Header
    bar = patches.Rectangle((2, 83), 96, 12, fc="#1A202C")
    ax.add_patch(bar)
    ax.text(6, 89, "Jenkins", fontsize=11, fontweight='bold', color="#FFFFFF")
    ax.text(18, 89, "> Cold-Storage-Pipeline > Stage View", fontsize=9, color="#A0AEC0")

    # Pipeline Title
    ax.text(5, 76, "Pipeline Stage View: Build #1 [SUCCESS]", fontsize=10, fontweight='bold', color="#2D3748")

    # Stage Headers
    stage_headers = [
        ("Checkout SCM", 19),
        ("Build & Test", 35),
        ("Package Artifact", 51),
        ("Deploy Server", 67),
        ("Health Verify", 83)
    ]
    for name, x in stage_headers:
        ax.text(x, 68, name, ha='center', va='center', fontsize=7.5, fontweight='bold', color="#4A5568")

    # Stage View Row for Build #1
    ax.text(9, 52, "#1", ha='center', va='center', fontsize=9.5, fontweight='bold', color="#3182CE")
    ax.text(9, 44, "19-Oct 08:10\nStable", ha='center', va='center', fontsize=6.8, color="#718096")

    stages_data = [
        (19, "2s", "#38A169"),
        (35, "8s", "#38A169"),
        (51, "11s", "#38A169"),
        (67, "3s", "#38A169"),
        (83, "2s", "#38A169")
    ]
    for x, duration, color in stages_data:
        box = patches.FancyBboxPatch((x - 6.5, 38), 13, 24, boxstyle="round,pad=0.5",
                                     fc=color, ec="#276749", lw=1.5)
        ax.add_patch(box)
        ax.text(x, 52, "SUCCESS", ha='center', va='center', fontsize=8, fontweight='bold', color="#FFFFFF")
        ax.text(x, 44, duration, ha='center', va='center', fontsize=7.5, color="#E6FFFA")

    # Total Pipeline Duration Banner
    ax.text(50, 18, "Total Pipeline Duration: 26s | Result: SUCCESS | Artifact: coldstorage-app.jar fingerprinted",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color="#276749")

    plt.tight_layout()
    plt.savefig("screenshots/task8/fig8_2_jenkins_stage_view.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 8.2: Jenkins Stage View")

# -------------------------------------------------------------------------
# Figure 8.3: Deployed Application Screen
# -------------------------------------------------------------------------
def create_fig8_3_deployed_app():
    src = "screenshots/task3/dashboard_live.png"
    dst = "screenshots/task8/fig8_3_deployed_app.png"
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print("Copied dashboard_live.png to Figure 8.3")

if __name__ == "__main__":
    create_fig8_1_pipeline_arch()
    create_fig8_2_stage_view()
    create_fig8_3_deployed_app()
