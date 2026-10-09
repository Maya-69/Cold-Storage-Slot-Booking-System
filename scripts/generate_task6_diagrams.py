import os
import shutil
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task6", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 6.1: Conflict Creation & Resolution Architecture
# -------------------------------------------------------------------------
def create_fig6_1_conflict():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Merge Conflict Creation & Resolution Flow",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    steps = [
        {"title": "1. Branch Divergence", "color": "#3182CE", "x": 3, "w": 21.5,
         "items": ["• feature/booking-rules:", "  CSBS-RES- prefix", "• dev integration:", "  CSBS-2026- prefix"]},
        {"title": "2. Merge Collision", "color": "#E53E3E", "x": 27.5, "w": 21.5,
         "items": ["• git merge rules", "• CONFLICT in:", "  BookingService.java", "• Auto-merge failed"]},
        {"title": "3. Conflict Markers", "color": "#D69E2E", "x": 52, "w": 21.5,
         "items": ["• Inspect <<<<<<< HEAD", "• Inspect =======", "• Inspect >>>>>>>", "• Audit developer intent"]},
        {"title": "4. Resolution & Tag", "color": "#38A169", "x": 76.5, "w": 21.5,
         "items": ["• CSBS-2026-RES-", "• git commit resolution", "• git tag v1.0.0", "• Release merged to main"]}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 12), s["w"], 75, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)

        # Header Box
        h_box = patches.Rectangle((s["x"], 72), s["w"], 15, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(s["x"] + s["w"]/2, 80, s["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")

        # Items
        y = 63
        for item in s["items"]:
            ax.text(s["x"] + 1.5, y, item, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 13

    # Connectors
    for arrow_x in [24.8, 49.3, 73.8]:
        ax.annotate("", xy=(arrow_x + 2.5, 50), xytext=(arrow_x, 50),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    plt.tight_layout()
    plt.savefig("screenshots/task6/fig6_1_conflict_workflow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 6.1: Conflict Workflow Diagram")

# -------------------------------------------------------------------------
# Figure 6.2: Terminal Conflict Markers Visual
# -------------------------------------------------------------------------
def create_fig6_2_conflict_terminal():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  PowerShell - Git Merge Conflict Markers in BookingService.java",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("PS E:\\Dev\\DevOPS> git merge feature/booking-rules", "#63B3ED", True),
        ("Auto-merging cold-storage-app/.../BookingService.java", "#CBD5E0", False),
        ("CONFLICT (content): Merge conflict in cold-storage-app/.../BookingService.java", "#FEB2B2", True),
        ("Automatic merge failed; fix conflicts and then commit the result.", "#FEB2B2", True),
        ("", "#FFFFFF", False),
        ("--- [Inspect Conflict Markers in BookingService.java] ---", "#ECC94B", True),
        ("<<<<<<< HEAD", "#E53E3E", True),
        ('    // Dev Policy: CSBS-2026- format', "#CBD5E0", False),
        ('    String ref = "CSBS-2026-" + UUID.randomUUID().toString().substring(0, 8);', "#68D391", False),
        ("=======", "#E53E3E", True),
        ('    // Feature Policy: CSBS-RES- format', "#CBD5E0", False),
        ('    String ref = "CSBS-RES-" + UUID.randomUUID().toString().substring(0, 8);', "#63B3ED", False),
        (">>>>>>> feature/booking-rules", "#E53E3E", True),
        ("", "#FFFFFF", False),
        ("--- [Manual Harmonization & Resolution] ---", "#ECC94B", True),
        ('String ref = "CSBS-2026-RES-" + UUID.randomUUID().toString().substring(0, 8);', "#48BB78", True)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.2, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 4.5

    plt.tight_layout()
    plt.savefig("screenshots/task6/fig6_2_conflict_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 6.2: Conflict Terminal Visual")

# -------------------------------------------------------------------------
# Figure 6.3: Terminal Tag & Release Tree Visual
# -------------------------------------------------------------------------
def create_fig6_3_tag_terminal():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  PowerShell - Git Release v1.0.0 Tagging & Full Commit Graph",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("PS E:\\Dev\\DevOPS> git tag -a v1.0.0 -m \"Release v1.0.0: Fully Functional Cold Storage MVP\"", "#63B3ED", True),
        ("PS E:\\Dev\\DevOPS> git tag -n", "#63B3ED", True),
        ("v1.0.0          Release v1.0.0: Fully Functional Cold Storage Slot Booking System MVP", "#68D391", True),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> git log --graph --oneline --all -n 7", "#63B3ED", True),
        ("*   60ffbc1 (main) release: merge dev baseline into main for production release v1.0.0", "#63B3ED", True),
        ("|\\", "#63B3ED", True),
        ("| *   15b1c98 (tag: v1.0.0, dev) fix(merge): resolve booking reference format conflict", "#48BB78", True),
        ("| |\\", "#48BB78", True),
        ("| | * 1d657e3 (feature/booking-rules) feat(booking): implement CSBS-RES reference prefix", "#ECC94B", False),
        ("| * | a5b4c22 feat(booking): set CSBS-2026 reference format on dev branch", "#ECC94B", False),
        ("| |/", "#48BB78", True),
        ("| *   3e45a1f merge: pull request #1 from feature/slot-view into dev", "#805AD5", False),
        ("| * d014f24 docs: establish dev branch baseline and issue templates", "#CBD5E0", False),
        ("* 17be392 feat(arch): initialize Cold Storage Slot Booking System skeleton", "#CBD5E0", False)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.2, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 4.8

    plt.tight_layout()
    plt.savefig("screenshots/task6/fig6_3_tag_release_tree.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 6.3: Tag and Release Tree Visual")

def create_fig6_4_mvp_ui():
    src = "screenshots/task3/bookings_live.png"
    dst = "screenshots/task6/fig6_4_mvp_booking_live.png"
    if os.path.exists(src):
        shutil.copyfile(src, dst)
        print("Copied bookings_live.png to Figure 6.4")

if __name__ == "__main__":
    create_fig6_1_conflict()
    create_fig6_2_conflict_terminal()
    create_fig6_3_tag_terminal()
    create_fig6_4_mvp_ui()
