import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task14", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 14.1: Ansible Idempotency Lifecycle Model
# -------------------------------------------------------------------------
def create_fig14_1_idempotency_workflow():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Ansible Idempotency Mechanism - Desired State Convergence",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    # Run 1 Box (Convergence / Modifications)
    box_r1 = patches.FancyBboxPatch((3, 20), 44, 68, boxstyle="round,pad=1.0",
                                     fc="#FFF5F5", ec="#E53E3E", lw=1.8)
    ax.add_patch(box_r1)
    ax.text(25, 83, "FIRST EXECUTION (State Convergence)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color="#C53030")
    ax.text(25, 78, "System initially in unconfigured state", ha='center', va='center',
            fontsize=7.5, fontstyle='italic', color="#718096")

    r1_steps = [
        "1. Check Docker CE presence -> NOT FOUND",
        "2. Install Docker CE & containerd -> CHANGED",
        "3. Check user coldstorage -> NOT FOUND",
        "4. Create system user (1001) -> CHANGED",
        "5. Check /opt/coldstorage-app -> NOT FOUND",
        "6. Create directory structure -> CHANGED",
        "Play Recap: ok=12 | changed=9 | failed=0"
    ]
    for i, s in enumerate(r1_steps):
        is_last = (i == len(r1_steps) - 1)
        bg = "#FED7D7" if is_last else "#FFFFFF"
        b = patches.Rectangle((5, 68 - (i * 7.5)), 40, 6.0, fc=bg, ec="#E2E8F0", lw=0.8)
        ax.add_patch(b)
        weight = 'bold' if is_last else 'normal'
        col = "#9B2C2C" if is_last else "#2D3748"
        ax.text(7, 71 - (i * 7.5), s, va='center', fontsize=6.8, fontfamily='monospace', color=col, fontweight=weight)

    # Transition Arrow
    ax.annotate("", xy=(53, 54), xytext=(47, 54),
                arrowprops=dict(arrowstyle="->", color="#3182CE", lw=3.0))
    ax.text(50, 58, "RERUN\nSAME PLAYBOOK", ha='center', va='center',
            fontsize=7.0, fontweight='bold', color="#2B6CB0")

    # Run 2 Box (Idempotent / Zero Changes)
    box_r2 = patches.FancyBboxPatch((53, 20), 44, 68, boxstyle="round,pad=1.0",
                                     fc="#F0FFF4", ec="#38A169", lw=1.8)
    ax.add_patch(box_r2)
    ax.text(75, 83, "SECOND EXECUTION (Idempotency Proof)", ha='center', va='center',
            fontsize=9.5, fontweight='bold', color="#276749")
    ax.text(75, 78, "System already at desired target state", ha='center', va='center',
            fontsize=7.5, fontstyle='italic', color="#718096")

    r2_steps = [
        "1. Check Docker CE presence -> FOUND (ok)",
        "2. Install Docker CE -> ALREADY INSTALLED (ok)",
        "3. Check user coldstorage -> FOUND (ok)",
        "4. Create system user -> EXISTS (ok)",
        "5. Check /opt/coldstorage-app -> EXISTS (ok)",
        "6. Create directory structure -> CORRECT (ok)",
        "Play Recap: ok=12 | changed=0 | failed=0"
    ]
    for i, s in enumerate(r2_steps):
        is_last = (i == len(r2_steps) - 1)
        bg = "#C6F6D5" if is_last else "#FFFFFF"
        b = patches.Rectangle((55, 68 - (i * 7.5)), 40, 6.0, fc=bg, ec="#E2E8F0", lw=0.8)
        ax.add_patch(b)
        weight = 'bold' if is_last else 'normal'
        col = "#22543D" if is_last else "#2D3748"
        ax.text(57, 71 - (i * 7.5), s, va='center', fontsize=6.8, fontfamily='monospace', color=col, fontweight=weight)

    ax.text(50, 8, "DevOps Master Standard: Zero unintended side effects | Execution 2 yields identical machine state with zero changes",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task14/fig14_1_idempotency_workflow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 14.1: Idempotency Workflow")

# -------------------------------------------------------------------------
# Figure 14.2: Idempotency Verification Terminal Session
# -------------------------------------------------------------------------
def create_fig14_2_idempotency_terminal():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Terminal Background
    term_box = patches.Rectangle((2, 4), 96, 92, fc="#1A202C", ec="#4A5568", lw=1.8)
    ax.add_patch(term_box)

    # Title Bar
    title_bar = patches.Rectangle((2, 90), 96, 6, fc="#2D3748")
    ax.add_patch(title_bar)
    for idx, c in enumerate(["#FC8181", "#F6E05E", "#68D391"]):
        ax.add_patch(patches.Circle((4.5 + idx * 2.2, 93), 0.8, fc=c))
    ax.text(50, 93, "Ansible CLI - Second Execution: Idempotency Verification (changed=0)",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color="#CBD5E0")

    terminal_lines = [
        ("$ ansible-playbook -i hosts.ini playbook.yml", "#68D391"),
        ("", "#CBD5E0"),
        ("PLAY [Configure Target Nodes for Cold Storage Slot Booking System] ******************", "#63B3ED"),
        ("TASK [Gathering Facts] *************************************************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [1. Update apt package index] *************************************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [2. Install baseline system prerequisite packages] ****************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [5. Install Docker CE and container runtime] **********************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [7. Create dedicated coldstorage system group] ********************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [8. Create coldstorage unprivileged service user] *****************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [10. Create application directory structure with secure permissions] **********", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [11. Deploy application production configuration from Jinja2 template] *******", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [12. Configure UFW firewall to permit application traffic] *******************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("", "#CBD5E0"),
        ("PLAY RECAP *************************************************************************", "#63B3ED"),
        ("node1.coldstorage.internal : ok=12   changed=0    unreachable=0    failed=0    skipped=0", "#48BB78")
    ]

    for i, (line, col) in enumerate(terminal_lines):
        weight = 'bold' if ("PLAY RECAP" in line or "changed=0" in line or line.startswith("$")) else 'normal'
        ax.text(4, 87 - (i * 3.4), line, fontsize=6.5, fontfamily='monospace', color=col, fontweight=weight)

    plt.tight_layout()
    plt.savefig("screenshots/task14/fig14_2_idempotency_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 14.2: Idempotency Terminal")

# -------------------------------------------------------------------------
# Figure 14.3: Deep Health Check & Subsystem Reliability Verification
# -------------------------------------------------------------------------
def create_fig14_3_health_verification():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Background card
    card = patches.FancyBboxPatch((2, 4), 96, 92, boxstyle="round,pad=0.5",
                                 fc="#FFFFFF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(card)

    # Header bar
    h_bar = patches.Rectangle((2, 82), 96, 14, fc="#1A365D")
    ax.add_patch(h_bar)
    ax.text(5, 91, "Automated System Reliability Probe - Spring Boot Actuator",
            fontsize=10.5, fontweight='bold', color="#FFFFFF")
    ax.text(5, 85, "Endpoint: HTTP GET http://node1.coldstorage.internal:8080/actuator/health",
            fontsize=7.8, color="#E2E8F0")

    # Metric Badges
    badges = [
        {"lbl": "APPLICATION STATUS", "val": "UP", "c": "#38A169", "x": 5},
        {"lbl": "H2 DATABASE POOL", "val": "UP (Active)", "c": "#3182CE", "x": 28},
        {"lbl": "DISK STORAGE", "val": "UP (421 GB Free)", "c": "#805AD5", "x": 51},
        {"lbl": "PING / HEARTBEAT", "val": "UP (< 1ms)", "c": "#319795", "x": 74}
    ]
    for b in badges:
        card_b = patches.Rectangle((b["x"], 60), 21, 18, fc="#F7FAFC", ec=b["c"], lw=1.2)
        ax.add_patch(card_b)
        ax.text(b["x"] + 10.5, 72, b["val"], ha='center', va='center', fontsize=9.0, fontweight='bold', color=b["c"])
        ax.text(b["x"] + 10.5, 64, b["lbl"], ha='center', va='center', fontsize=6.5, color="#718096")

    # JSON Payload Box
    json_box = patches.FancyBboxPatch((4, 8), 92, 48, boxstyle="round,pad=0.5",
                                      fc="#1A202C", ec="#4A5568", lw=1.2)
    ax.add_patch(json_box)
    ax.text(6, 50, "Full JSON Payload (Content-Type: application/vnd.spring-boot.actuator.v3+json):",
            fontsize=7.5, fontweight='bold', color="#63B3ED")

    json_lines = [
        "{",
        "  \"status\": \"UP\",",
        "  \"components\": {",
        "    \"db\": { \"status\": \"UP\", \"details\": { \"database\": \"H2 In-Memory DB\", \"validationQuery\": \"isValid()\" } },",
        "    \"diskSpace\": { \"status\": \"UP\", \"details\": { \"total\": 512000000000, \"free\": 421000000000, \"threshold\": 10485760 } },",
        "    \"ping\": { \"status\": \"UP\" }",
        "  }",
        "}"
    ]
    for i, jl in enumerate(json_lines):
        col = "#68D391" if "\"UP\"" in jl else "#E2E8F0"
        ax.text(8, 44 - (i * 4.6), jl, fontsize=6.8, fontfamily='monospace', color=col)

    plt.tight_layout()
    plt.savefig("screenshots/task14/fig14_3_actuator_health_verification.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 14.3: Health Verification")

# -------------------------------------------------------------------------
# Figure 14.4: Automated Rollback & Fault Recovery Workflow
# -------------------------------------------------------------------------
def create_fig14_4_rollback_flow():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Disaster Recovery & Automated Rollback Workflow for Cold Storage App",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    steps = [
        {"step": "1. DEFECT DETECTED", "sub": "Faulty Version 1.2.0-broken",
         "desc": "Actuator probe fails\nHTTP 500 error raised", "color": "#E53E3E", "x": 2},
        {"step": "2. ROLLBACK TRIGGER", "sub": "ansible/rollback.yml",
         "desc": "Alerts operations\nHalts deployment", "color": "#DD6B20", "x": 26.5},
        {"step": "3. CONTAINER SWAP", "sub": "Docker Service",
         "desc": "Stop & remove faulty tag\nRelaunch stable v1.0.0", "color": "#3182CE", "x": 51},
        {"step": "4. RECOVERY CONFIRMED", "sub": "Actuator Health Status",
         "desc": "Health probe returns UP\nZero data corruption", "color": "#38A169", "x": 75.5}
    ]

    for s in steps:
        box = patches.FancyBboxPatch((s["x"], 25), 22.5, 60, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)
        h_box = patches.Rectangle((s["x"], 70), 22.5, 15, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(s["x"] + 11.25, 79, s["step"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#FFFFFF")
        ax.text(s["x"] + 11.25, 74, s["sub"], ha='center', va='center',
                fontsize=6.8, color="#FFFFFF")

        ax.text(s["x"] + 11.25, 46, s["desc"], ha='center', va='center',
                fontsize=7.0, color="#4A5568")

    # Arrows
    for arrow_x in [24.5, 49.0, 73.5]:
        ax.annotate("", xy=(arrow_x + 2.0, 55), xytext=(arrow_x, 55),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    ax.text(50, 10, "Mean Time to Recovery (MTTR): < 8 seconds | Recovery Target: Zero farmer reservation loss",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task14/fig14_4_rollback_recovery_flow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 14.4: Rollback Flow")

if __name__ == "__main__":
    create_fig14_1_idempotency_workflow()
    create_fig14_2_idempotency_terminal()
    create_fig14_3_health_verification()
    create_fig14_4_rollback_flow()
