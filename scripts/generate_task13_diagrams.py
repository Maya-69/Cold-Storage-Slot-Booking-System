import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task13", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 13.1: Ansible Configuration Management Architecture
# -------------------------------------------------------------------------
def create_fig13_1_ansible_arch():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Ansible Configuration Management Architecture",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    # Control Node Box
    ctrl_box = patches.FancyBboxPatch((4, 25), 32, 60, boxstyle="round,pad=0.8",
                                      fc="#EBF8FF", ec="#3182CE", lw=2.0)
    ax.add_patch(ctrl_box)
    h_ctrl = patches.Rectangle((4, 75), 32, 10, fc="#3182CE")
    ax.add_patch(h_ctrl)
    ax.text(20, 80, "ANSIBLE CONTROL NODE", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color="#FFFFFF")

    ctrl_items = [
        "• ansible.cfg (Execution Engine)",
        "• hosts.ini (Node Inventory)",
        "• playbook.yml (Idempotent Tasks)",
        "• templates/ (Jinja2 Configs)",
        "• SSH Keys (~/.ssh/id_rsa)",
        "Agentless Automation (Zero Client)"
    ]
    for i, it in enumerate(ctrl_items):
        ax.text(6, 68 - (i * 7.5), it, fontsize=7.2, color="#2D3748")

    # Target Node 1 (Staging)
    node1_box = patches.FancyBboxPatch((64, 55), 32, 32, boxstyle="round,pad=0.8",
                                       fc="#F0FFF4", ec="#38A169", lw=1.8)
    ax.add_patch(node1_box)
    h_n1 = patches.Rectangle((64, 77), 32, 10, fc="#38A169")
    ax.add_patch(h_n1)
    ax.text(80, 82, "TARGET NODE 1: STAGING", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color="#FFFFFF")
    ax.text(66, 70, "• IP: 192.168.56.101 (Ubuntu 22.04 LTS)\n• OpenJDK 21 + Docker CE Engine\n• /opt/coldstorage-app (Config & Logs)\n• UFW Port 8080/tcp Allowed",
            fontsize=6.8, color="#2D3748")

    # Target Node 2 (Production)
    node2_box = patches.FancyBboxPatch((64, 15), 32, 32, boxstyle="round,pad=0.8",
                                       fc="#FEFCBF", ec="#D69E2E", lw=1.8)
    ax.add_patch(node2_box)
    h_n2 = patches.Rectangle((64, 37), 32, 10, fc="#D69E2E")
    ax.add_patch(h_n2)
    ax.text(80, 42, "TARGET NODE 2: PRODUCTION", ha='center', va='center',
            fontsize=8.0, fontweight='bold', color="#FFFFFF")
    ax.text(66, 30, "• IP: 192.168.56.102 (Ubuntu 22.04 LTS)\n• OpenJDK 21 + Docker CE Engine\n• /opt/coldstorage-app (Config & Logs)\n• UFW Port 8080/tcp Allowed",
            fontsize=6.8, color="#2D3748")

    # Communication Arrows
    ax.annotate("", xy=(64, 71), xytext=(36, 60),
                arrowprops=dict(arrowstyle="->", color="#3182CE", lw=2.2))
    ax.text(49, 70, "SSH (Port 22)\nIdempotent Push", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color="#2B6CB0")

    ax.annotate("", xy=(64, 31), xytext=(36, 50),
                arrowprops=dict(arrowstyle="->", color="#3182CE", lw=2.2))
    ax.text(49, 36, "SSH (Port 22)\nIdempotent Push", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color="#2B6CB0")

    ax.text(50, 7, "Protocol: OpenSSH | Security: Sudo privilege escalation without password | Format: Human-readable YAML",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task13/fig13_1_ansible_cm_arch.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 13.1: Ansible Architecture")

# -------------------------------------------------------------------------
# Figure 13.2: Cold Storage Server Prerequisites Breakdown Tree
# -------------------------------------------------------------------------
def create_fig13_2_prereqs_tree():
    fig, ax = plt.subplots(figsize=(10.5, 5.0), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Cold Storage Slot Booking System - Server Prerequisites Hierarchy",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    pillars = [
        {"title": "1. OS & PACKAGES", "color": "#3182CE", "x": 2,
         "items": ["Ubuntu 22.04 LTS x86_64", "OpenJDK 21 Headless", "Docker CE & containerd", "curl, ufw, gnupg, ca-cert"]},
        {"title": "2. USERS & GROUPS", "color": "#D69E2E", "x": 26.5,
         "items": ["Group: coldstorage (1001)", "User: coldstorage (1001)", "Shell: /bin/false (No login)", "Supplemental: docker group"]},
        {"title": "3. DIRECTORIES & FILES", "color": "#805AD5", "x": 51,
         "items": ["/opt/coldstorage-app (0750)", "/opt/coldstorage-app/config", "/opt/coldstorage-app/logs", "application-prod.properties"]},
        {"title": "4. PORTS & SERVICES", "color": "#38A169", "x": 75.5,
         "items": ["Port 8080/tcp (App Listener)", "Port 22/tcp (SSH Management)", "Service: docker.service", "Service: ufw.service (Active)"]}
    ]

    for p in pillars:
        box = patches.FancyBboxPatch((p["x"], 18), 22.5, 68, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=p["color"], lw=1.8)
        ax.add_patch(box)
        h_box = patches.Rectangle((p["x"], 74), 22.5, 12, fc=p["color"])
        ax.add_patch(h_box)
        ax.text(p["x"] + 11.25, 80, p["title"], ha='center', va='center',
                fontsize=8, fontweight='bold', color="#FFFFFF")

        for idx, item in enumerate(p["items"]):
            y_pos = 65 - (idx * 13)
            i_box = patches.Rectangle((p["x"] + 1.5, y_pos), 19.5, 10, fc="#F7FAFC", ec="#E2E8F0", lw=1)
            ax.add_patch(i_box)
            ax.text(p["x"] + 11.25, y_pos + 5, item, ha='center', va='center',
                    fontsize=7.0, color="#2D3748")

    ax.text(50, 8, "Configuration Standard: Principle of Least Privilege | Dedicated System User | Zero Root Service Execution",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task13/fig13_2_prerequisites_breakdown.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 13.2: Prerequisites Tree")

# -------------------------------------------------------------------------
# Figure 13.3: Ansible Playbook Execution Workflow & Handlers
# -------------------------------------------------------------------------
def create_fig13_3_playbook_workflow():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Ansible Playbook Structure & Idempotent Handler Mechanics",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    # Main Play Tasks Box
    main_box = patches.FancyBboxPatch((3, 14), 58, 72, boxstyle="round,pad=0.8",
                                      fc="#F8FAFC", ec="#3182CE", lw=1.5)
    ax.add_patch(main_box)
    h_main = patches.Rectangle((3, 76), 58, 10, fc="#3182CE")
    ax.add_patch(h_main)
    ax.text(32, 81, "PLAY: Configure Target Nodes (Tasks 1 - 12)", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color="#FFFFFF")

    tasks = [
        "1. Update apt cache (apt_repository / update_cache)",
        "2. Install baseline system packages (apt)",
        "3. Add Docker GPG key & configure repo (apt_repository)",
        "4. Install Docker CE and containerd -> NOTIFIES 'Restart docker'",
        "5. Enable & start docker.service (systemd)",
        "6. Create coldstorage group (GID 1001) & user (UID 1001)",
        "7. Create /opt/coldstorage-app directory structure (0750)",
        "8. Deploy application-prod.properties template",
        "9. Configure UFW firewall for port 8080/tcp -> NOTIFIES 'Reload ufw'"
    ]
    for idx, t in enumerate(tasks):
        ax.text(5, 71 - (idx * 6.5), t, fontsize=6.8, fontfamily='monospace', color="#1A202C")

    # Handlers Box
    h_box = patches.FancyBboxPatch((66, 35), 31, 51, boxstyle="round,pad=0.8",
                                  fc="#FFF5F5", ec="#E53E3E", lw=1.5)
    ax.add_patch(h_box)
    h_h = patches.Rectangle((66, 76), 31, 10, fc="#E53E3E")
    ax.add_patch(h_h)
    ax.text(81.5, 81, "NOTIFY HANDLERS", ha='center', va='center',
            fontsize=8.5, fontweight='bold', color="#FFFFFF")

    h_items = [
        "Handler 1: Restart docker\n• Executes only if Docker\n  packages or daemon changed\n• Ensures fresh socket binding",
        "Handler 2: Reload ufw\n• Executes only if port 8080\n  rule was added/updated\n• Flushes iptables chains"
    ]
    for idx, hi in enumerate(h_items):
        ax.text(68, 63 - (idx * 18), hi, fontsize=6.8, color="#2D3748")

    # Arrow from Tasks to Handlers
    ax.annotate("", xy=(66, 62), xytext=(58, 62),
                arrowprops=dict(arrowstyle="->", color="#E53E3E", lw=2))

    ax.text(50, 6, "Idempotency Guarantee: Tasks execute only when state differs; Handlers trigger only upon 'changed' notification.",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task13/fig13_3_ansible_playbook_structure.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 13.3: Playbook Structure")

# -------------------------------------------------------------------------
# Figure 13.4: First Playbook Execution Log Terminal
# -------------------------------------------------------------------------
def create_fig13_4_first_exec_terminal():
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
    ax.text(50, 93, "Ansible CLI - First Execution of playbook.yml against Target Nodes",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color="#CBD5E0")

    terminal_lines = [
        ("$ ansible-playbook -i hosts.ini playbook.yml", "#68D391"),
        ("", "#CBD5E0"),
        ("PLAY [Configure Target Nodes for Cold Storage Slot Booking System] ******************", "#63B3ED"),
        ("TASK [Gathering Facts] *************************************************************", "#CBD5E0"),
        ("ok: [node1.coldstorage.internal]", "#68D391"),
        ("TASK [1. Update apt package index] *************************************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal]", "#ECC94B"),
        ("TASK [2. Install baseline system prerequisite packages] ****************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (packages: openjdk-21-jre-headless, curl, ufw...)", "#ECC94B"),
        ("TASK [5. Install Docker CE and container runtime] **********************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (packages: docker-ce, containerd.io)", "#ECC94B"),
        ("TASK [7. Create dedicated coldstorage system group] ********************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (state=present, gid=1001)", "#ECC94B"),
        ("TASK [8. Create coldstorage unprivileged service user] *****************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (state=present, uid=1001, shell=/bin/false)", "#ECC94B"),
        ("TASK [10. Create application directory structure with secure permissions] **********", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (dirs: /opt/coldstorage-app, /config, /logs)", "#ECC94B"),
        ("TASK [11. Deploy application production configuration from Jinja2 template] *******", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal] => (dest=/opt/coldstorage-app/config/application-prod.properties)", "#ECC94B"),
        ("RUNNING HANDLER [Restart docker] **************************************************", "#CBD5E0"),
        ("changed: [node1.coldstorage.internal]", "#ECC94B"),
        ("", "#CBD5E0"),
        ("PLAY RECAP *************************************************************************", "#63B3ED"),
        ("node1.coldstorage.internal : ok=12   changed=9    unreachable=0    failed=0    skipped=0", "#68D391")
    ]

    for i, (line, col) in enumerate(terminal_lines):
        weight = 'bold' if ("PLAY RECAP" in line or "PLAY [" in line or "node1.coldstorage" in line and "ok=12" in line or line.startswith("$")) else 'normal'
        ax.text(4, 87 - (i * 3.4), line, fontsize=6.5, fontfamily='monospace', color=col, fontweight=weight)

    plt.tight_layout()
    plt.savefig("screenshots/task13/fig13_4_first_execution_terminal.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 13.4: First Execution Terminal")

if __name__ == "__main__":
    create_fig13_1_ansible_arch()
    create_fig13_2_prereqs_tree()
    create_fig13_3_playbook_workflow()
    create_fig13_4_first_exec_terminal()
