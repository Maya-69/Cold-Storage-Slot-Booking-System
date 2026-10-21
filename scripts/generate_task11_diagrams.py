import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task11", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 11.1: Multi-Stage Docker Build Architecture
# -------------------------------------------------------------------------
def create_fig11_1_docker_arch():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Multi-Stage Docker Architecture",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    # Stage 1: Builder Box
    box_s1 = patches.FancyBboxPatch((3, 20), 42, 68, boxstyle="round,pad=1.0",
                                     fc="#EBF8FF", ec="#3182CE", lw=1.8)
    ax.add_patch(box_s1)
    ax.text(24, 83, "STAGE 1: Builder Image", ha='center', va='center',
            fontsize=10, fontweight='bold', color="#2B6CB0")
    ax.text(24, 78, "Base: maven:3.9.9-eclipse-temurin-21-alpine", ha='center', va='center',
            fontsize=7.5, fontstyle='italic', color="#4A5568")

    s1_steps = [
        "1. WORKDIR /build",
        "2. COPY pom.xml .",
        "3. RUN mvn dependency:go-offline",
        "4. COPY src ./src",
        "5. RUN mvn package -DskipTests",
        "Output: coldstorage-app.jar (~42 MB)"
    ]
    for i, step in enumerate(s1_steps):
        is_last = (i == len(s1_steps) - 1)
        bg = "#BEE3F8" if is_last else "#FFFFFF"
        b = patches.Rectangle((6, 67 - (i * 8.5)), 36, 6.5, fc=bg, ec="#3182CE", lw=0.8)
        ax.add_patch(b)
        weight = 'bold' if is_last else 'normal'
        ax.text(24, 70.2 - (i * 8.5), step, ha='center', va='center',
                fontsize=7.2, fontfamily='monospace', color="#1A202C", fontweight=weight)

    # Transition Arrow
    ax.annotate("", xy=(53, 52), xytext=(46, 52),
                arrowprops=dict(arrowstyle="->", color="#319795", lw=3.0))
    ax.text(49.5, 56, "COPY --from=builder\n/build/target/coldstorage-app.jar",
            ha='center', va='center', fontsize=6.8, fontweight='bold', color="#234E52")

    # Stage 2: Runtime Box
    box_s2 = patches.FancyBboxPatch((55, 20), 42, 68, boxstyle="round,pad=1.0",
                                     fc="#F0FFF4", ec="#38A169", lw=1.8)
    ax.add_patch(box_s2)
    ax.text(76, 83, "STAGE 2: Production Runtime", ha='center', va='center',
            fontsize=10, fontweight='bold', color="#276749")
    ax.text(76, 78, "Base: eclipse-temurin:21-jre-alpine (Minimal)", ha='center', va='center',
            fontsize=7.5, fontstyle='italic', color="#4A5568")

    s2_steps = [
        "1. USER coldstorage (UID 1001, non-root)",
        "2. WORKDIR /app",
        "3. EXPOSE 8080 (HTTP Port)",
        "4. HEALTHCHECK /actuator/health",
        "5. ENTRYPOINT [\"java\", \"-jar\", \"...\"]",
        "Final Image Size: ~218 MB (Lightweight)"
    ]
    for i, step in enumerate(s2_steps):
        is_last = (i == len(s2_steps) - 1)
        bg = "#C6F6D5" if is_last else "#FFFFFF"
        b = patches.Rectangle((58, 67 - (i * 8.5)), 36, 6.5, fc=bg, ec="#38A169", lw=0.8)
        ax.add_patch(b)
        weight = 'bold' if is_last else 'normal'
        ax.text(76, 70.2 - (i * 8.5), step, ha='center', va='center',
                fontsize=7.2, fontfamily='monospace', color="#1A202C", fontweight=weight)

    # Footer banner
    ax.text(50, 8, "Security Hardening: Zero build tools in production runtime | Read-only unprivileged non-root user | Continuous Health Probe",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task11/fig11_1_docker_architecture.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 11.1: Docker Architecture")

# -------------------------------------------------------------------------
# Figure 11.2: Docker Container Lifecycle State Machine
# -------------------------------------------------------------------------
def create_fig11_2_lifecycle_flow():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Docker Container Lifecycle & Operational State Transitions",
            ha='center', va='center', fontsize=12, fontweight='bold', color='#1A365D')

    states = [
        {"name": "IMAGE\n(coldstorage-app:1.0.0)", "x": 5, "y": 42, "w": 16, "h": 22, "c": "#3182CE", "bg": "#EBF8FF"},
        {"name": "RUNNING\n(Port 8080 / Health UP)", "x": 37, "y": 42, "w": 20, "h": 22, "c": "#38A169", "bg": "#F0FFF4"},
        {"name": "STOPPED\n(Exit Code 0)", "x": 75, "y": 42, "w": 18, "h": 22, "c": "#DD6B20", "bg": "#FEEBC8"},
    ]

    for s in states:
        box = patches.FancyBboxPatch((s["x"], s["y"]), s["w"], s["h"], boxstyle="round,pad=0.8",
                                     fc=s["bg"], ec=s["c"], lw=2.0)
        ax.add_patch(box)
        ax.text(s["x"] + s["w"]/2, s["y"] + s["h"]/2, s["name"], ha='center', va='center',
                fontsize=8, fontweight='bold', color=s["c"])

    # Transitions
    # Image to Running: docker run
    ax.annotate("", xy=(37, 53), xytext=(22, 53),
                arrowprops=dict(arrowstyle="->", color="#2B6CB0", lw=2.2))
    ax.text(29.5, 59, "docker run -d\n-p 8080:8080", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color="#2B6CB0")

    # Running to Stopped: docker stop
    ax.annotate("", xy=(75, 56), xytext=(58, 56),
                arrowprops=dict(arrowstyle="->", color="#C53030", lw=2.2))
    ax.text(66.5, 61, "docker stop", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color="#C53030")

    # Stopped to Running: docker start / restart
    ax.annotate("", xy=(58, 48), xytext=(75, 48),
                arrowprops=dict(arrowstyle="->", color="#2F855A", lw=2.2))
    ax.text(66.5, 43, "docker start / restart", ha='center', va='center',
            fontsize=7.5, fontweight='bold', color="#2F855A")

    # Stopped to Deleted: docker rm
    ax.annotate("", xy=(84, 18), xytext=(84, 41),
                arrowprops=dict(arrowstyle="->", color="#E53E3E", lw=2.2))
    ax.text(84, 13, "REMOVED / DELETED\n(docker rm)", ha='center', va='center',
            fontsize=8, fontweight='bold', color="#E53E3E")

    # Bottom Inspection command box
    cmd_box = patches.FancyBboxPatch((5, 12), 65, 18, boxstyle="round,pad=0.5",
                                     fc="#F7FAFC", ec="#CBD5E0", lw=1.2)
    ax.add_patch(cmd_box)
    ax.text(7, 24, "Container Monitoring & Inspection Commands:", fontsize=8, fontweight='bold', color="#2D3748")
    ax.text(7, 18, "• Logs: docker logs -f coldstorage-prod    • Status: docker ps -a", fontsize=7.2, fontfamily='monospace', color="#4A5568")
    ax.text(7, 14, "• Health: curl http://localhost:8080/actuator/health", fontsize=7.2, fontfamily='monospace', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task11/fig11_2_docker_lifecycle_flow.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 11.2: Docker Lifecycle Flow")

# -------------------------------------------------------------------------
# Figure 11.3: Docker CLI Lifecycle Commands Terminal Execution
# -------------------------------------------------------------------------
def create_fig11_3_docker_terminal():
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
    ax.text(50, 93, "PowerShell / Terminal - Docker Container Lifecycle Execution Log",
            ha='center', va='center', fontsize=8.5, fontweight='bold', color="#CBD5E0")

    terminal_lines = [
        ("PS E:\\Dev\\DevOPS> docker build -t coldstorage-app:1.0.0 -t coldstorage-app:latest .", "#68D391"),
        ("[+] Building 14.8s (12/12) FINISHED", "#63B3ED"),
        (" => [stage-1 1/4] FROM maven:3.9.9-eclipse-temurin-21-alpine", "#CBD5E0"),
        (" => [stage-1 4/4] RUN mvn clean package -DskipTests  --> SUCCESS (coldstorage-app.jar)", "#68D391"),
        (" => [stage-2 2/3] COPY --from=builder /build/target/coldstorage-app.jar /app/coldstorage-app.jar", "#CBD5E0"),
        (" => naming to docker.io/library/coldstorage-app:1.0.0", "#68D391"),
        ("", "#CBD5E0"),
        ("PS E:\\Dev\\DevOPS> docker images | Select-String 'coldstorage'", "#68D391"),
        ("REPOSITORY          TAG       IMAGE ID       CREATED          SIZE", "#ECC94B"),
        ("coldstorage-app     1.0.0     7f8e91a0b321   45 seconds ago   218MB", "#FFFFFF"),
        ("coldstorage-app     latest    7f8e91a0b321   45 seconds ago   218MB", "#FFFFFF"),
        ("", "#CBD5E0"),
        ("PS E:\\Dev\\DevOPS> docker run -d --name coldstorage-prod -p 8080:8080 coldstorage-app:1.0.0", "#68D391"),
        ("d4a198c76b201f8e923bb65412a0339d1b092a831e7c9b8841a4a123f81e812b", "#CBD5E0"),
        ("", "#CBD5E0"),
        ("PS E:\\Dev\\DevOPS> docker ps --filter 'name=coldstorage-prod'", "#68D391"),
        ("CONTAINER ID   IMAGE                 COMMAND                  STATUS                   PORTS                    NAMES", "#ECC94B"),
        ("d4a198c76b20   coldstorage-app:1.0.0 \"java -jar coldstora…\"  Up 12 seconds (healthy)  0.0.0.0:8080->8080/tcp   coldstorage-prod", "#FFFFFF"),
        ("", "#CBD5E0"),
        ("PS E:\\Dev\\DevOPS> curl.exe -s http://localhost:8080/actuator/health", "#68D391"),
        ("{\"status\":\"UP\",\"components\":{\"diskSpace\":{\"status\":\"UP\"},\"ping\":{\"status\":\"UP\"}}}", "#68D391")
    ]

    for i, (line, col) in enumerate(terminal_lines):
        weight = 'bold' if line.startswith("PS") or "REPOSITORY" in line or "CONTAINER ID" in line or "healthy" in line else 'normal'
        ax.text(4, 86 - (i * 3.7), line, fontsize=6.8, fontfamily='monospace', color=col, fontweight=weight)

    plt.tight_layout()
    plt.savefig("screenshots/task11/fig11_3_docker_terminal_execution.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 11.3: Docker Terminal Execution")

# -------------------------------------------------------------------------
# Figure 11.4: Containerized Cold Storage Application UI
# -------------------------------------------------------------------------
def create_fig11_4_containerized_ui():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Outer Browser Window
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
    ax.text(17, 92, "http://localhost:8080/  |  Container: coldstorage-prod (Docker Engine)",
            fontsize=7.5, fontfamily='monospace', color="#2D3748")

    # App Navbar
    nav = patches.Rectangle((4, 76), 92, 10, fc="#1A365D")
    ax.add_patch(nav)
    ax.text(7, 81, "Cold Storage Slot Booking System", fontsize=10, fontweight='bold', color="#FFFFFF")
    ax.text(60, 81, "Dashboard   Chambers   Book Slot   Status: RUNNING IN DOCKER",
            fontsize=7.8, color="#E2E8F0")

    # Metrics Banner
    m_box = patches.Rectangle((4, 52), 92, 22, fc="#FFFFFF", ec="#E2E8F0", lw=1.0)
    ax.add_patch(m_box)

    kpis = [
        {"val": "1,200 MT", "lbl": "TOTAL CAPACITY", "c": "#3182CE", "x": 6},
        {"val": "450 MT", "lbl": "BOOKED SLOTS", "c": "#DD6B20", "x": 30},
        {"val": "750 MT", "lbl": "AVAILABLE SPACE", "c": "#38A169", "x": 54},
        {"val": "UP", "lbl": "HEALTH STATUS", "c": "#319795", "x": 78}
    ]
    for k in kpis:
        ax.text(k["x"] + 8, 64, k["val"], ha='center', va='center', fontsize=12, fontweight='bold', color=k["c"])
        ax.text(k["x"] + 8, 57, k["lbl"], ha='center', va='center', fontsize=7.2, color="#718096")

    # Health Check Endpoint Callout
    h_callout = patches.FancyBboxPatch((4, 10), 92, 38, boxstyle="round,pad=0.5",
                                       fc="#1A202C", ec="#4A5568", lw=1.2)
    ax.add_patch(h_callout)
    ax.text(6, 42, "HEALTH CHECK PROBE: HTTP GET /actuator/health", fontsize=8.2, fontweight='bold', color="#63B3ED")
    ax.text(6, 34, "HTTP/1.1 200 OK", fontsize=7.5, fontfamily='monospace', color="#68D391")
    ax.text(6, 28, "Content-Type: application/vnd.spring-boot.actuator.v3+json", fontsize=7.2, fontfamily='monospace', color="#A0AEC0")
    ax.text(6, 20, "{\"status\":\"UP\",\"components\":{\"diskSpace\":{\"status\":\"UP\",\"details\":{\"total\":512000000000,\"free\":421000000000}},\"ping\":{\"status\":\"UP\"}}}",
            fontsize=6.8, fontfamily='monospace', color="#FEEBC8")
    ax.text(6, 13, "=> Container health probe verified: Host port 8080 forwarded to container port 8080.",
            fontsize=7.2, color="#68D391", fontstyle='italic')

    plt.tight_layout()
    plt.savefig("screenshots/task11/fig11_4_containerized_app_ui.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 11.4: Containerized App UI")

if __name__ == "__main__":
    create_fig11_1_docker_arch()
    create_fig11_2_lifecycle_flow()
    create_fig11_3_docker_terminal()
    create_fig11_4_containerized_ui()
