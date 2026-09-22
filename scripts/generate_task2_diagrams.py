import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task2", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 2.1: DevOps Lifecycle Diagram (Plan -> Code -> Build -> Test -> Release -> Deploy -> Operate -> Monitor)
# -------------------------------------------------------------------------
def create_fig2_1():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Cold Storage Slot Booking System - DevOps Continuous Delivery Lifecycle",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    stages = [
        {"name": "1. PLAN", "tool": "Jira / GitHub Issues", "sub": "Agile Backlog & User Stories", "color": "#2B6CB0", "x": 3, "y": 55},
        {"name": "2. CODE", "tool": "Java 21 / Spring Boot", "sub": "Git Feature Branching & PRs", "color": "#319795", "x": 27, "y": 55},
        {"name": "3. BUILD", "tool": "Apache Maven (mvnw)", "sub": "Deterministic JAR Compilation", "color": "#D69E2E", "x": 51, "y": 55},
        {"name": "4. TEST", "tool": "Selenium 4 & JUnit 5", "sub": "Headless Functional Quality Gate", "color": "#DD6B20", "x": 75, "y": 55},
        {"name": "5. RELEASE", "tool": "Docker Multi-Stage", "sub": "Versioned Container Packaging", "color": "#805AD5", "x": 75, "y": 15},
        {"name": "6. DEPLOY", "tool": "Jenkins CD Pipeline", "sub": "Automated Fresh Container Update", "color": "#D53F8C", "x": 51, "y": 15},
        {"name": "7. OPERATE", "tool": "Ansible Playbook", "sub": "Idempotent Server Provisioning", "color": "#38A169", "x": 27, "y": 15},
        {"name": "8. MONITOR", "tool": "Spring Boot Actuator", "sub": "Health Probe /actuator/health", "color": "#4A5568", "x": 3, "y": 15}
    ]

    for s in stages:
        box = patches.FancyBboxPatch((s["x"], s["y"]), 21.5, 30, boxstyle="round,pad=1.2",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)
        
        # Header banner
        header = patches.Rectangle((s["x"], s["y"] + 20), 21.5, 10, fc=s["color"])
        ax.add_patch(header)
        ax.text(s["x"] + 10.75, s["y"] + 25, s["name"], ha='center', va='center',
                fontsize=9.5, fontweight='bold', color="#FFFFFF")
        
        # Tool and Subtitle
        ax.text(s["x"] + 10.75, s["y"] + 13, s["tool"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#1A202C")
        ax.text(s["x"] + 10.75, s["y"] + 5, s["sub"], ha='center', va='center',
                fontsize=7.2, color="#4A5568")

    # Flow arrows: 1->2->3->4
    for arrow_x in [24.8, 48.8, 72.8]:
        ax.annotate("", xy=(arrow_x + 2, 70), xytext=(arrow_x, 70),
                    arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2))

    # Down arrow: 4->5
    ax.annotate("", xy=(85.75, 45.5), xytext=(85.75, 54.5),
                arrowprops=dict(arrowstyle="->", color="#DD6B20", lw=2))

    # Reverse flow: 5->6->7->8
    for arrow_x in [74.5, 50.5, 26.5]:
        ax.annotate("", xy=(arrow_x - 1.8, 30), xytext=(arrow_x, 30),
                    arrowprops=dict(arrowstyle="->", color="#805AD5", lw=2))

    # Loop back arrow: 8 -> 1
    ax.annotate("", xy=(13.75, 54.5), xytext=(13.75, 45.5),
                arrowprops=dict(arrowstyle="->", color="#38A169", lw=2))
    ax.text(14, 50, "Continuous Feedback Loop", ha='center', va='center', fontsize=6.8,
            fontweight='bold', color="#276749", backgroundcolor="#F0FFF4")

    plt.tight_layout()
    plt.savefig("screenshots/task2/fig1_devops_lifecycle.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 2.1")

# -------------------------------------------------------------------------
# Figure 2.2: Agile Scrum/Kanban Task Board & Sprint Planning Progression
# -------------------------------------------------------------------------
def create_fig2_2():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Cold Storage Slot Booking System - 15-Task Kanban Sprint Board",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    columns = [
        {"title": "PRODUCT BACKLOG", "color": "#718096", "x": 2, "w": 22.5,
         "cards": [
             ("Task 13: Ansible Inventory", "5 SP | Infrastructure"),
             ("Task 14: Idempotent Run", "5 SP | Reliability"),
             ("Task 15: Final Release/Viva", "8 SP | Release")
         ]},
        {"title": "SPRINT BACKLOG", "color": "#3182CE", "x": 26.5, "w": 22.5,
         "cards": [
             ("Task 9: Selenium Suite", "5 SP | Automated QA"),
             ("Task 10: Jenkins QA Gate", "5 SP | CI Gate"),
             ("Task 11: Docker Container", "3 SP | Containerization"),
             ("Task 12: Continuous Deploy", "5 SP | CD Pipeline")
         ]},
        {"title": "IN PROGRESS / REVIEW", "color": "#D69E2E", "x": 51, "w": 22.5,
         "cards": [
             ("Task 5: Feature Branching", "3 SP | Git Workflow"),
             ("Task 6: MVP Completion", "5 SP | Collaboration"),
             ("Task 7: Jenkins CI Build", "5 SP | CI Job"),
             ("Task 8: Jenkinsfile Pipeline", "5 SP | Pipeline-as-Code")
         ]},
        {"title": "DONE (VERIFIED)", "color": "#38A169", "x": 75.5, "w": 22.5,
         "cards": [
             ("Task 1: Problem & Scope", "3 SP | Inception"),
             ("Task 2: Agile Planning", "3 SP | Scrum/DoD"),
             ("Task 3: Architecture Setup", "5 SP | Baseline"),
             ("Task 4: GitHub Repo Init", "2 SP | VCS Skeleton")
         ]}
    ]

    for col in columns:
        # Outer Column Box
        c_box = patches.FancyBboxPatch((col["x"], 6), col["w"], 83, boxstyle="round,pad=1.0",
                                       fc="#F7FAFC", ec=col["color"], lw=1.5)
        ax.add_patch(c_box)

        # Header Box
        h_box = patches.Rectangle((col["x"], 81), col["w"], 8, fc=col["color"])
        ax.add_patch(h_box)
        ax.text(col["x"] + col["w"]/2, 85, col["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")

        # Cards
        y = 72
        for title, meta in col["cards"]:
            card = patches.FancyBboxPatch((col["x"] + 1, y - 11), col["w"] - 2, 11,
                                          boxstyle="round,pad=0.6", fc="#FFFFFF", ec="#CBD5E0", lw=1)
            ax.add_patch(card)
            ax.text(col["x"] + 2, y - 4, title, ha='left', va='center',
                    fontsize=7.5, fontweight='bold', color="#2D3748")
            ax.text(col["x"] + 2, y - 9, meta, ha='left', va='center',
                    fontsize=6.8, color="#718096")
            y -= 14

    plt.tight_layout()
    plt.savefig("screenshots/task2/fig2_kanban_board.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 2.2")

# -------------------------------------------------------------------------
# Figure 2.3: Sprint Velocity and Story Point Breakdown
# -------------------------------------------------------------------------
def create_fig2_3():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
    
    sprints = ['Sprint 1:\nFoundations\n(Tasks 1-4)',
               'Sprint 2:\nCore Features\n(Tasks 5-6)',
               'Sprint 3:\nCI & Testing\n(Tasks 7-10)',
               'Sprint 4:\nDocker & Ansible\n(Tasks 11-15)']
    story_points = [13, 8, 20, 26]
    colors = ['#3182CE', '#38A169', '#D69E2E', '#805AD5']

    bars = ax.bar(sprints, story_points, color=colors, width=0.45, edgecolor='#2D3748', linewidth=1.2)
    ax.set_ylabel('Committed Story Points (SP)', fontsize=10, fontweight='bold', color='#1A365D')
    ax.set_title('Sprint Capacity and Velocity Distribution (Total: 67 Story Points across 15 Tasks)',
                 fontsize=11, fontweight='bold', color='#1A365D', pad=12)
    ax.set_ylim(0, 32)
    ax.grid(axis='y', linestyle='--', alpha=0.5)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height} SP',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 4), textcoords="offset points",
                    ha='center', va='bottom', fontsize=9.5, fontweight='bold', color='#2D3748')

    plt.tight_layout()
    plt.savefig("screenshots/task2/fig3_sprint_velocity.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 2.3")

if __name__ == "__main__":
    create_fig2_1()
    create_fig2_2()
    create_fig2_3()
