import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task1", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 1.1: Cold Storage Slot Booking Workflow & Physical Facility Topology
# -------------------------------------------------------------------------
def create_fig1():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # Title Banner
    ax.text(50, 95, "Cold Storage Slot Booking System (CSBS) - Logistics & Storage Flow",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    # Step 1: User / Producer
    box_user = patches.FancyBboxPatch((3, 50), 20, 32, boxstyle="round,pad=1.5",
                                      fc="#EBF8FF", ec="#3182CE", lw=1.5)
    ax.add_patch(box_user)
    ax.text(13, 76, "Agricultural Producer\n& Commercial Trader", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color="#2B6CB0")
    ax.text(13, 62, "• Farmers (Vegetables/Fruits)\n• Dairy & Poultry Suppliers\n• Meat & Seafood Exporters\n• Cold Logistics Brokers",
            ha='center', va='center', fontsize=8, color="#2D3748")

    # Arrow 1
    ax.annotate("", xy=(30, 66), xytext=(24, 66),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2))
    ax.text(27, 70, "Slot Search\n& Booking", ha='center', va='bottom', fontsize=7.5, fontweight='bold', color="#2B6CB0")

    # Step 2: Digital Booking System (Core Application)
    box_core = patches.FancyBboxPatch((31, 35), 32, 52, boxstyle="round,pad=1.5",
                                      fc="#F0FFF4", ec="#38A169", lw=1.8)
    ax.add_patch(box_core)
    ax.text(47, 81, "Cold Storage Booking Platform\n(Spring Boot & Thymeleaf)", ha='center', va='center',
            fontsize=10, fontweight='bold', color="#22543D")
    
    modules = [
        "1. Farmer / Trader Authentication",
        "2. Temperature Zone Directory",
        "3. Live Slot Grid & Reservation Engine",
        "4. Crate & Weight Validation Guard",
        "5. Booking Status Transition (PENDING -> CONFIRMED)",
        "6. Actuator Real-Time Metrics & Health Probe"
    ]
    y_pos = 71
    for mod in modules:
        ax.text(33, y_pos, mod, ha='left', va='center', fontsize=7.8, color="#2D3748")
        y_pos -= 6.5

    # Arrow 2
    ax.annotate("", xy=(70, 66), xytext=(64, 66),
                arrowprops=dict(arrowstyle="->", color="#38A169", lw=2))
    ax.text(67, 70, "Chamber\nAllocation", ha='center', va='bottom', fontsize=7.5, fontweight='bold', color="#22543D")

    # Step 3: Physical Cold Storage Facility
    box_fac = patches.FancyBboxPatch((71, 15), 26, 72, boxstyle="round,pad=1.5",
                                     fc="#FFF5F5", ec="#E53E3E", lw=1.5)
    ax.add_patch(box_fac)
    ax.text(84, 82, "Physical Cold Facility\n(Smart Warehouse)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color="#9B2C2C")

    # Chamber 1: Deep Freeze
    c1 = patches.Rectangle((73, 58), 22, 18, fc="#E2E8F0", ec="#4A5568", lw=1)
    ax.add_patch(c1)
    ax.text(84, 71, "Chamber A: Deep Freeze", ha='center', va='center', fontsize=8, fontweight='bold', color="#1A202C")
    ax.text(84, 63, "-18°C to -25°C\nSeafood, Frozen Meat, Butter", ha='center', va='center', fontsize=7, color="#4A5568")

    # Chamber 2: Chilled
    c2 = patches.Rectangle((73, 36), 22, 18, fc="#EDF2F7", ec="#4A5568", lw=1)
    ax.add_patch(c2)
    ax.text(84, 49, "Chamber B: Chilled Zone", ha='center', va='center', fontsize=8, fontweight='bold', color="#1A202C")
    ax.text(84, 41, "0°C to 4°C\nDairy, Fresh Milk, Apples, Berries", ha='center', va='center', fontsize=7, color="#4A5568")

    # Chamber 3: CA
    c3 = patches.Rectangle((73, 18), 22, 15, fc="#F7FAFC", ec="#4A5568", lw=1)
    ax.add_patch(c3)
    ax.text(84, 28, "Chamber C: Controlled Atm.", ha='center', va='center', fontsize=8, fontweight='bold', color="#1A202C")
    ax.text(84, 22, "10°C to 15°C | Onions, Potatoes", ha='center', va='center', fontsize=7, color="#4A5568")

    # Bottom Footer
    ax.text(50, 6, "Key Benefit: 0% Produce Spoilage, 100% Deterministic Reservation & Capacity Utilization",
            ha='center', va='center', fontsize=8.5, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task1/fig1_cold_storage_workflow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 1.1")

# -------------------------------------------------------------------------
# Figure 1.2: Multi-Stakeholder Value Proposition & Responsibilities
# -------------------------------------------------------------------------
def create_fig2():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Cold Storage Slot Booking System - Stakeholder Value Matrix",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    stakeholders = [
        {"name": "Farmers & Growers", "color_bg": "#FEFCBF", "color_bdr": "#D69E2E", "x": 3,
         "pain": "High post-harvest loss (25-35%); no advance slot visibility.",
         "value": "Guaranteed chamber reservation before harvest; transparent pricing."},
        {"name": "Warehouse Operators", "color_bg": "#E9D8FD", "color_bdr": "#805AD5", "x": 27.5,
         "pain": "Manual register tracking; empty slots and erratic overbooking.",
         "value": "Automated capacity planning, multi-temperature chamber tracking."},
        {"name": "Logistics & Fleet", "color_bg": "#BEE3F8", "color_bdr": "#3182CE", "x": 52,
         "pain": "Long truck idling at gate; turnaround delays of 8-12 hours.",
         "value": "Pre-scheduled check-in windows, rapid dock intake verification."},
        {"name": "Quality Evaluators", "color_bg": "#C6F6D5", "color_bdr": "#38A169", "x": 76.5,
         "pain": "Zero temperature compliance audit trail; spoiled commodity disputes.",
         "value": "Digital chamber logs, timestamped check-in/out records."}
    ]

    for s in stakeholders:
        box = patches.FancyBboxPatch((s["x"], 12), 21.5, 76, boxstyle="round,pad=1.2",
                                     fc=s["color_bg"], ec=s["color_bdr"], lw=1.5)
        ax.add_patch(box)
        ax.text(s["x"] + 10.75, 82, s["name"], ha='center', va='center',
                fontsize=9.5, fontweight='bold', color="#1A202C")
        
        # Pain Points Section
        ax.text(s["x"] + 2, 72, "Current Pain Points:", ha='left', va='center',
                fontsize=8, fontweight='bold', color="#C53030")
        ax.text(s["x"] + 2, 58, s["pain"], ha='left', va='top',
                fontsize=7.5, color="#2D3748", wrap=True)
        
        # Value Proposition Section
        ax.text(s["x"] + 2, 42, "CSBS Solution:", ha='left', va='center',
                fontsize=8, fontweight='bold', color="#276749")
        ax.text(s["x"] + 2, 28, s["value"], ha='left', va='top',
                fontsize=7.5, color="#2D3748", wrap=True)

    plt.tight_layout()
    plt.savefig("screenshots/task1/fig2_stakeholder_matrix.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 1.2")

# -------------------------------------------------------------------------
# Figure 1.3: 15-Task DevOps Laboratory Roadmap
# -------------------------------------------------------------------------
def create_fig3():
    fig, ax = plt.subplots(figsize=(10, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "DevOps Laboratory Project - 15-Task End-to-End Progression Roadmap",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    phases = [
        {"title": "Phase 1: Planning & Architecture", "tasks": "Tasks 1 - 3", "color": "#3182CE", "x": 2, "w": 21,
         "details": ["• Problem & MVP Scope", "• Agile Backlog & DoD", "• Spring Boot Architecture"]},
        {"title": "Phase 2: Git Version Control", "tasks": "Tasks 4 - 6", "color": "#DD6B20", "x": 26, "w": 21,
         "details": ["• GitHub Repo & Policies", "• Feature Branch & PRs", "• Conflict Resolution & v1.0"]},
        {"title": "Phase 3: CI/CD & Testing", "tasks": "Tasks 7 - 10", "color": "#38A169", "x": 50, "w": 23,
         "details": ["• Jenkins Job & Pipeline", "• Tomcat/App Deployment", "• Selenium Test Suite", "• Quality Gate Defect Stop"]},
        {"title": "Phase 4: Docker & Ansible", "tasks": "Tasks 11 - 15", "color": "#805AD5", "x": 75, "w": 23,
         "details": ["• Dockerfile & Lifecycle", "• Continuous Deployment", "• Ansible Playbook Config", "• Idempotency & Rollback", "• Final Release & Viva"]}
    ]

    for p in phases:
        box = patches.FancyBboxPatch((p["x"], 14), p["w"], 72, boxstyle="round,pad=1.2",
                                     fc="#FFFFFF", ec=p["color"], lw=1.8)
        ax.add_patch(box)
        
        # Header Box
        header_box = patches.Rectangle((p["x"], 74), p["w"], 12, fc=p["color"])
        ax.add_patch(header_box)
        ax.text(p["x"] + p["w"]/2, 82, p["title"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")
        ax.text(p["x"] + p["w"]/2, 76, p["tasks"], ha='center', va='center',
                fontsize=7.5, fontstyle='italic', color="#E2E8F0")

        # Items
        y = 66
        for d in p["details"]:
            ax.text(p["x"] + 1.5, y, d, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 11

    # Progression arrows between phases
    for arrow_x in [23.5, 47.5, 73.5]:
        ax.annotate("", xy=(arrow_x + 2, 50), xytext=(arrow_x - 0.5, 50),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    plt.tight_layout()
    plt.savefig("screenshots/task1/fig3_devops_roadmap.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 1.3")

if __name__ == "__main__":
    create_fig1()
    create_fig2()
    create_fig3()
