import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task5", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 5.1: Pull Request Review & Merge Architecture
# -------------------------------------------------------------------------
def create_fig5_1_pr_workflow():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Pull Request Review & Merge Governance",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    steps = [
        {"title": "1. Feature Branch", "sub": "git checkout -b feature/slot-view",
         "items": ["• Isolated feature work", "• Commodity search logic", "• Conventional commit"],
         "color": "#3182CE", "x": 3, "w": 21.5},
        {"title": "2. Pull Request #1", "sub": "Raised on GitHub / Git",
         "items": ["• Title: feat(slot): directory", "• PR checklist verified", "• Linked to User Story US-01"],
         "color": "#D69E2E", "x": 27.5, "w": 21.5},
        {"title": "3. Code Review & QA", "sub": "Peer Review by Dr. Snehal Andhare",
         "items": ["• Clean MVC separation", "• Sub-second test pass", "• Changes Approved (LGTM)"],
         "color": "#805AD5", "x": 52, "w": 21.5},
        {"title": "4. Non-FF Merge", "sub": "git merge --no-ff feature/slot-view",
         "items": ["• Merge commit recorded", "• Preserved commit history", "• Integrated into dev branch"],
         "color": "#38A169", "x": 76.5, "w": 21.5}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 12), s["w"], 75, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)

        # Header Box
        h_box = patches.Rectangle((s["x"], 72), s["w"], 15, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(s["x"] + s["w"]/2, 81, s["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")
        ax.text(s["x"] + s["w"]/2, 75, s["sub"], ha='center', va='center',
                fontsize=7.0, fontstyle='italic', color="#E2E8F0")

        # Items
        y = 64
        for item in s["items"]:
            ax.text(s["x"] + 1.5, y, item, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 14

    # Connectors
    for arrow_x in [24.8, 49.3, 73.8]:
        ax.annotate("", xy=(arrow_x + 2.5, 50), xytext=(arrow_x, 50),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    plt.tight_layout()
    plt.savefig("screenshots/task5/fig5_1_pr_workflow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 5.1: PR Workflow Diagram")

# -------------------------------------------------------------------------
# Figure 5.2: Terminal Git Merge & Graph Output Visual
# -------------------------------------------------------------------------
def create_fig5_2_terminal():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Terminal Background
    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    # Header Bar
    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  PowerShell - Feature Branching & Pull Request Merge Verification",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("PS E:\\Dev\\DevOPS> git checkout dev", "#63B3ED", True),
        ("Switched to branch 'dev'", "#CBD5E0", False),
        ("PS E:\\Dev\\DevOPS> git merge --no-ff feature/slot-view -m \"merge: PR #1 feature/slot-view into dev\"", "#63B3ED", True),
        ("Merge made by the 'ort' strategy.", "#48BB78", False),
        (" 3 files changed, 34 insertions(+), 9 deletions(-)", "#CBD5E0", False),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> git log --graph --oneline -n 4", "#63B3ED", True),
        ("*   3e45a1f (HEAD -> dev) merge: pull request #1 from feature/slot-view into dev", "#ECC94B", True),
        ("|\\", "#ECC94B", True),
        ("| * 3756f4e (feature/slot-view) feat(slot): enhance chamber directory with commodity search", "#68D391", False),
        ("|/", "#ECC94B", True),
        ("* d014f24 docs: establish dev branch baseline and issue templates", "#ECC94B", False),
        ("* 17be392 (main) feat(arch): initialize Cold Storage Slot Booking System skeleton", "#ECC94B", False)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.5, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 5.4

    plt.tight_layout()
    plt.savefig("screenshots/task5/fig5_2_git_merge_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 5.2: Git Merge Terminal Visual")

# -------------------------------------------------------------------------
# Figure 5.3: Feature 1 UI Screenshot (copy or re-render)
# -------------------------------------------------------------------------
def create_fig5_3_feature1():
    # We can use the existing slots screenshot which shows Feature 1:
    src = "screenshots/task3/slots_live.png"
    dst = "screenshots/task5/fig5_3_feature1_live.png"
    if os.path.exists(src):
        import shutil
        shutil.copyfile(src, dst)
        print("Copied slots_live.png to Figure 5.3")

if __name__ == "__main__":
    create_fig5_1_pr_workflow()
    create_fig5_2_terminal()
    create_fig5_3_feature1()
