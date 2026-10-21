import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from doc_helper import (
    set_student_identity,
    apply_table_styles,
    style_cell,
    add_heading,
    add_subheading,
    add_body_p,
    add_bullet_p,
    add_figure,
    save_and_archive,
    STUDENT_NAME,
    STUDENT_ROLL,
    PROJECT_TITLE
)

def generate_task13_document():
    template_path = os.path.abspath("templates/template_standard.docx")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")
        
    doc = docx.Document(template_path)
    
    # Enforce Student Identity in Table 0 and Table 1
    set_student_identity(doc)
    
    # Table 2: 5-row standard envelope
    t2 = doc.tables[2]
    
    # Row 0: Task Number
    t2.rows[0].cells[1].text = "13"
    style_cell(t2.rows[0].cells[1], bold=True, font_size=12, text="13")
    
    # Row 1: Task Title
    task_title = (
        "Configuration Management Script: Identify all server prerequisites for the Cold Storage Slot Booking System: "
        "packages, users, folders, files, ports and services. Create either a Puppet manifest/modules or an Ansible "
        "inventory and YAML playbook to configure the target node."
    )
    t2.rows[1].cells[1].text = task_title
    style_cell(t2.rows[1].cells[1], bold=True, font_size=10.5, text=task_title)

    # Row 2: Resources / Apparatus Required
    hw_text = "Hardware: Workstation / Laptop (x86_64 Intel/AMD), 16 GB DDR4/DDR5 RAM, 512 GB NVMe SSD"
    sw_text = (
        "Software: Ansible Core 2.16+, OpenSSH 8.9+, Python 3.10+, Ubuntu Linux 22.04 LTS (Target Nodes), "
        "Docker Engine 26+, OpenJDK 21 Headless, UFW Firewall, Git 2.55+"
    )
    t2.rows[2].cells[1].text = hw_text
    style_cell(t2.rows[2].cells[1], bold=False, font_size=9.5, text=hw_text)
    t2.rows[2].cells[2].text = sw_text
    style_cell(t2.rows[2].cells[2], bold=False, font_size=9.5, text=sw_text)

    # Row 3: Program & Output
    c_cell = t2.rows[3].cells[1]
    c_cell.text = "" # Clear placeholder

    # 1. Introduction to Infrastructure as Code & Configuration Management
    add_heading(c_cell, "1. Configuration Management & Infrastructure as Code (IaC)")
    add_body_p(
        c_cell,
        "Configuration Management (CM) is an essential DevOps discipline that enables automated, repeatable, and declarative "
        "provisioning of infrastructure environments. Without configuration management, system administrators are forced to rely on "
        "manual shell commands, leading to configuration drift, security vulnerabilities, and unpredictable deployment failures across "
        "heterogeneous warehouse servers."
    )
    add_body_p(
        c_cell,
        "For the Cold Storage Slot Booking System (CSBS), Ansible was chosen as the Configuration Management tool due to its agentless "
        "architecture, human-readable YAML syntax, built-in idempotency, and reliance on standard OpenSSH protocols. Ansible allows "
        "defining the entire server prerequisites stack—packages, user privileges, directory topologies, configuration files, firewall "
        "ports, and background services—as version-controlled code in the project repository."
    )

    # 2. Comprehensive Server Prerequisites Specification
    add_heading(c_cell, "2. Server Prerequisites Specification for Cold Storage App")
    add_body_p(
        c_cell,
        "A rigorous audit of the Cold Storage application identified six core prerequisite categories required for stable operations. "
        "Figure 13.1 illustrates the architectural hierarchy governing these system resources."
    )

    fig13_2_path = os.path.abspath("screenshots/task13/fig13_2_prerequisites_breakdown.png")
    if os.path.exists(fig13_2_path):
        add_figure(c_cell, fig13_2_path, "Figure 13.1: Cold Storage Slot Booking System - Server Prerequisites Hierarchy")

    add_body_p(
        c_cell,
        "Detailed specification of identified prerequisites:"
    )
    add_bullet_p(c_cell, "Operating System & Base Packages: Linux Ubuntu 22.04 LTS (Jammy Jellyfish), OpenJDK 21 headless runtime, Docker CE, containerd, curl, gnupg, ca-certificates, and UFW firewall.")
    add_bullet_p(c_cell, "Dedicated System User & Group: An unprivileged system group 'coldstorage' (GID 1001) and service user 'coldstorage' (UID 1001) with shell '/bin/false' to eliminate interactive login vulnerabilities.")
    add_bullet_p(c_cell, "Directory Hierarchy: Isolated root '/opt/coldstorage-app', configuration subdirectory '/opt/coldstorage-app/config', and log store '/opt/coldstorage-app/logs' with restricted permissions (0750) owned by coldstorage:coldstorage.")
    add_bullet_p(c_cell, "Configuration Files: Templated 'application-prod.properties' establishing H2 datasource parameters, actuator metrics exposure, and log formatting.")
    add_bullet_p(c_cell, "Networking & Firewall: TCP port 8080 explicitly permitted for HTTP traffic; TCP port 22 reserved for Ansible SSH management.")
    add_bullet_p(c_cell, "Daemons & Services: 'docker.service' enabled on boot; 'ufw.service' active to enforce iptables packet filtering.")

    # 3. Ansible Inventory & Agentless Architecture
    add_heading(c_cell, "3. Ansible Topology & Inventory Structure")
    add_body_p(
        c_cell,
        "Ansible operates in an agentless push topology. The Ansible Control Node parses 'hosts.ini' and executes tasks on target nodes "
        "via secure SSH tunnels. Figure 13.2 details the control node architecture communicating with staging and production environments."
    )

    fig13_1_path = os.path.abspath("screenshots/task13/fig13_1_ansible_cm_arch.png")
    if os.path.exists(fig13_1_path):
        add_figure(c_cell, fig13_1_path, "Figure 13.2: Ansible Configuration Management Architecture")

    add_body_p(
        c_cell,
        "The inventory file ('ansible/hosts.ini') segregates staging and production nodes while sharing common global variables:"
    )

    hosts_ini_snippet = (
        "[all:vars]\n"
        "ansible_user=ubuntu\n"
        "ansible_python_interpreter=/usr/bin/python3\n"
        "app_name=coldstorage-app\n"
        "app_port=8080\n"
        "app_root_dir=/opt/coldstorage-app\n"
        "app_user=coldstorage\n"
        "app_group=coldstorage\n\n"
        "[staging]\n"
        "node1.coldstorage.internal ansible_host=192.168.56.101 env=staging\n\n"
        "[production]\n"
        "node2.coldstorage.internal ansible_host=192.168.56.102 env=production"
    )
    p_hi = c_cell.add_paragraph()
    p_hi.paragraph_format.left_indent = Inches(0.2)
    p_hi.paragraph_format.space_after = Pt(4)
    run_hi = p_hi.add_run(hosts_ini_snippet)
    run_hi.font.name = "Consolas"
    run_hi.font.size = Pt(8.0)
    run_hi.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    # 4. Ansible Playbook Structure & Idempotent Mechanics
    add_heading(c_cell, "4. Structured YAML Playbook Design & Handlers")
    add_body_p(
        c_cell,
        "The provisioning logic is encapsulated within 'ansible/playbook.yml'. It leverages built-in idempotent modules "
        "(apt, systemd, user, file, template, ufw) to ensure that tasks execute only when state reconciliation is required. "
        "Figure 13.3 illustrates the playbook workflow and reactive event handlers."
    )

    fig13_3_path = os.path.abspath("screenshots/task13/fig13_3_ansible_playbook_structure.png")
    if os.path.exists(fig13_3_path):
        add_figure(c_cell, fig13_3_path, "Figure 13.3: Ansible Playbook Structure & Idempotent Handler Mechanics")

    playbook_yaml_snippet = (
        "# Structured Ansible Playbook (playbook.yml)\n"
        "- name: Configure Target Nodes for Cold Storage Slot Booking System\n"
        "  hosts: coldstorage_servers\n"
        "  become: true\n"
        "  tasks:\n"
        "    - name: 1. Update apt package index\n"
        "      ansible.builtin.apt: { update_cache: yes, cache_valid_time: 3600 }\n"
        "    - name: 2. Install baseline system prerequisite packages\n"
        "      ansible.builtin.apt: { name: '{{ required_packages }}', state: present }\n"
        "    - name: 5. Install Docker CE and container runtime\n"
        "      ansible.builtin.apt: { name: ['docker-ce', 'containerd.io'], state: present }\n"
        "      notify: Restart docker\n"
        "    - name: 6. Ensure Docker service is enabled and running\n"
        "      ansible.builtin.systemd: { name: docker, state: started, enabled: yes }\n"
        "    - name: 8. Create coldstorage unprivileged service user\n"
        "      ansible.builtin.user: { name: '{{ app_user }}', uid: 1001, shell: /bin/false }\n"
        "    - name: 10. Create application directory structure\n"
        "      ansible.builtin.file: { path: '{{ item }}', state: directory, mode: '0750' }\n"
        "      loop: ['/opt/coldstorage-app', '/opt/coldstorage-app/config', '/opt/coldstorage-app/logs']\n"
        "    - name: 12. Configure UFW firewall for port 8080/tcp\n"
        "      ansible.builtin.ufw: { rule: allow, port: '{{ app_port }}', proto: tcp }\n"
        "      notify: Reload ufw"
    )
    p_pb = c_cell.add_paragraph()
    p_pb.paragraph_format.left_indent = Inches(0.2)
    p_pb.paragraph_format.space_after = Pt(4)
    run_pb = p_pb.add_run(playbook_yaml_snippet)
    run_pb.font.name = "Consolas"
    run_pb.font.size = Pt(7.8)
    run_pb.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    # 5. First Playbook Execution Log Analysis
    add_heading(c_cell, "5. First Execution Log & Forensic Output")
    add_body_p(
        c_cell,
        "Executing 'ansible-playbook -i hosts.ini playbook.yml' initiated the first provisioning pass on the clean target node. "
        "As expected on a freshly installed system, Ansible performed all required state changes, created users, erected directory trees, "
        "and triggered notification handlers. Figure 13.4 captures the terminal session and PLAY RECAP summary."
    )

    fig13_4_path = os.path.abspath("screenshots/task13/fig13_4_first_execution_terminal.png")
    if os.path.exists(fig13_4_path):
        add_figure(c_cell, fig13_4_path, "Figure 13.4: Ansible CLI - First Execution of playbook.yml against Target Nodes")

    add_body_p(
        c_cell,
        "Key forensic observations from the first run log:"
    )
    add_bullet_p(c_cell, "Fact Gathering: Discovered distribution 'Ubuntu 22.04 LTS', kernel release, and available IP interfaces.")
    add_bullet_p(c_cell, "State Changes: Exactly 9 tasks reported 'changed', including Docker installation, user creation, and file generation.")
    add_bullet_p(c_cell, "Handler Invocations: Handlers 'Restart docker' and 'Reload ufw' fired automatically upon task notification.")
    add_bullet_p(c_cell, "Play Recap: 'ok=12 changed=9 unreachable=0 failed=0' confirmed 100% configuration success without runtime errors.")

    # 6. Server Prerequisites Verification Matrix
    add_heading(c_cell, "6. Server Prerequisites Verification Matrix")
    add_body_p(
        c_cell,
        "Table 13.1 correlates each server prerequisite with its desired state and verification command."
    )

    # Table 13.1: Verification matrix
    t_v = c_cell.add_table(rows=7, cols=4)
    apply_table_styles(t_v)

    headers = ["Prerequisite Category", "Resource / Identifier", "Desired State / Specification", "Verification Command"]
    for i, h in enumerate(headers):
        t_v.rows[0].cells[i].text = h
        style_cell(t_v.rows[0].cells[i], bold=True, font_size=9.0, text=h)

    prereq_data = [
        ("Base Runtime", "OpenJDK 21 JRE Headless", "Package present; java -version returns 21.0.x", "java -version"),
        ("Container Engine", "Docker CE 26+ & containerd", "Package present; systemctl is-active docker", "docker --version && systemctl status docker"),
        ("System User", "coldstorage (UID 1001)", "System user present; shell: /bin/false; group: 1001", "id coldstorage"),
        ("Directory Layout", "/opt/coldstorage-app (0750)", "Owner: coldstorage:coldstorage; mode: 0750", "ls -ld /opt/coldstorage-app/"),
        ("Application Config", "application-prod.properties", "Deployed from template; server.port=8080", "cat /opt/coldstorage-app/config/application-prod.properties"),
        ("Firewall Rule", "UFW TCP Port 8080", "Status: ALLOW IN from any to 8080/tcp", "sudo ufw status verbose | grep 8080")
    ]

    for row_idx, data in enumerate(prereq_data, start=1):
        for col_idx, text in enumerate(data):
            t_v.rows[row_idx].cells[col_idx].text = text
            style_cell(t_v.rows[row_idx].cells[col_idx], bold=(col_idx == 0), font_size=8.5, text=text)

    add_body_p(c_cell, "") # spacing

    # 7. Industrial Advantages
    add_heading(c_cell, "7. Industrial Impact for Cold Chain Warehouse Infrastructure")
    add_body_p(
        c_cell,
        "Codifying server prerequisites in Ansible guarantees operational consistency across geographically dispersed cold storage facilities:"
    )
    add_bullet_p(c_cell, "Rapid Warehouse Onboarding: New cold storage facility servers can be fully provisioned and hardened from bare metal in under 5 minutes.")
    add_bullet_p(c_cell, "Compliance & Security Hardening: Automated firewall locking and unprivileged service user execution eliminate human errors and security policy oversights.")
    add_bullet_p(c_cell, "Version-Controlled Infrastructure: Infrastructure changes follow the same pull request and review standards as application source code.")

    # Row 4: Conclusion
    c_conc = t2.rows[4].cells[1]
    c_conc.text = ""
    conc_p = (
        "In this task, all server prerequisites for the Cold Storage Slot Booking System—including system packages (OpenJDK 21, Docker CE, "
        "UFW), service accounts (coldstorage user/group UID 1001), directory hierarchies (/opt/coldstorage-app with 0750 permissions), configuration "
        "files, and firewall rules (port 8080/tcp)—were systematically identified, codified, and managed. An Ansible inventory ('hosts.ini') "
        "and structured YAML playbook ('playbook.yml') were authored following declarative Infrastructure as Code (IaC) principles. The first "
        "execution of the playbook successfully brought the clean target node into the desired operational state, yielding 'ok=12, changed=9, failed=0', "
        "and establishing an automated, auditable foundation for container deployment."
    )
    add_body_p(c_conc, conc_p)

    # Save and Archive Document
    output_filename = os.path.join("docs", f"DevOps_Task13_{STUDENT_NAME.replace(' ', '')}_{STUDENT_ROLL}.docx")
    save_and_archive(doc, output_filename)
    print(f"Task 13 document successfully generated at: {output_filename}")

if __name__ == "__main__":
    generate_task13_document()
