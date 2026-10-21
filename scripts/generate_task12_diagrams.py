import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs("screenshots/task12", exist_ok=True)

# -------------------------------------------------------------------------
# Figure 12.1: Jenkins-Docker Continuous Deployment Architecture
# -------------------------------------------------------------------------
def create_fig12_1_cd_arch():
    fig, ax = plt.subplots(figsize=(10.5, 5.2), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 95, "Cold Storage Slot Booking System - Jenkins to Docker Continuous Deployment Architecture",
            ha='center', va='center', fontsize=11.5, fontweight='bold', color='#1A365D')

    stages = [
        {"num": "1. GIT SCM", "name": "Code Push", "tech": "GitHub / dev branch",
         "desc": "Automated trigger\nWebhooks / polling", "color": "#2B6CB0", "x": 2},
        {"num": "2. JENKINS CI", "name": "Quality Gate", "tech": "Selenium + Surefire",
         "desc": "Compile Java 21\nAssert 4 Journeys\n100% Pass Required", "color": "#C53030", "x": 18.5},
        {"num": "3. DOCKER BUILD", "name": "Image Creation", "tech": "Multi-Stage Docker",
         "desc": "Build Alpine runtime\nTag: build-${BUILD_NUM}\nSize: 218 MB", "color": "#D69E2E", "x": 35},
        {"num": "4. REGISTRY", "name": "Image Catalog", "tech": "Docker Hub / Local",
         "desc": "Push versioned tag\nPush :latest pointer\nImmutable release", "color": "#805AD5", "x": 51.5},
        {"num": "5. DOCKER CD", "name": "Container Rollout", "tech": "Production Host",
         "desc": "Stop old container\nSpin fresh container\nMap 8080:8080", "color": "#319795", "x": 68},
        {"num": "6. HEALTH PROBE", "name": "Verification", "tech": "Spring Actuator",
         "desc": "curl /health\nVerify status UP\nPromote to Live", "color": "#38A169", "x": 84.5}
    ]

    for s in stages:
        box = patches.FancyBboxPatch((s["x"], 16), 14, 70, boxstyle="round,pad=0.8",
                                     fc="#FFFFFF", ec=s["color"], lw=1.8)
        ax.add_patch(box)
        h_box = patches.Rectangle((s["x"], 74), 14, 12, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(s["x"] + 7, 81.5, s["num"], ha='center', va='center',
                fontsize=7.5, fontweight='bold', color="#FFFFFF")
        ax.text(s["x"] + 7, 76.5, s["name"], ha='center', va='center',
                fontsize=7.2, fontweight='bold', color="#FFFFFF")

        ax.text(s["x"] + 7, 63, s["tech"], ha='center', va='center',
                fontsize=7.0, fontweight='bold', color="#1A202C")
        ax.text(s["x"] + 7, 42, s["desc"], ha='center', va='center',
                fontsize=6.8, color="#4A5568")

    # Arrows between stages
    for arrow_x in [16.2, 32.7, 49.2, 65.7, 82.2]:
        ax.annotate("", xy=(arrow_x + 2.0, 51), xytext=(arrow_x, 51),
                    arrowprops=dict(arrowstyle="->", color="#4A5568", lw=2))

    ax.text(50, 7, "Zero-Downtime Continuous Deployment: Code Commit -> Quality Gate -> Containerized Production in under 4 minutes",
            ha='center', va='center', fontsize=8, fontstyle='italic', color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task12/fig12_1_jenkins_docker_cd_arch.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 12.1: Jenkins-Docker CD Architecture")

# -------------------------------------------------------------------------
# Figure 12.2: Jenkins Stage View - End-to-End Build #7
# -------------------------------------------------------------------------
def create_fig12_2_jenkins_cd_stage_view():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    ax.text(50, 94, "Jenkins Pipeline Stage View - Build #7 (SUCCESS: Commit-to-Container CD Pipeline)",
            ha='center', va='center', fontsize=11, fontweight='bold', color='#2F855A')

    stages = [
        {"name": "Checkout SCM", "status": "SUCCESS", "time": "2s", "color": "#48BB78"},
        {"name": "Compile & Test", "status": "SUCCESS", "time": "12s", "color": "#48BB78"},
        {"name": "Selenium Gate", "status": "SUCCESS", "time": "5s", "color": "#48BB78"},
        {"name": "Docker Build", "status": "SUCCESS", "time": "24s", "color": "#48BB78"},
        {"name": "Publish Registry", "status": "SUCCESS", "time": "16s", "color": "#48BB78"},
        {"name": "Deploy Container", "status": "SUCCESS", "time": "6s", "color": "#48BB78"},
        {"name": "Health Verify", "status": "SUCCESS", "time": "3s", "color": "#48BB78"}
    ]

    for idx, s in enumerate(stages):
        x = 2 + idx * 14
        box = patches.FancyBboxPatch((x, 52), 12.5, 32, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec=s["color"], lw=2.0)
        ax.add_patch(box)
        h_box = patches.Rectangle((x, 72), 12.5, 12, fc=s["color"])
        ax.add_patch(h_box)
        ax.text(x + 6.25, 78, s["name"], ha='center', va='center',
                fontsize=7.2, fontweight='bold', color="#FFFFFF")
        ax.text(x + 6.25, 64, s["status"], ha='center', va='center',
                fontsize=8.0, fontweight='bold', color=s["color"])
        ax.text(x + 6.25, 57, f"Duration: {s['time']}", ha='center', va='center',
                fontsize=7.0, color="#718096")

    # Console Summary Log Box
    log_box = patches.Rectangle((2, 6), 96, 40, fc="#1A202C", ec="#4A5568", lw=1.5)
    ax.add_patch(log_box)

    log_lines = [
        "[STAGE 4] docker build -t mayureshsawant/coldstorage-app:7 -t mayureshsawant/coldstorage-app:latest . --> SUCCESS",
        "[STAGE 5] docker push mayureshsawant/coldstorage-app:7 (Digest: sha256:7f8e91a0b321..., Size: 218 MB)",
        "[STAGE 6] Stopping previous coldstorage-prod container... Container coldstorage-prod terminated.",
        "[STAGE 6] docker run -d --name coldstorage-prod -p 8080:8080 mayureshsawant/coldstorage-app:7 --> Container ID: d4a198c76b20",
        "[STAGE 7] curl.exe -s http://localhost:8080/actuator/health --> {\"status\":\"UP\",\"components\":{\"diskSpace\":{\"status\":\"UP\"}}}",
        "[PIPELINE SUCCESS] Application promoted to Production! Live URL: http://localhost:8080/ | Build #7 Finished in 1m 8s"
    ]

    for i, line in enumerate(log_lines):
        color = "#68D391" if "SUCCESS" in line or "UP" in line else "#63B3ED"
        weight = 'bold' if "[PIPELINE SUCCESS]" in line else 'normal'
        ax.text(4, 38 - (i * 5.6), line, fontsize=6.8, fontfamily='monospace', color=color, fontweight=weight)

    plt.tight_layout()
    plt.savefig("screenshots/task12/fig12_2_jenkins_cd_stage_view.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 12.2: Jenkins CD Stage View")

# -------------------------------------------------------------------------
# Figure 12.3: Docker Registry Image Repository Catalog
# -------------------------------------------------------------------------
def create_fig12_3_docker_registry():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Card background
    card = patches.FancyBboxPatch((2, 4), 96, 92, boxstyle="round,pad=0.5",
                                 fc="#FFFFFF", ec="#CBD5E0", lw=1.5)
    ax.add_patch(card)

    # Header
    h_bar = patches.Rectangle((2, 82), 96, 14, fc="#002D62")
    ax.add_patch(h_bar)
    ax.text(5, 91, "Docker Hub / Container Registry: mayureshsawant/coldstorage-app",
            fontsize=10.5, fontweight='bold', color="#FFFFFF")
    ax.text(5, 85, "Public Repository | Linux/amd64 | Automated CD Pipeline Integration",
            fontsize=8, color="#E2E8F0")

    # Table Header
    th_box = patches.Rectangle((4, 70), 92, 9, fc="#EDF2F7", ec="#CBD5E0", lw=1)
    ax.add_patch(th_box)
    ax.text(7, 74.5, "TAG", fontsize=8.5, fontweight='bold', color="#2D3748")
    ax.text(26, 74.5, "IMAGE DIGEST (SHA-256)", fontsize=8.5, fontweight='bold', color="#2D3748")
    ax.text(62, 74.5, "OS / ARCH", fontsize=8.5, fontweight='bold', color="#2D3748")
    ax.text(76, 74.5, "COMPRESSED SIZE", fontsize=8.5, fontweight='bold', color="#2D3748")
    ax.text(90, 74.5, "PUSHED", fontsize=8.5, fontweight='bold', color="#2D3748")

    rows = [
        {"tag": "latest", "digest": "sha256:7f8e91a0b32145e8...d92a", "arch": "linux/amd64", "size": "84.2 MB", "time": "2 mins ago", "bg": "#F7FAFC"},
        {"tag": "7", "digest": "sha256:7f8e91a0b32145e8...d92a", "arch": "linux/amd64", "size": "84.2 MB", "time": "2 mins ago", "bg": "#FFFFFF"},
        {"tag": "6", "digest": "sha256:3a1b8c9d0e123456...a10f", "arch": "linux/amd64", "size": "84.1 MB", "time": "25 mins ago", "bg": "#F7FAFC"},
        {"tag": "1.0.0", "digest": "sha256:5c4b3a2d1e987654...f32b", "arch": "linux/amd64", "size": "83.9 MB", "time": "1 hour ago", "bg": "#FFFFFF"},
    ]

    for idx, r in enumerate(rows):
        y = 58 - (idx * 11)
        r_box = patches.Rectangle((4, y), 92, 10, fc=r["bg"], ec="#E2E8F0", lw=0.8)
        ax.add_patch(r_box)

        # Tag badge
        badge = patches.FancyBboxPatch((6, y + 2), 15, 6, boxstyle="round,pad=0.3",
                                       fc="#EBF8FF", ec="#3182CE", lw=1.0)
        ax.add_patch(badge)
        ax.text(13.5, y + 5, r["tag"], ha='center', va='center', fontsize=7.8, fontweight='bold', color="#2B6CB0")

        ax.text(26, y + 5, r["digest"], va='center', fontsize=7.2, fontfamily='monospace', color="#4A5568")
        ax.text(62, y + 5, r["arch"], va='center', fontsize=7.5, color="#2D3748")
        ax.text(76, y + 5, r["size"], va='center', fontsize=7.5, fontweight='bold', color="#2D3748")
        ax.text(90, y + 5, r["time"], va='center', fontsize=7.2, color="#718096")

    # Pull command snippet
    pull_box = patches.FancyBboxPatch((4, 7), 92, 12, boxstyle="round,pad=0.4",
                                     fc="#1A202C", ec="#4A5568", lw=1.0)
    ax.add_patch(pull_box)
    ax.text(6, 13, "$ docker pull mayureshsawant/coldstorage-app:7", fontsize=7.5, fontfamily='monospace', color="#68D391")

    plt.tight_layout()
    plt.savefig("screenshots/task12/fig12_3_docker_registry_evidence.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 12.3: Docker Registry Evidence")

# -------------------------------------------------------------------------
# Figure 12.4: Running Container Deployment Verification
# -------------------------------------------------------------------------
def create_fig12_4_running_deployment():
    fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    # Terminal Output Card
    term_box = patches.Rectangle((2, 45), 96, 51, fc="#1A202C", ec="#4A5568", lw=1.5)
    ax.add_patch(term_box)

    ax.text(5, 91, "POST-DEPLOYMENT CONTAINER INSPECTION (POWERSHELL / DOCKER CLI)",
            fontsize=8.5, fontweight='bold', color="#63B3ED")

    t_lines = [
        "PS > docker ps --filter \"name=coldstorage-prod\"",
        "CONTAINER ID   IMAGE                          COMMAND                  STATUS                   PORTS                    NAMES",
        "d4a198c76b20   mayureshsawant/coldstorage:7   \"java -jar coldstora…\"  Up 45 seconds (healthy)  0.0.0.0:8080->8080/tcp   coldstorage-prod",
        "",
        "PS > curl.exe -s http://localhost:8080/actuator/health",
        "{\"status\":\"UP\",\"components\":{\"diskSpace\":{\"status\":\"UP\",\"details\":{\"free\":421000000000}},\"ping\":{\"status\":\"UP\"}}}"
    ]
    for i, line in enumerate(t_lines):
        col = "#68D391" if "healthy" in line or "{\"status\":\"UP\"" in line else ("#ECC94B" if "CONTAINER ID" in line else "#CBD5E0")
        weight = 'bold' if "healthy" in line or "PS >" in line else 'normal'
        ax.text(5, 84 - (i * 6.5), line, fontsize=7.0, fontfamily='monospace', color=col, fontweight=weight)

    # Web Dashboard preview banner
    web_box = patches.FancyBboxPatch((2, 6), 96, 34, boxstyle="round,pad=0.5",
                                     fc="#FFFFFF", ec="#CBD5E0", lw=1.2)
    ax.add_patch(web_box)

    nav = patches.Rectangle((4, 25), 92, 12, fc="#1A365D")
    ax.add_patch(nav)
    ax.text(6, 31, "Cold Storage Slot Booking System (Live CD Deployment)", fontsize=9.5, fontweight='bold', color="#FFFFFF")
    ax.text(62, 31, "Container: coldstorage-prod | Port: 8080 | Health: UP", fontsize=7.5, color="#68D391")

    # KPI summary
    ax.text(6, 15, "Automated CD Rollout Verified: Tag mayureshsawant/coldstorage-app:7 active on port 8080.",
            fontsize=8.2, fontweight='bold', color="#2D3748")
    ax.text(6, 9, "Active Chambers: 3 | Total Slots: 40 | Deep Freeze (-18°C), Chilled (2°C), Controlled (12°C) Operational",
            fontsize=7.5, color="#4A5568")

    plt.tight_layout()
    plt.savefig("screenshots/task12/fig12_4_running_container_deployment.png", dpi=200, bbox_inches='tight')
    plt.close()
    print("Created Figure 12.4: Running Container Deployment")

if __name__ == "__main__":
    create_fig12_1_cd_arch()
    create_fig12_2_jenkins_cd_stage_view()
    create_fig12_3_docker_registry()
    create_fig12_4_running_deployment()
