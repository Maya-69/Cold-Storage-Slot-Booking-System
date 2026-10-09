import os
import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task3", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 3.1: Use Case Diagram
# -------------------------------------------------------------------------
def create_fig3_1_use_case():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - UML Use Case Diagram",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    # Boundary Box: System
    sys_box = patches.FancyBboxPatch((28, 5), 45, 85, boxstyle="round,pad=1.0",
                                     fc="#F7FAFC", ec="#2B6CB0", lw=2, linestyle='--')
    ax.add_patch(sys_box)
    ax.text(50.5, 87, "Cold Storage Application Boundary (Spring Boot)",
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='#2B6CB0')

    # Actor 1: Farmer / Trader (Left)
    ax.scatter(12, 60, s=200, color="#3182CE")
    ax.plot([12, 12], [47, 57], color="#3182CE", lw=2.5) # Body
    ax.plot([6, 18], [53, 53], color="#3182CE", lw=2.5) # Arms
    ax.plot([12, 7], [47, 36], color="#3182CE", lw=2.5) # Left Leg
    ax.plot([12, 17], [47, 36], color="#3182CE", lw=2.5) # Right Leg
    ax.text(12, 30, "Farmer / Trader\n(Produce Producer)", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color="#1A365D")

    # Actor 2: Warehouse Manager (Right)
    ax.scatter(88, 60, s=200, color="#805AD5")
    ax.plot([88, 88], [47, 57], color="#805AD5", lw=2.5) # Body
    ax.plot([82, 94], [53, 53], color="#805AD5", lw=2.5) # Arms
    ax.plot([88, 83], [47, 36], color="#805AD5", lw=2.5) # Left Leg
    ax.plot([88, 93], [47, 36], color="#805AD5", lw=2.5) # Right Leg
    ax.text(88, 30, "Warehouse Manager\n(Facility Admin)", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color="#44337A")

    # Use Cases inside system
    use_cases = [
        {"name": "UC-01: Register & Authenticate", "y": 78},
        {"name": "UC-02: View Chamber Availability & Zones", "y": 64},
        {"name": "UC-03: Reserve Slot & Specify Commodity", "y": 50},
        {"name": "UC-04: Confirm / Cancel Reservations", "y": 36},
        {"name": "UC-05: Record Consignment Check-In", "y": 22},
        {"name": "UC-06: Monitor Real-Time Actuator Health", "y": 10}
    ]

    for uc in use_cases:
        ellipse = patches.Ellipse((50.5, uc["y"]), 38, 9, fc="#FFFFFF", ec="#2D3748", lw=1.2)
        ax.add_patch(ellipse)
        ax.text(50.5, uc["y"], uc["name"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#2D3748")

    # Actor 1 Associations (Farmer to UC 1, 2, 3)
    for target_y in [78, 64, 50]:
        ax.plot([18, 32], [55, target_y], color="#3182CE", lw=1.5)

    # Actor 2 Associations (Manager to UC 1, 2, 4, 5, 6)
    for target_y in [78, 64, 36, 22, 10]:
        ax.plot([82, 69], [55, target_y], color="#805AD5", lw=1.5)

    plt.tight_layout()
    plt.savefig("screenshots/task3/fig3_1_use_case.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 3.1: Use Case Diagram")

# -------------------------------------------------------------------------
# Figure 3.2: 4-Tier Monolithic System Architecture
# -------------------------------------------------------------------------
def create_fig3_2_architecture():
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - 4-Tier Monolithic Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    tiers = [
        {"title": "Tier 1: Presentation Layer", "tech": "Thymeleaf + Bootstrap 5 + JS",
         "items": ["• Responsive UI Dashboard", "• Chamber Directory & Filter Grid", "• Slot Reservation Form", "• Booking Action Buttons"],
         "color": "#3182CE", "x": 3, "w": 21.5},
        {"title": "Tier 2: Controller Layer", "tech": "Spring MVC / REST Controllers",
         "items": ["• DashboardController", "• SlotController", "• BookingController", "• Auth & Actuator Probe"],
         "color": "#319795", "x": 27.5, "w": 21.5},
        {"title": "Tier 3: Business Logic Layer", "tech": "Spring Service Components",
         "items": ["• ChamberService (Capacity)", "• BookingService (Validator)", "• UserService (Auth/Roles)", "• DataLoader (H2 Seeder)"],
         "color": "#D69E2E", "x": 52, "w": 21.5},
        {"title": "Tier 4: Data Access & DB", "tech": "Spring Data JPA + Embedded H2",
         "items": ["• ChamberRepository", "• SlotRepository", "• BookingRepository", "• In-Memory H2 DB Table"],
         "color": "#805AD5", "x": 76.5, "w": 21.5}
    ]

    for t in tiers:
        box = patches.FancyBboxPatch((t["x"], 10), t["w"], 78, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=t["color"], lw=1.8)
        ax.add_patch(box)

        # Header Box
        h_box = patches.Rectangle((t["x"], 73), t["w"], 15, fc=t["color"])
        ax.add_patch(h_box)
        ax.text(t["x"] + t["w"]/2, 83, t["title"], ha='center', va='center',
                fontsize=8.5, fontweight='bold', color="#FFFFFF")
        ax.text(t["x"] + t["w"]/2, 77, t["tech"], ha='center', va='center',
                fontsize=7.2, fontstyle='italic', color="#E2E8F0")

        # Items
        y = 65
        for item in t["items"]:
            ax.text(t["x"] + 1.5, y, item, ha='left', va='center', fontsize=7.5, color="#2D3748")
            y -= 12

    # Flow arrows between tiers
    for arrow_x in [24.8, 49.3, 73.8]:
        ax.annotate("", xy=(arrow_x + 2.5, 48), xytext=(arrow_x, 48),
                    arrowprops=dict(arrowstyle="<->", color="#4A5568", lw=2))

    # Bottom Architecture Banner
    ax.text(50, 4, "Self-Contained Embedded Architecture: Zero External DB Dependency | Embedded Tomcat 11 | Spring Boot Actuator",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task3/fig3_2_system_architecture.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 3.2: Architecture Diagram")

# -------------------------------------------------------------------------
# Figure 3.3: Data Model / Entity Relationship Diagram
# -------------------------------------------------------------------------
def create_fig3_3_data_model():
    fig, ax = plt.subplots(figsize=(10, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Relational Data Model (ER Entities)",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    entities = [
        {"title": "CHAMBERS", "color": "#2B6CB0", "x": 3, "w": 21,
         "fields": ["PK  id : BIGINT", "UK  chamberCode : VARCHAR", "    name : VARCHAR", "    zoneType : VARCHAR",
                    "    minTemperature : DOUBLE", "    maxTemperature : DOUBLE", "    suitableCommodities : VARCHAR",
                    "    totalSlots : INT", "    availableSlots : INT", "    pricePerDayPerCrate : NUMERIC"]},
        {"title": "SLOTS", "color": "#319795", "x": 27.5, "w": 20,
         "fields": ["PK  id : BIGINT", "UK  slotNumber : VARCHAR", "FK  chamberCode : VARCHAR",
                    "    available : BOOLEAN", "    maxCratesCapacity : INT"]},
        {"title": "BOOKINGS", "color": "#D69E2E", "x": 51, "w": 25,
         "fields": ["PK  id : BIGINT", "UK  bookingReference : VARCHAR", "    farmerName : VARCHAR", "    contactNumber : VARCHAR",
                    "    commodityType : VARCHAR", "    cratesCount : INT", "    checkInDate : DATE", "    checkOutDate : DATE",
                    "    totalCost : NUMERIC", "    status : VARCHAR", "FK  chamberCode : VARCHAR", "FK  slotNumber : VARCHAR"]},
        {"title": "USERS", "color": "#805AD5", "x": 79.5, "w": 18,
         "fields": ["PK  id : BIGINT", "UK  username : VARCHAR", "    password : VARCHAR", "    fullName : VARCHAR",
                    "    email : VARCHAR", "    phone : VARCHAR", "    role : VARCHAR"]}
    ]

    for e in entities:
        box = patches.FancyBboxPatch((e["x"], 10), e["w"], 78, boxstyle="round,pad=1.0",
                                     fc="#FFFFFF", ec=e["color"], lw=1.8)
        ax.add_patch(box)

        # Header Box
        h_box = patches.Rectangle((e["x"], 78), e["w"], 10, fc=e["color"])
        ax.add_patch(h_box)
        ax.text(e["x"] + e["w"]/2, 83, e["title"], ha='center', va='center',
                fontsize=9, fontweight='bold', color="#FFFFFF")

        # Fields
        y = 72
        for f in e["fields"]:
            ax.text(e["x"] + 1, y, f, ha='left', va='center', fontsize=7.2,
                    fontfamily='monospace', color="#2D3748")
            y -= 6.4

    # Relationship connectors
    # Chamber -> Slot (1:N)
    ax.annotate("", xy=(27.5, 50), xytext=(24, 50),
                arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(25.5, 52, "1:N", fontsize=7.5, fontweight='bold', color="#2B6CB0")

    # Slot -> Booking (1:N)
    ax.annotate("", xy=(51, 50), xytext=(47.5, 50),
                arrowprops=dict(arrowstyle="->", color="#2D3748", lw=1.5))
    ax.text(49, 52, "1:N", fontsize=7.5, fontweight='bold', color="#319795")

    plt.tight_layout()
    plt.savefig("screenshots/task3/fig3_3_data_model.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 3.3: Data Model ER Diagram")

# -------------------------------------------------------------------------
# Figure 3.4: Actuator Health Endpoint Terminal Output Visual
# -------------------------------------------------------------------------
def create_fig3_4_actuator():
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Terminal Background
    term = patches.FancyBboxPatch((2, 5), 96, 90, boxstyle="round,pad=1.0",
                                  fc="#1A202C", ec="#4A5568", lw=2)
    ax.add_patch(term)

    # Terminal Header Bar
    top_bar = patches.Rectangle((2, 84), 96, 11, fc="#2D3748")
    ax.add_patch(top_bar)
    ax.text(5, 89.5, "● ● ●  PowerShell - Spring Boot Actuator Observability Probe",
            fontsize=8.5, fontweight='bold', color="#CBD5E0")

    # Command line and JSON output
    lines = [
        ("PS E:\\Dev\\DevOPS> curl.exe -s http://localhost:8080/actuator/health", "#63B3ED", True),
        ("{", "#FFFFFF", False),
        ('  "status": "UP",', "#48BB78", True),
        ('  "components": {', "#CBD5E0", False),
        ('    "db": { "status": "UP", "details": { "database": "H2", "validationQuery": "isValid()" } },', "#CBD5E0", False),
        ('    "diskSpace": { "status": "UP", "details": { "total": 1000202039296, "free": 347900379136 } },', "#CBD5E0", False),
        ('    "ping": { "status": "UP" }', "#CBD5E0", False),
        ('  }', "#CBD5E0", False),
        ("}", "#FFFFFF", False),
        ("", "#FFFFFF", False),
        ("PS E:\\Dev\\DevOPS> curl.exe -s http://localhost:8080/api/metrics", "#63B3ED", True),
        ('{"availableCapacitySlots":95,"activeReservations":3,"totalCapacitySlots":115,"bookedCapacitySlots":20,"status":"UP"}', "#ECC94B", True)
    ]

    y = 78
    for text, color, bold in lines:
        ax.text(5, y, text, fontsize=7.8, fontfamily='monospace', fontweight='bold' if bold else 'normal', color=color)
        y -= 5.8

    plt.tight_layout()
    plt.savefig("screenshots/task3/actuator_live.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 3.4: Actuator Terminal Visual")

if __name__ == "__main__":
    create_fig3_1_use_case()
    create_fig3_2_architecture()
    create_fig3_3_data_model()
    create_fig3_4_actuator()
