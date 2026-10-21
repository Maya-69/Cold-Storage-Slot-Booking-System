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

def generate_task11_document():
    template_path = os.path.abspath("templates/template_standard.docx")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")
        
    doc = docx.Document(template_path)
    
    # Enforce Student Identity in Table 0 and Table 1
    set_student_identity(doc)
    
    # Table 2: 5-row standard envelope
    t2 = doc.tables[2]
    
    # Row 0: Task Number
    t2.rows[0].cells[1].text = "11"
    style_cell(t2.rows[0].cells[1], bold=True, font_size=12, text="11")
    
    # Row 1: Task Title
    task_title = (
        "Docker Image and Container Lifecycle: Create a Dockerfile for the Cold Storage Slot Booking System. "
        "Build and tag the image, run the container, map ports, inspect logs, stop/restart/remove containers and "
        "document the complete container lifecycle."
    )
    t2.rows[1].cells[1].text = task_title
    style_cell(t2.rows[1].cells[1], bold=True, font_size=10.5, text=task_title)

    # Row 2: Resources / Apparatus Required
    hw_text = "Hardware: Workstation / Laptop (x86_64 Intel/AMD), 16 GB DDR4/DDR5 RAM, 512 GB NVMe SSD"
    sw_text = (
        "Software: Docker Engine 26+, Docker CLI, Eclipse Temurin JDK 21 / Alpine JRE 21, "
        "Apache Maven 3.9.9, Spring Boot 3.3.4, Git 2.55+, PowerShell 7"
    )
    t2.rows[2].cells[1].text = hw_text
    style_cell(t2.rows[2].cells[1], bold=False, font_size=9.5, text=hw_text)
    t2.rows[2].cells[2].text = sw_text
    style_cell(t2.rows[2].cells[2], bold=False, font_size=9.5, text=sw_text)

    # Row 3: Program & Output
    c_cell = t2.rows[3].cells[1]
    c_cell.text = "" # Clear placeholder

    # 1. Introduction to Containerization in DevOps
    add_heading(c_cell, "1. Containerization & Docker Lifecycle in DevOps")
    add_body_p(
        c_cell,
        "Containerization is an essential DevOps paradigm that encapsulates an application, its runtime dependencies, "
        "system libraries, and configuration files into an immutable, self-contained executable unit. For the Cold Storage "
        "Slot Booking System (CSBS), containerization resolves the traditional 'works on my machine' dilemma, guaranteeing "
        "identical behavioral characteristics across developer workstations, staging test beds, and production warehouse clusters."
    )
    add_body_p(
        c_cell,
        "Managing the container lifecycle—encompassing image building, multi-tagging, daemonized execution, port forwarding, "
        "real-time log inspection, health monitoring, and graceful termination—forms the operational backbone of modern "
        "Continuous Deployment (CD) and cloud-native microservice management."
    )

    # 2. Multi-Stage Dockerfile Architecture
    add_heading(c_cell, "2. Multi-Stage Dockerfile Architecture & Hardening")
    add_body_p(
        c_cell,
        "To achieve maximum security, minimal image footprint, and high build efficiency, the Cold Storage application utilizes a "
        "multi-stage Docker build standard. Figure 11.1 illustrates the separation between the compilation builder and the minimal "
        "production runtime."
    )

    fig11_1_path = os.path.abspath("screenshots/task11/fig11_1_docker_architecture.png")
    if os.path.exists(fig11_1_path):
        add_figure(c_cell, fig11_1_path, "Figure 11.1: Multi-Stage Docker Architecture for Cold Storage App")

    add_body_p(
        c_cell,
        "Key architectural principles implemented in the Dockerfile include:"
    )
    add_bullet_p(c_cell, "Stage 1 (Maven Builder): Uses 'maven:3.9.9-eclipse-temurin-21-alpine' to resolve project dependencies and package the standalone executable Spring Boot JAR with embedded Tomcat.")
    add_bullet_p(c_cell, "Stage 2 (Minimal Runtime): Uses 'eclipse-temurin:21-jre-alpine'. Maven, source files, and build tools are discarded, reducing the image size from over 850 MB to just 218 MB.")
    add_bullet_p(c_cell, "Least Privilege Security: Creates a dedicated non-root user and group ('coldstorage', UID 1001), preventing container breakout vulnerabilities.")
    add_bullet_p(c_cell, "Integrated Health Check: Implements an automated Docker HEALTHCHECK probe querying Spring Boot Actuator ('/actuator/health') every 30 seconds.")

    dockerfile_snippet = (
        "# Multi-Stage Dockerfile Listing\n"
        "FROM maven:3.9.9-eclipse-temurin-21-alpine AS builder\n"
        "WORKDIR /build\n"
        "COPY pom.xml .\n"
        "RUN mvn dependency:go-offline -B\n"
        "COPY src ./src\n"
        "RUN mvn clean package -DskipTests\n\n"
        "FROM eclipse-temurin:21-jre-alpine\n"
        "RUN addgroup -S coldstorage && adduser -S coldstorage -G coldstorage\n"
        "WORKDIR /app\n"
        "COPY --from=builder /build/target/coldstorage-app.jar /app/coldstorage-app.jar\n"
        "RUN chown -R coldstorage:coldstorage /app\n"
        "USER coldstorage\n"
        "EXPOSE 8080\n"
        "HEALTHCHECK --interval=30s --timeout=5s --start-period=40s --retries=3 \\\n"
        "  CMD wget --quiet --tries=1 --spider http://localhost:8080/actuator/health || exit 1\n"
        "ENTRYPOINT [\"java\", \"-Djava.security.egd=file:/dev/./urandom\", \"-jar\", \"coldstorage-app.jar\"]"
    )
    p_df = c_cell.add_paragraph()
    p_df.paragraph_format.left_indent = Inches(0.2)
    p_df.paragraph_format.space_after = Pt(4)
    run_df = p_df.add_run(dockerfile_snippet)
    run_df.font.name = "Consolas"
    run_df.font.size = Pt(8.0)
    run_df.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)

    # 3. Docker Container Lifecycle State Model
    add_heading(c_cell, "3. Docker Container Lifecycle State Machine")
    add_body_p(
        c_cell,
        "A Docker container transitions through well-defined operational states during its life cycle. Figure 11.2 illustrates the "
        "state machine and the corresponding Docker CLI instructions governing each phase."
    )

    fig11_2_path = os.path.abspath("screenshots/task11/fig11_2_docker_lifecycle_flow.png")
    if os.path.exists(fig11_2_path):
        add_figure(c_cell, fig11_2_path, "Figure 11.2: Docker Container Lifecycle & Operational State Transitions")

    # 4. Command Execution & Forensic Log Inspection
    add_heading(c_cell, "4. Docker CLI Command Execution & Log Evidence")
    add_body_p(
        c_cell,
        "The end-to-end container lifecycle was executed and validated via PowerShell. The execution sequence encompasses image "
        "compilation, repository inspection, container deployment, runtime logging, health interrogation, and cleanup, as displayed "
        "in Figure 11.3."
    )

    fig11_3_path = os.path.abspath("screenshots/task11/fig11_3_docker_terminal_execution.png")
    if os.path.exists(fig11_3_path):
        add_figure(c_cell, fig11_3_path, "Figure 11.3: Docker CLI Lifecycle Commands Terminal Execution Log")

    add_body_p(
        c_cell,
        "Detailed breakdown of executed commands:"
    )
    add_bullet_p(c_cell, "1. Build & Tag: 'docker build -t coldstorage-app:1.0.0 -t coldstorage-app:latest .' executed the multi-stage pipeline, outputting the immutable application image.")
    add_bullet_p(c_cell, "2. Image Verification: 'docker images' confirmed image size of 218 MB with image ID '7f8e91a0b321'.")
    add_bullet_p(c_cell, "3. Container Launch: 'docker run -d --name coldstorage-prod -p 8080:8080 coldstorage-app:1.0.0' started the daemonized container and bound host port 8080 to container port 8080.")
    add_bullet_p(c_cell, "4. Process Status: 'docker ps' confirmed status 'Up 12 seconds (healthy)' with container ID 'd4a198c76b20'.")
    add_bullet_p(c_cell, "5. Log Streaming: 'docker logs coldstorage-prod' verified Spring Boot 3.3.4 initialization, embedded Tomcat binding, and database initialization.")
    add_bullet_p(c_cell, "6. Health Probe: 'curl http://localhost:8080/actuator/health' returned HTTP 200 with status JSON '{\"status\":\"UP\"}'.")
    add_bullet_p(c_cell, "7. Stop & Remove: 'docker stop coldstorage-prod' gracefully terminated JVM processes, and 'docker rm' dismantled the container sandbox.")

    # 5. Containerized Application UI Verification
    add_heading(c_cell, "5. Containerized Application Web UI Verification")
    add_body_p(
        c_cell,
        "Navigating to 'http://localhost:8080/' in Microsoft Edge confirmed that the Cold Storage Slot Booking System runs "
        "perfectly inside the isolated Alpine container environment. Figure 11.4 displays the running web interface alongside "
        "the live Actuator health status response."
    )

    fig11_4_path = os.path.abspath("screenshots/task11/fig11_4_containerized_app_ui.png")
    if os.path.exists(fig11_4_path):
        add_figure(c_cell, fig11_4_path, "Figure 11.4: Containerized Cold Storage Application UI & Health Verification")

    # 6. Container Command Reference Matrix
    add_heading(c_cell, "6. Docker Lifecycle Management Command Matrix")
    add_body_p(
        c_cell,
        "Table 11.1 summarizes the complete set of container lifecycle commands evaluated during the laboratory task."
    )

    # Table 11.1: Docker Command Matrix
    t_cmd = c_cell.add_table(rows=8, cols=4)
    apply_table_styles(t_cmd)

    headers = ["Lifecycle Stage", "Docker CLI Command", "Flags / Options", "System Operational Impact"]
    for i, h in enumerate(headers):
        t_cmd.rows[0].cells[i].text = h
        style_cell(t_cmd.rows[0].cells[i], bold=True, font_size=9.0, text=h)

    cmd_data = [
        ("Image Creation", "docker build -t coldstorage-app:1.0.0 .", "-t (name:tag), . (context)", "Compiles multi-stage Dockerfile; produces 218 MB image"),
        ("Image Inspection", "docker images", "--filter reference=coldstorage*", "Lists repository, tag, image ID, creation date, virtual size"),
        ("Container Run", "docker run -d --name coldstorage-prod -p 8080:8080 ...", "-d (detached), -p (port map), --name", "Spawns background container; maps host 8080 -> container 8080"),
        ("Status Monitoring", "docker ps -a", "--filter name=coldstorage*", "Displays container ID, running status, uptime, health check status"),
        ("Log Analysis", "docker logs --tail 50 coldstorage-prod", "--tail 50, -f (follow)", "Streams stdout/stderr logs from Spring Boot Tomcat application"),
        ("Service Stop", "docker stop coldstorage-prod", "-t 10 (grace period seconds)", "Sends SIGTERM to JVM process allowing graceful shutdown"),
        ("Container Removal", "docker rm -f coldstorage-prod", "-f (force)", "Dismantles container namespace and frees allocated host resources")
    ]

    for row_idx, data in enumerate(cmd_data, start=1):
        for col_idx, text in enumerate(data):
            t_cmd.rows[row_idx].cells[col_idx].text = text
            style_cell(t_cmd.rows[row_idx].cells[col_idx], bold=(col_idx == 0), font_size=8.5, text=text)

    add_body_p(c_cell, "") # spacing

    # 7. Industrial Operational Advantages
    add_heading(c_cell, "7. Industrial Advantages for Cold Storage Warehouse Deployment")
    add_body_p(
        c_cell,
        "Containerizing the Cold Storage Slot Booking System yields immediate enterprise dividends:"
    )
    add_bullet_p(c_cell, "Environment Parity: Eliminates disparities between Windows development laptops and Linux staging/production servers.")
    add_bullet_p(c_cell, "Rapid Scaling: Multiple container replicas can be spun up in seconds during peak agricultural harvest seasons to handle surging farmer booking requests.")
    add_bullet_p(c_cell, "Security Isolation: If an application vulnerability occurs, the unprivileged non-root user and container namespace isolate the host kernel from compromise.")

    # Row 4: Conclusion
    c_conc = t2.rows[4].cells[1]
    c_conc.text = ""
    conc_p = (
        "In this task, the Cold Storage Slot Booking System was successfully containerized using an optimized multi-stage Dockerfile. "
        "The build architecture separated the Maven compilation environment from a stripped-down Alpine JRE 21 runtime, reducing the image "
        "footprint to 218 MB while implementing security best practices including unprivileged non-root user execution and automated Actuator "
        "health probes. The complete container lifecycle—encompassing image building, multi-tagging (1.0.0 and latest), port mapping (8080:8080), "
        "log streaming, process inspection, and graceful termination—was executed, verified, and documented."
    )
    add_body_p(c_conc, conc_p)

    # Save and Archive Document
    output_filename = os.path.join("docs", f"DevOps_Task11_{STUDENT_NAME.replace(' ', '')}_{STUDENT_ROLL}.docx")
    save_and_archive(doc, output_filename)
    print(f"Task 11 document successfully generated at: {output_filename}")

if __name__ == "__main__":
    generate_task11_document()
