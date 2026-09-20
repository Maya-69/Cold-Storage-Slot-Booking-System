import os
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

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

def generate_task1_document():
    template_path = os.path.abspath("templates/template_task1.docx")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")
        
    doc = docx.Document(template_path)
    
    # Enforce Student Identity in Table 0 and Table 1
    set_student_identity(doc)
    
    # Task 1 uses template_task1.docx which has 4 rows in Table 2:
    # Row 0: Task Number
    # Row 1: Task Title
    # Row 2: Program & Output (Content)
    # Row 3: Conclusion
    t2 = doc.tables[2]
    
    # Row 0: Task Number
    t2.rows[0].cells[1].text = "1"
    style_cell(t2.rows[0].cells[1], bold=True, font_size=12, text="1")
    
    # Row 1: Task Title
    task_title = (
        "Problem Definition and Scope: Study the real-time need for the Cold Storage Slot Booking System. "
        "Identify target users, existing pain points, stakeholders, constraints and measurable success criteria. "
        "Freeze a small 15-Task MVP scope."
    )
    t2.rows[1].cells[1].text = task_title
    style_cell(t2.rows[1].cells[1], bold=True, font_size=10.5, text=task_title)
    
    # Row 2: Program & Output (Main Body Cell)
    body_cell = t2.rows[2].cells[1]
    if body_cell.paragraphs:
        body_cell.paragraphs[0].text = ""
        p0 = body_cell.paragraphs[0]
    else:
        p0 = body_cell.add_paragraph()
        
    p0.paragraph_format.space_before = Pt(4)
    p0.paragraph_format.space_after = Pt(2)
    p0.paragraph_format.keep_with_next = True
    r0 = p0.add_run("1. Executive Problem Background & Context")
    r0.bold = True
    r0.font.name = "Calibri"
    r0.font.size = Pt(12)
    
    add_body_p(
        body_cell,
        "Agricultural and cold-chain logistics in developing economies face acute structural bottlenecks. "
        "According to national agro-economic surveys, an estimated 25% to 35% of harvested perishable produce "
        "(including fruits, vegetables, fresh dairy, poultry, and marine catch) undergoes irreversible post-harvest spoilage "
        "prior to reaching terminal consumption markets. A primary catalyst of this economic loss is the absence of a synchronized, "
        "real-time reservation mechanism for commercial cold storage facilities. In the current operational landscape, smallholder "
        "farmers, merchant cooperatives, and freight handlers rely heavily on physical travel, fragmented telephone calls, or ad-hoc "
        "paper registers to inquire about cold storage chamber availability."
    )
    add_body_p(
        body_cell,
        "Consequently, farmers frequently arrive at facility receiving bays only to discover that temperature-controlled chambers "
        "are at full capacity, or lack the specific thermal environment required for their specific crop (e.g., Deep Freeze for seafood "
        "vs. Controlled Atmosphere for tubers). This results in catastrophic produce dumping, distressed distress-selling below cost, "
        "and prolonged multi-hour idling of refrigerated transport trucks. The objective of this project is to architect, build, containerize, "
        "and deploy a modern, cloud-ready web application—the Cold Storage Slot Booking System (CSBS)—supported by a fully automated "
        "DevOps pipeline spanning automated continuous integration, Selenium test gates, Docker packaging, and Ansible configuration management."
    )

    # Section 2: Formal Problem Statement
    add_heading(body_cell, "2. Formal Problem Statement", keep_with_next=True)
    add_body_p(
        body_cell,
        "Traditional multi-tenant cold storage facilities suffer from four interrelated systemic failures that prevent reliable operations:"
    )
    add_bullet_p(
        body_cell,
        "Absence of Real-Time Chamber Visibility: Farmers and merchants cannot ascertain chamber occupancy, temperature zoning, "
        "or dimensional slot availability prior to transporting highly perishable cargo.",
        bold_prefix="Opaque Inventory Tracking: "
    )
    add_bullet_p(
        body_cell,
        "Produce with incompatible preservation parameters (e.g., ethylene-sensitive leafy greens stored next to high-respiration fruits, "
        "or seafood requiring -20°C stored in 2°C chilled zones) is erroneously allocated due to manual paper logging.",
        bold_prefix="Thermal Zone Misallocation: "
    )
    add_bullet_p(
        body_cell,
        "Uncoordinated gate arrivals cause severe dock congestion, truck waiting durations between 6 and 14 hours, and temperature breaks "
        "during cargo staging that degrade food safety compliance.",
        bold_prefix="Logistical Bottlenecks: "
    )
    add_bullet_p(
        body_cell,
        "Lack of real-time software deployment pipelines causes warehouse management tools to remain brittle, requiring manual "
        "server provisioning, undocumented configuration drift, and lengthy software downtime during operational updates.",
        bold_prefix="DevOps Operational Deficit: "
    )

    # Section 3: Stakeholder Analysis
    add_heading(body_cell, "3. Stakeholder Analysis and Target User Personas", keep_with_next=True)
    add_body_p(
        body_cell,
        "To ensure the system satisfies end-to-end commercial workflows, I conducted a stakeholder requirements analysis across "
        "the cold-chain logistics domain. The primary stakeholder classes and their operational responsibilities are classified in Table 1.1:"
    )

    # Table 1.1: Stakeholders (Total = 7900 dxa: 1200, 1600, 2900, 2200)
    table_sh = body_cell.add_table(rows=6, cols=4)
    apply_table_styles(table_sh, dxa_widths=[1200, 1600, 2900, 2200])
    
    headers_sh = ["Stakeholder ID", "Stakeholder Role", "Operational Responsibilities", "Key Pain Points Addressed"]
    for i, h in enumerate(headers_sh):
        style_cell(table_sh.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    sh_data = [
        ("SH-01", "Perishable Produce Farmers", 
         "Registers harvest volume, reserves specific temperature-compatible slots, schedules check-in dates, tracks reservation status.",
         "Eliminates distress selling; guarantees dock acceptance before dispatch."),
        ("SH-02", "Commodity Traders & Wholesalers", 
         "Manages multi-crate consignments across dairy, poultry, seafood, and horticultural commodities; manages lease lifecycles.",
         "Provides transparent rate tracking and reliable reservation holding."),
        ("SH-03", "Cold Storage Warehouse Managers", 
         "Oversees physical chamber occupancy, confirms or cancels booking requests, monitors real-time capacity KPIs and dock scheduling.",
         "Replaces chaotic manual registers with real-time digital slot matrices."),
        ("SH-04", "Refrigerated Logistics Fleet", 
         "Transports cargo between farm-gate and facility; relies on pre-booked intake windows for zero gate idling.",
         "Reduces truck demurrage and dock staging turnaround from hours to minutes."),
        ("SH-05", "DevOps & Systems Evaluators", 
         "Deploys code updates, manages Jenkins CI pipelines, oversees Docker containers, and executes automated Ansible provisioning.",
         "Ensures deterministic releases, zero-downtime rollbacks, and 100% test pass gates.")
    ]
    for r_idx, row_vals in enumerate(sh_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_sh.rows[r_idx].cells[c_idx], font_size=8.8, text=val)

    # Figure 1.1
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task1/fig1_cold_storage_workflow.png"),
        "Figure 1.1: Cold Storage Slot Booking System (CSBS) Supply Chain Workflow and Chamber Zoning",
        width_inches=5.4
    )

    # Section 4: System Objectives and Measurable Success Criteria
    add_heading(body_cell, "4. System Objectives and Measurable Success Criteria", keep_with_next=True)
    add_body_p(
        body_cell,
        "The project combines application engineering goals with stringent DevOps delivery criteria. "
        "Table 1.2 establishes the quantitative metrics used to validate success across the 15-task development lifecycle:"
    )

    # Table 1.2: Success Criteria (Total = 7900 dxa: 800, 2000, 3100, 2000)
    table_sc = body_cell.add_table(rows=7, cols=4)
    apply_table_styles(table_sc, dxa_widths=[800, 2000, 3100, 2000])
    
    headers_sc = ["Obj ID", "Strategic Objective", "Implementation Target / Mechanism", "Measurable Success Metric"]
    for i, h in enumerate(headers_sc):
        style_cell(table_sc.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    sc_data = [
        ("OBJ-01", "Real-Time Slot Directory", 
         "Dynamic grid rendering active chambers across Deep Freeze, Chilled, and CA zones with instant availability indicators.",
         "Directory page load < 500 ms; real-time slot state reflection."),
        ("OBJ-02", "Automated Reservation Engine", 
         "Self-service booking capturing commodity type, crate count, and dates with overlap validation.",
         "Zero double-booking errors; 100% rejection of overlapping date windows."),
        ("OBJ-03", "Booking Lifecycle Enforcement", 
         "State machine governing PENDING -> CONFIRMED -> CHECKED_IN -> COMPLETED/CANCELLED transitions.",
         "100% adherence to state model; zero illegal status mutations."),
        ("OBJ-04", "Continuous Integration Reliability", 
         "Jenkins automated pipeline compiling Maven project and running headless Selenium test suites.",
         "Zero-defect pipeline execution; automated build time < 180 seconds."),
        ("OBJ-05", "Automated Quality Gate", 
         "Pipeline fails immediately upon assertion error in Selenium tests, blocking broken Docker image publication.",
         "100% prevention of broken artifacts reaching deployment environment."),
        ("OBJ-06", "Infrastructure Idempotency", 
         "Ansible configuration management ensuring clean deployment, directory creation, and rollback capabilities.",
         "0 failed tasks, 0 changes on second execution (changed=0, failed=0).")
    ]
    for r_idx, row_vals in enumerate(sc_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_sc.rows[r_idx].cells[c_idx], font_size=8.8, text=val)

    # Figure 1.2
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task1/fig2_stakeholder_matrix.png"),
        "Figure 1.2: Multi-Stakeholder Value Proposition and Pain Point Resolution Matrix",
        width_inches=5.4
    )

    # Section 5: Technical, Operational & Environmental Constraints
    add_heading(body_cell, "5. System Constraints and Design Boundaries", keep_with_next=True)
    add_body_p(
        body_cell,
        "To ensure high engineering rigor and seamless execution within university laboratory and CI/CD server environments, "
        "the architecture operates under the following explicit constraints:"
    )
    add_bullet_p(
        body_cell,
        "The application is engineered using Java 21+ and Spring Boot 3.x, compiled via an Apache Maven Wrapper (mvnw) to eliminate "
        "external build-tool installation discrepancies on Jenkins agent nodes.",
        bold_prefix="Runtime Autonomy: "
    )
    add_bullet_p(
        body_cell,
        "To maintain deterministic test velocity without requiring an external MySQL/PostgreSQL server daemon, the system utilizes "
        "an embedded in-memory H2 database with Spring Data JPA. This ensures sub-second test execution during CI test runs.",
        bold_prefix="Zero Database Footprint: "
    )
    add_bullet_p(
        body_cell,
        "Chamber temperature ranges strictly conform to international cold-storage standards: Deep Freeze (-18°C to -25°C for seafood/meat), "
        "Chilled (0°C to 4°C for dairy/fruits), and Controlled Atmosphere (10°C to 15°C for tubers/onions).",
        bold_prefix="Thermal Zoning Precision: "
    )
    add_bullet_p(
        body_cell,
        "The application exposes an HTTP GET /actuator/health endpoint returning 200 OK and JSON status 'UP' to support automated "
        "health probes by Jenkins pipeline post-deployment steps and Ansible reliability verification tasks.",
        bold_prefix="Observability Probe Standard: "
    )

    # Section 6: Approved 15-Task MVP Scope Breakdown
    add_heading(body_cell, "6. Approved 15-Task DevOps Laboratory MVP Scope", keep_with_next=True)
    add_body_p(
        body_cell,
        "In accordance with the official laboratory syllabus allocation, the Cold Storage Slot Booking System project is partitioned "
        "into fifteen sequential tasks spanning agile planning, software engineering, version control, automated testing, containerization, "
        "and configuration management. Table 1.3 defines the approved task roadmap and official deliverables:"
    )

    # Table 1.3: 15 Tasks (Total = 7900 dxa: 800, 2200, 4900)
    table_mvp = body_cell.add_table(rows=16, cols=3)
    apply_table_styles(table_mvp, dxa_widths=[800, 2200, 4900])
    
    headers_mvp = ["Task #", "Official Task Phase & Title", "Approved Scope & Concrete Technical Deliverable"]
    for i, h in enumerate(headers_mvp):
        style_cell(table_mvp.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    tasks_data = [
        ("Task 1", "Problem Definition & Scope", 
         "Analyze cold-chain logistics challenges, identify 5 stakeholder classes, define measurable KPIs, establish thermal constraints, and freeze 15-task MVP scope."),
        ("Task 2", "Agile Planning & DevOps Workflow", 
         "Generate user stories, acceptance criteria, product backlog, 15-task Kanban board, Definition of Done (DoD), and end-to-end DevOps lifecycle flow diagram."),
        ("Task 3", "Architecture & Technology Setup", 
         "Formulate SRS, design 4-tier Spring Boot architecture, model ER entities (Chamber, Slot, Booking, User), define REST APIs, and verify local execution on port 8080."),
        ("Task 4", "Git & GitHub Initialization", 
         "Establish git repository, configure .gitignore, README.md, branching model (main, dev, feature/*), issue templates, and commit the initial application skeleton."),
        ("Task 5", "Feature Development with Branching", 
         "Implement Feature 1 (User Registration & Chamber/Slot Availability View) on feature branch, demonstrate git add/commit/push, raise Pull Request, and merge to dev."),
        ("Task 6", "MVP Completion & Collaboration", 
         "Implement remaining MVP modules (Booking Request, Confirmation, Cancellation, Status Tracking), simulate and resolve a git merge conflict, and tag release v1.0.0."),
        ("Task 7", "Jenkins Installation & CI Job", 
         "Install and configure Jenkins, integrate local Git repository, establish Maven build job with commit polling trigger, and archive the compiled JAR artifact."),
        ("Task 8", "Pipeline as Code & Server Deployment", 
         "Create declarative Jenkinsfile (Checkout -> Build -> Package -> Deploy), deploy artifact to embedded Tomcat server, and parameterize deployment port."),
        ("Task 9", "Selenium Test Design & Execution", 
         "Implement Selenium WebDriver 4 test suite for 4 critical user journeys (slot booking, capacity validation, status transition), including failure screenshot hook."),
        ("Task 10", "Continuous Testing in Jenkins", 
         "Integrate Selenium test suite into Jenkins pipeline, publish test reports, deliberately introduce regression bug to fail pipeline, fix bug, and prove pipeline recovery."),
        ("Task 11", "Docker Image & Container Lifecycle", 
         "Write multi-stage Dockerfile, build lightweight image (coldstorage-app:1.0.0), run container with port mapping (8080:8080), inspect logs, and test container lifecycle."),
        ("Task 12", "Jenkins-Docker Continuous Deployment", 
         "Extend Jenkinsfile to build Docker image upon successful test pass, tag with build number, publish to registry, and deploy fresh container automatically."),
        ("Task 13", "Configuration Management Script", 
         "Specify server prerequisites (Java, Docker, directories, firewall), create Ansible inventory (hosts.ini) and playbook (playbook.yml) for automated provisioning."),
        ("Task 14", "Automated Provisioning & Reliability", 
         "Execute Ansible playbook to provision target environment, prove idempotency (changed=0 on rerun), perform curl health check on /actuator/health, and execute rollback."),
        ("Task 15", "Final End-to-End Release & Viva", 
         "Execute complete pipeline run (Git commit -> Jenkins CI -> Selenium Gate -> Docker CD -> Ansible Provisioning), compile comprehensive report, and prepare viva defense.")
    ]
    for r_idx, row_vals in enumerate(tasks_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_mvp.rows[r_idx].cells[c_idx], font_size=8.8, text=val)

    # Figure 1.3
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task1/fig3_devops_roadmap.png"),
        "Figure 1.3: DevOps Laboratory Project 15-Task Progression and Quality Gate Lifecycle",
        width_inches=5.4
    )

    # Row 3: Conclusion
    conclusion_text = (
        "In this foundational task, I thoroughly investigated the operational challenges of the cold-chain logistics sector "
        "and established the formal problem definition for the Cold Storage Slot Booking System (CSBS). By analyzing critical pain points "
        "across five key stakeholder groups—smallholder farmers, commercial traders, warehouse managers, logistics fleet operators, and DevOps engineers—I "
        "identified the need for a synchronized, web-based slot reservation platform that prevents post-harvest spoilage and eliminates transport bottlenecks. "
        "I formulated six measurable success criteria, defined rigorous architectural and regulatory constraints governing temperature zones (Deep Freeze, "
        "Chilled, Controlled Atmosphere), and froze an approved 15-task DevOps laboratory scope. This approved blueprint provides an unambiguous roadmap "
        "for subsequent agile sprint planning, Spring Boot implementation, automated Selenium regression testing, Docker containerization, Jenkins CI/CD automation, "
        "and Ansible configuration management."
    )
    t2.rows[3].cells[1].text = conclusion_text
    style_cell(t2.rows[3].cells[1], font_size=10.5, text=conclusion_text)
    
    output_path = os.path.abspath(f"docs/DevOps_Task1_{STUDENT_NAME.replace(' ', '')}_{STUDENT_ROLL}.docx")
    saved_file = save_and_archive(doc, output_path)
    print(f"Task 1 document successfully generated at: {saved_file}")

if __name__ == "__main__":
    generate_task1_document()
