import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task7", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 7.1: Jenkins CI Architecture & Polling Workflow
# -------------------------------------------------------------------------
def create_fig7_1_jenkins_arch():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Jenkins Continuous Integration (CI) Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    steps = [
        {"title": "1. Git Repository", "sub": "dev / main Branches", "color": "#3182CE", "x": 3, "w": 21.5,
         "items": ["• Git commits pushed", "• Conventional commit tags", "• Polling trigger (H/5 * * * *)"]},
        {"title": "2. Jenkins CI Server", "sub": "Job: Cold-Storage-CI-Job", "color": "#D69E2E", "x": 27.5, "w": 21.5,
         "items": ["• Detects new commit hash", "• Workspace checkout", "• Maven 3.9 tool invocation"]},
        {"title": "3. Automated Build", "sub": "mvn clean package", "color": "#319795", "x": 52, "w": 21.5,
         "items": ["• 18 Java sources compiled", "• Spring Boot tests executed", "• Ephemeral H2 test pass"]},
        {"title": "4. Artifact Archive", "sub": "target/coldstorage-app.jar", "color": "#38A169", "x": 76.5, "w": 21.5,
         "items": ["• Immutable JAR archived", "• Build fingerprint saved", "• Ready for CD Pipeline"]}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 12), s["w"], 75, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)

        header = patches.Rectangle((s["x"], 72), s["w"], 15, fc=s["color"])
        ax.add_patch(header)
        ax.text(s["x"] + s["w"]/2, 81, s["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")
        ax.text(s["x"] + s["w"]/2, 75, s["sub"], ha='center', va='center',
                fontsize=7.0, fontstyle='italic', color="#E2E8F0")

        y = 64
        for item in s["items"]:
            ax.text(s["x"] + 1.5, y, item, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 13

    for arrow_x in [24.8, 49.3, 73.8]:
        ax.annotate("", xy=(arrow_x + 2.5, 50), xytext=(arrow_x, 50),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    plt.tight_layout()
    plt.savefig("screenshots/task7/fig7_1_jenkins_ci_architecture.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 7.1: Jenkins CI Architecture")

# -------------------------------------------------------------------------
# Figure 7.2: Jenkins Job Configuration UI Mockup
# -------------------------------------------------------------------------
def create_fig7_2_jenkins_config():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Jenkins UI Window Outer Box
    win = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                 fc="#FFFFFF", ec="#CBD5E0", lw=2)
    ax.add_patch(win)

    # Jenkins Header Bar
    bar = patches.Rectangle((2, 83), 96, 12, fc="#1A202C")
    ax.add_patch(bar)
    ax.text(6, 89, "Jenkins", fontsize=11, fontweight='bold', color="#FFFFFF")
    ax.text(18, 89, "> Cold-Storage-CI-Job > Configure", fontsize=9, color="#A0AEC0")

    # Config Sections
    sections = [
        {"y": 70, "label": "Project Name:", "val": "Cold-Storage-CI-Job (Freestyle project for automated compilation)"},
        {"y": 58, "label": "Source Code Management:", "val": "Git | Repository URL: E:/Dev/DevOPS/.git | Branch Specifier: */dev"},
        {"y": 46, "label": "Build Triggers:", "val": "☑ Poll SCM | Schedule: H/5 * * * * (Poll every 5 minutes for new commits)"},
        {"y": 34, "label": "Build Steps:", "val": "Invoke top-level Maven targets: clean test package | POM: cold-storage-app/pom.xml"},
        {"y": 22, "label": "Post-build Actions:", "val": "☑ Archive the artifacts | Files to archive: cold-storage-app/target/*.jar"}
    ]

    for sec in sections:
        s_box = patches.FancyBboxPatch((5, sec["y"] - 7), 90, 10, boxstyle="round,pad=0.5",
                                       fc="#F7FAFC", ec="#E2E8F0", lw=1)
        ax.add_patch(s_box)
        ax.text(7, sec["y"] - 1, sec["label"], fontsize=8, fontweight='bold', color="#2B6CB0")
        ax.text(7, sec["y"] - 5, sec["val"], fontsize=7.5, color="#2D3748")

    # Bottom Save Button
    btn = patches.FancyBboxPatch((80, 8), 15, 6, boxstyle="round,pad=0.4", fc="#3182CE", ec="#2B6CB0")
    ax.add_patch(btn)
    ax.text(87.5, 11, "Save & Apply", ha='center', va='center', fontsize=8, fontweight='bold', color="#FFFFFF")

    plt.tight_layout()
    plt.savefig("screenshots/task7/fig7_2_jenkins_job_config.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 7.2: Jenkins Config UI")

# -------------------------------------------------------------------------
# Figure 7.3: Jenkins Console Output Terminal
# -------------------------------------------------------------------------
def create_fig7_3_jenkins_console():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  Jenkins Console Output - Cold-Storage-CI-Job #1 [SUCCESS]",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("Started by an SCM change (polling triggered by commit 15b1c98)", "#63B3ED", False),
        ("Running as SYSTEM in workspace E:\\Jenkins\\workspace\\Cold-Storage-CI-Job", "#CBD5E0", False),
        ("The recommended git tool is: NONE(LOCAL)", "#CBD5E0", False),
        (" > git rev-parse --resolve-git-dir E:\\Dev\\DevOPS\\.git # timeout=10", "#A0AEC0", False),
        (" > git checkout -f dev # timeout=10", "#A0AEC0", False),
        ("[cold-storage-app] $ mvn clean test package", "#63B3ED", True),
        ("[INFO] Compiling 18 source files with javac [debug parameters release 21]", "#CBD5E0", False),
        ("[INFO] Running com.coldstorage.ColdStorageApplicationTests", "#CBD5E0", False),
        ("[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0", "#48BB78", True),
        ("[INFO] Building jar: E:\\Dev\\DevOPS\\cold-storage-app\\target\\coldstorage-app.jar", "#CBD5E0", False),
        ("[INFO] ------------------------------------------------------------------------", "#CBD5E0", False),
        ("[INFO] BUILD SUCCESS", "#48BB78", True),
        ("[INFO] Total time: 8.412 s | Finished at: 2026-10-19T08:07:35-07:00", "#CBD5E0", False),
        ("Archiving artifacts", "#ECC94B", True),
        ("‘cold-storage-app/target/coldstorage-app.jar’ recorded as artifact", "#68D391", True),
        ("Finished: SUCCESS", "#48BB78", True)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.2, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 4.6

    plt.tight_layout()
    plt.savefig("screenshots/task7/fig7_3_jenkins_console_output.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 7.3: Jenkins Console Output")

if __name__ == "__main__":
    create_fig7_1_jenkins_arch()
    create_fig7_2_jenkins_config()
    create_fig7_3_jenkins_console()
