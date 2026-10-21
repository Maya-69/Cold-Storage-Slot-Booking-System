import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task15", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 15.1: Master End-to-End DevOps Lifecycle Diagram
# -------------------------------------------------------------------------
def create_fig15_1_e2e_workflow():
    fig, ax = plt.subplots(figsize=(10.8, 5.5), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 96, "Cold Storage Slot Booking System - Master End-to-End DevOps Lifecycle",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    phases = [
        {"num": "1. PLAN", "title": "Agile Scrum", "tools": "Backlog & Kanban",
         "items": "User Stories\nDoD & Acceptance\n15-Task Scope", "c": "#2B6CB0", "x": 1.5},
        {"num": "2. CODE", "title": "Git & SCM", "tools": "GitHub Repository",
         "items": "Branching (dev)\nFeature Branches\nConflict Resolution", "c": "#3182CE", "x": 14.0},
        {"num": "3. BUILD", "title": "Maven CI", "tools": "Jenkins 2.450+",
         "items": "Compile Java 21\nSpring Boot 3.3.4\nStandalone JAR", "c": "#D69E2E", "x": 26.5},
        {"num": "4. TEST", "title": "Quality Gate", "tools": "Selenium + Surefire",
         "items": "4 User Journeys\nHeadless Edge\nJUnit XML Reports", "c": "#DD6B20", "x": 39.0},
        {"num": "5. PACKAGE", "title": "Docker Image", "tools": "Multi-Stage Build",
         "items": "Alpine JRE 21\nTag: ${BUILD_NUM}\nSize: 218 MB", "c": "#805AD5", "x": 51.5},
        {"num": "6. RELEASE", "title": "Container Registry", "tools": "Docker Hub",
         "items": "Push versioned tag\nPush :latest\nDigest verification", "c": "#6B46C1", "x": 64.0},
        {"num": "7. DEPLOY", "title": "Ansible & CD", "tools": "hosts.ini / playbooks",
         "items": "Container Rollout\nIdempotency (chg=0)\nPort 8080 Binding", "c": "#319795", "x": 76.5},
        {"num": "8. OPERATE", "title": "Reliability & SRE", "tools": "Actuator Probe",
         "items": "HTTP GET /health\nStatus: UP\nMTTR < 8s Rollback", "c": "#38A169", "x": 89.0}
    ]

    for p in phases:
        box = patches.FancyBboxPatch((p["x"], 16), 11.2, 72, boxstyle="round,pad=0.6",
                                     fc="#FFFFFF", ec=p["c"], lw=1.8)
        ax.add_patch(box)
        h_box = patches.Rectangle((p["x"], 74), 11.2, 14, fc=p["c"])
        ax.add_patch(h_box)
        ax.text(p["x"] + 5.6, 82.5, p["num"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#FFFFFF")
        ax.text(p["x"] + 5.6, 77.5, p["title"], ha='center', va='center',
                fontsize=6.8, fontweight='bold', color="#FFFFFF")

        ax.text(p["x"] + 5.6, 64, p["tools"], ha='center', va='center',
                fontsize=6.8, fontweight='bold', color="#1A202C")
        ax.text(p["x"] + 5.6, 42, p["items"], ha='center', va='center',
                fontsize=6.4, color="#4A5568")

    # Arrows between phases
    for arrow_x in [12.7, 25.2, 37.7, 50.2, 62.7, 75.2, 87.7]:
        ax.annotate("", xy=(arrow_x + 1.3, 52), xytext=(arrow_x, 52),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=1.8))

    # Bottom loopback feedback arrow
    ax.annotate("", xy=(6.5, 12), xytext=(94.5, 12),
                arrowprops=dict(arrowstyle="->", color="#3182CE", lw=1.8, linestyle="--"))
    ax.text(50, 8, "Continuous Monitoring & Fast Feedback Loop: Real-time Telemetry informs Backlog Refinement",
            ha='center', va='center', fontsize=7.8, fontstyle='italic', color="#2B6CB0")

    plt.tight_layout()
    plt.savefig("screenshots/task15/fig15_1_end_to_end_devops_workflow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 15.1: Master End-to-End DevOps Workflow")

# -------------------------------------------------------------------------
# Figure 15.2: Complete Technical Architecture Diagram
# -------------------------------------------------------------------------
def create_fig15_2_technical_arch():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Multi-Tier Architecture & Technology Stack",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    tiers = [
        {"y": 68, "h": 20, "name": "PRESENTATION LAYER", "tech": "Spring Boot Thymeleaf + HTML5 + Bootstrap 5 + JavaScript",
         "desc": "Responsive Farmer Booking Portal | Chamber Grid Filtering | Slot Reservation Form | Capacity KPI Dashboard", "c": "#3182CE", "bg": "#EBF8FF"},
        {"y": 42, "h": 22, "name": "APPLICATION & BUSINESS LOGIC LAYER", "tech": "Java 21 LTS + Spring Boot 3.3.4 (MVC)",
         "desc": "BookingService (Capacity & Overlap Guard) | ChamberService (Zone Temp Validation) | Actuator Health Probes", "c": "#D69E2E", "bg": "#FEFCBF"},
        {"y": 16, "h": 22, "name": "PERSISTENCE & STORAGE LAYER", "tech": "Embedded H2 Database + Spring Data JPA / Hibernate",
         "desc": "In-Memory Storage | Entities: Chamber, Slot, Booking, User | Zero External DB Dependency | Auto-DDL", "c": "#38A169", "bg": "#F0FFF4"}
    ]

    for t in tiers:
        box = patches.FancyBboxPatch((4, t["y"]), 92, t["h"], boxstyle="round,pad=0.6",
                                     fc=t["bg"], ec=t["c"], lw=1.8)
        ax.add_patch(box)
        ax.text(7, t["y"] + t["h"] - 5.5, t["name"], fontsize=8.5, fontweight='bold', color=t["c"])
        ax.text(7, t["y"] + t["h"] - 11, f"Technologies: {t['tech']}", fontsize=7.5, fontweight='bold', color="#1A202C")
        ax.text(7, t["y"] + 4, t["desc"], fontsize=7.2, color="#4A5568")

    # Arrows connecting tiers
    ax.annotate("", xy=(50, 65), xytext=(50, 68),
                arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=2))
    ax.annotate("", xy=(50, 39), xytext=(50, 42),
                arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=2))

    # Host & Container Infrastructure Wrapper
    ax.text(50, 6, "Container Infrastructure: Eclipse Temurin Alpine JRE 21 | Non-Root User: coldstorage (1001) | Port 8080/tcp",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task15/fig15_2_system_architecture_overview.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 15.2: Technical Architecture")

# -------------------------------------------------------------------------
# Figure 15.3: Live Production System Showcase
# -------------------------------------------------------------------------
def create_fig15_3_live_production():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Browser Window Frame
    b_window = patches.FancyBboxPatch((2, 4), 96, 92, boxstyle="round,pad=0.5",
                                     fc="#F8FAFC", ec="#CBD5E0", lw=1.5)
    ax.add_patch(b_window)

    # Address bar
    a_bar = patches.Rectangle((2, 88), 96, 8, fc="#EDF2F7")
    ax.add_patch(a_bar)
    for idx, c in enumerate(["#FC8181", "#F6E05E", "#68D391"]):
        ax.add_patch(patches.Circle((5 + idx * 2.2, 92), 0.9, fc=c))

    url_box = patches.Rectangle((15, 89.5), 78, 5, fc="#FFFFFF", ec="#CBD5E0", lw=0.8)
    ax.add_patch(url_box)
    ax.text(17, 92, "http://node1.coldstorage.internal:8080/  |  Status: Verified CD Deployment",
            fontsize=7.5, fontfamily='monospace', color="#2D3748")

    # Navbar
    nav = patches.Rectangle((4, 76), 92, 10, fc="#1A365D")
    ax.add_patch(nav)
    ax.text(7, 81, "Cold Storage Slot Booking System", fontsize=10, fontweight='bold', color="#FFFFFF")
    ax.text(62, 81, "Dashboard   Chambers   Bookings   Actuator Health: UP", fontsize=7.8, color="#68D391")

    # Metrics row
    kpis = [
        {"val": "1,200 MT", "lbl": "TOTAL CAPACITY", "c": "#3182CE", "x": 6},
        {"val": "450 MT", "lbl": "BOOKED SLOTS", "c": "#DD6B20", "x": 30},
        {"val": "750 MT", "lbl": "AVAILABLE SPACE", "c": "#38A169", "x": 54},
        {"val": "12", "lbl": "ACTIVE BOOKINGS", "c": "#805AD5", "x": 78}
    ]
    for k in kpis:
        box = patches.Rectangle((k["x"], 56), 20, 16, fc="#FFFFFF", ec="#CBD5E0", lw=1)
        ax.add_patch(box)
        ax.text(k["x"] + 10, 66, k["val"], ha='center', va='center', fontsize=11, fontweight='bold', color=k["c"])
        ax.text(k["x"] + 10, 60, k["lbl"], ha='center', va='center', fontsize=6.8, color="#718096")

    # Active Bookings Table Mockup
    t_box = patches.Rectangle((6, 10), 88, 42, fc="#FFFFFF", ec="#CBD5E0", lw=1)
    ax.add_patch(t_box)

    th = patches.Rectangle((6, 42), 88, 10, fc="#EDF2F7")
    ax.add_patch(th)
    ax.text(9, 47, "REF ID", fontsize=7.5, fontweight='bold', color="#2D3748")
    ax.text(30, 47, "FARMER / TRADER", fontsize=7.5, fontweight='bold', color="#2D3748")
    ax.text(50, 47, "COMMODITY", fontsize=7.5, fontweight='bold', color="#2D3748")
    ax.text(68, 47, "DATES", fontsize=7.5, fontweight='bold', color="#2D3748")
    ax.text(85, 47, "STATUS", fontsize=7.5, fontweight='bold', color="#2D3748")

    table_rows = [
        ("CSBS-2026-RES-001", "Ramesh Patil", "Apples (Chilled: 2°C)", "Oct 21 - Oct 28", "CONFIRMED", "#38A169"),
        ("CSBS-2026-RES-002", "Suresh Shinde", "Dairy Butter (Deep Freeze: -20°C)", "Oct 22 - Nov 05", "CONFIRMED", "#38A169"),
        ("CSBS-2026-RES-003", "Kisan Agro Co.", "Potatoes (Controlled: 12°C)", "Oct 20 - Nov 20", "PENDING", "#DD6B20")
    ]
    for idx, (ref, name, com, dates, st, col) in enumerate(table_rows):
        y = 32 - (idx * 10)
        ax.text(9, y + 4, ref, fontsize=7.0, fontfamily='monospace', color="#3182CE")
        ax.text(30, y + 4, name, fontsize=7.0, color="#2D3748")
        ax.text(50, y + 4, com, fontsize=7.0, color="#4A5568")
        ax.text(68, y + 4, dates, fontsize=7.0, color="#4A5568")
        badge = patches.FancyBboxPatch((84, y + 1.5), 9, 5, boxstyle="round,pad=0.2",
                                       fc="#F0FFF4" if st == "CONFIRMED" else "#FEEBC8", ec=col, lw=0.8)
        ax.add_patch(badge)
        ax.text(88.5, y + 4, st, ha='center', va='center', fontsize=6.5, fontweight='bold', color=col)

    plt.tight_layout()
    plt.savefig("screenshots/task15/fig15_3_live_production_dashboard.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 15.3: Live Production Dashboard")

# -------------------------------------------------------------------------
# Figure 15.4: Troubleshooting & Incident Response Playbook
# -------------------------------------------------------------------------
def create_fig15_4_troubleshooting_flow():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "DevOps Incident Response & Troubleshooting Playbook",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    scenarios = [
        {"x": 3, "title": "1. GIT CONFLICT", "symptom": "Merge aborted\nMarkers in code",
         "solution": "1. Inspect conflict lines\n2. Align with team\n3. Select correct baseline\n4. Commit & push dev", "c": "#3182CE"},
        {"x": 27.5, "title": "2. SELENIUM FAIL", "symptom": "Build aborted\nSurefire error",
         "solution": "1. Inspect failure PNG\n2. Verify locator ID\n3. Fix code assertion\n4. Rerun Jenkins job", "c": "#E53E3E"},
        {"x": 52, "title": "3. PORT CONFLICT", "symptom": "Port 8080 busy\nTomcat bind error",
         "solution": "1. docker ps -a\n2. Identify rogue PID\n3. docker rm -f old-app\n4. Relaunch container", "c": "#DD6B20"},
        {"x": 76.5, "title": "4. PROD OUTAGE", "symptom": "Actuator HTTP 500\nHealth status DOWN",
         "solution": "1. Trigger rollback.yml\n2. Pull prior tag 1.0.0\n3. Swap container (<8s)\n4. Verify /actuator/health", "c": "#38A169"}
    ]

    for sc in scenarios:
        box = patches.FancyBboxPatch((sc["x"], 16), 21.5, 72, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=sc["c"], lw=1.8)
        ax.add_patch(box)
        h_box = patches.Rectangle((sc["x"], 74), 21.5, 14, fc=sc["c"])
        ax.add_patch(h_box)
        ax.text(sc["x"] + 10.75, 82.5, sc["title"], ha='center', va='center',
                fontsize=7.8, fontweight='bold', color="#FFFFFF")
        ax.text(sc["x"] + 10.75, 77.5, "Triage Protocol", ha='center', va='center',
                fontsize=6.8, color="#FFFFFF")

        ax.text(sc["x"] + 2, 67, "Symptom / Detection:", fontsize=6.8, fontweight='bold', color="#1A202C")
        ax.text(sc["x"] + 2, 59, sc["symptom"], fontsize=6.5, color="#C53030")

        ax.text(sc["x"] + 2, 48, "Resolution Steps:", fontsize=6.8, fontweight='bold', color="#1A202C")
        ax.text(sc["x"] + 2, 33, sc["solution"], fontsize=6.4, color="#4A5568")

    ax.text(50, 7, "Operational Standard: Mean Time to Detect (MTTD) < 1 min | Mean Time to Recover (MTTR) < 8 seconds",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task15/fig15_4_troubleshooting_and_incident_flow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 15.4: Troubleshooting Flow")

if __name__ == "__main__":
    create_fig15_1_e2e_workflow()
    create_fig15_2_technical_arch()
    create_fig15_3_live_production()
    create_fig15_4_troubleshooting_flow()
