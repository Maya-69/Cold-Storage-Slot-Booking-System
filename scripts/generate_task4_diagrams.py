import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task4", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 4.1: Git Branching Architecture & Policy Flow
# -------------------------------------------------------------------------
def create_fig4_1_branching():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Git Branching Strategy & Release Workflow",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    # Main Branch (Top Lane)
    ax.plot([5, 95], [75, 75], color="#2B6CB0", lw=3)
    ax.text(10, 81, "main (Protected Production Branch)", fontsize=9.5, fontweight='bold', color="#2B6CB0")
    ax.scatter([20, 80], [75, 75], s=120, color="#2B6CB0", zorder=3)
    ax.text(20, 70, "v0.1.0-init", ha='center', fontsize=7.5, fontweight='bold', color="#2D3748")
    ax.text(80, 70, "v1.0.0-release", ha='center', fontsize=7.5, fontweight='bold', color="#2D3748")

    # Dev Branch (Middle Lane)
    ax.plot([5, 95], [45, 45], color="#38A169", lw=3)
    ax.text(10, 51, "dev (Integration & Daily Development Branch)", fontsize=9.5, fontweight='bold', color="#38A169")
    ax.scatter([20, 40, 60, 80], [45, 45, 45, 45], s=100, color="#38A169", zorder=3)
    ax.text(40, 40, "Sprint 1 Base", ha='center', fontsize=7, color="#2D3748")
    ax.text(60, 40, "Feature Merged", ha='center', fontsize=7, color="#2D3748")

    # Feature Branch (Bottom Lane)
    ax.plot([25, 65], [18, 18], color="#D69E2E", lw=2.5, linestyle="--")
    ax.text(28, 23, "feature/slot-view (Isolated Feature Development)", fontsize=8.5, fontweight='bold', color="#D69E2E")
    ax.scatter([30, 45, 58], [18, 18, 18], s=80, color="#D69E2E", zorder=3)
    ax.text(30, 12, "feat: dir UI", ha='center', fontsize=6.8, color="#2D3748")
    ax.text(45, 12, "feat: filters", ha='center', fontsize=6.8, color="#2D3748")
    ax.text(58, 12, "test: pass", ha='center', fontsize=6.8, color="#2D3748")

    # Branch off from dev to feature
    ax.annotate("", xy=(30, 18), xytext=(20, 45),
                arrowprops=dict(arrowstyle="->", color="#D69E2E", lw=1.8, linestyle="--"))

    # Pull Request & Merge from feature into dev
    ax.annotate("", xy=(60, 45), xytext=(58, 18),
                arrowprops=dict(arrowstyle="->", color="#38A169", lw=1.8))
    ax.text(62, 30, "Pull Request\nReview & Merge", ha='left', va='center',
            fontsize=7.2, fontweight='bold', color="#276749")

    # Release merge from dev into main
    ax.annotate("", xy=(80, 75), xytext=(80, 45),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2))
    ax.text(83, 60, "Tagged Release\n(v1.0.0)", ha='left', va='center',
            fontsize=7.2, fontweight='bold', color="#1A365D")

    plt.tight_layout()
    plt.savefig("screenshots/task4/fig4_1_branching.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 4.1: Branching Diagram")

# -------------------------------------------------------------------------
# Figure 4.2: Terminal Git Log & Status Output Visual
# -------------------------------------------------------------------------
def create_fig4_2_terminal():
    fig, ax = plt.subplots(figsize=(10, 4.5), dpi=200)
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
    ax.text(5, 89.5, "● ● ●  PowerShell - Git Version Control Baseline & Commit Tree",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    lines = [
        ("PS E:\\Dev\\DevOPS> git status", "#63B3ED", True),
        ("On branch dev", "#48BB78", True),
        ("nothing to commit, working tree clean", "#CBD5E0", False),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> git branch -a", "#63B3ED", True),
        ("* dev", "#48BB78", True),
        ("  main", "#CBD5E0", False),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> git log --graph --oneline --all --decorate", "#63B3ED", True),
        ("* d014f24 (HEAD -> dev) docs: establish dev branch baseline and issue templates", "#ECC94B", False),
        ("* 17be392 (main) feat(arch): initialize Cold Storage Slot Booking System skeleton and Maven architecture", "#ECC94B", False),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> git config --get user.name && git config --get user.email", "#63B3ED", True),
        ("Mayuresh Sawant | 23102A0029@student.edu", "#68D391", True)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.6, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 5.8

    plt.tight_layout()
    plt.savefig("screenshots/task4/fig4_2_git_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 4.2: Git Terminal Visual")

if __name__ == "__main__":
    create_fig4_1_branching()
    create_fig4_2_terminal()
