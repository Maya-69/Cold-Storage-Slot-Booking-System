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

def generate_task2_document():
    template_path = os.path.abspath("templates/template_standard.docx")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")
        
    doc = docx.Document(template_path)
    
    # Enforce Student Identity in Table 0 and Table 1
    set_student_identity(doc)
    
    # Task 2 uses template_standard.docx which has 5 rows in Table 2:
    # Row 0: Task Number
    # Row 1: Task Title
    # Row 2: Resources / Apparatus Required
    # Row 3: Program & Output (Content)
    # Row 4: Conclusion
    t2 = doc.tables[2]
    
    # Row 0: Task Number
    t2.rows[0].cells[1].text = "2"
    style_cell(t2.rows[0].cells[1], bold=True, font_size=12, text="2")
    
    # Row 1: Task Title
    task_title = (
        "Agile Planning and DevOps Workflow: Create user stories and acceptance criteria for the "
        "Cold Storage Slot Booking System. Prepare a product backlog, 15-Task Kanban/Scrum plan, "
        "Definition of Done and a DevOps lifecycle diagram from development to operations."
    )
    t2.rows[1].cells[1].text = task_title
    style_cell(t2.rows[1].cells[1], bold=True, font_size=10.5, text=task_title)

    # Row 2: Resources / Apparatus Required
    hw_text = "Hardware: Workstation / Laptop (x86_64 Intel/AMD), 16 GB DDR4/DDR5 RAM, 512 GB NVMe SSD"
    sw_text = (
        "Software: Windows 11 64-bit, Eclipse Adoptium JDK 21 LTS, Apache Maven 3.9+, Spring Boot 3.3.x, "
        "Git 2.55+, Jenkins CI 2.450+, Docker Engine 26+, Ansible Core 2.16+, Selenium WebDriver 4.25+, "
        "Google Chrome / Headless Chromium, Jira/Kanban Planning Tool, VS Code / IntelliJ IDEA"
    )
    t2.rows[2].cells[1].text = hw_text
    style_cell(t2.rows[2].cells[1], font_size=9.5, text=hw_text)
    t2.rows[2].cells[2].text = sw_text
    style_cell(t2.rows[2].cells[2], font_size=9.5, text=sw_text)
    
    # Row 3: Program & Output (Main Body Cell)
    body_cell = t2.rows[3].cells[1]
    if body_cell.paragraphs:
        body_cell.paragraphs[0].text = ""
        p0 = body_cell.paragraphs[0]
    else:
        p0 = body_cell.add_paragraph()
        
    p0.paragraph_format.space_before = Pt(4)
    p0.paragraph_format.space_after = Pt(2)
    p0.paragraph_format.keep_with_next = True
    r0 = p0.add_run("1. Agile Framework and DevOps Methodology")
    r0.bold = True
    r0.font.name = "Calibri"
    r0.font.size = Pt(12)
    
    add_body_p(
        body_cell,
        "The development of the Cold Storage Slot Booking System (CSBS) is governed by an Agile-DevOps hybrid methodology. "
        "Agile Scrum and Kanban principles drive iterative requirement elaboration, user story sizing, and sprint planning, "
        "while DevOps practices ensure that every incremental code change is built, tested, packaged, and provisioned through an "
        "automated, repeatable continuous delivery pipeline. This tight synergy eliminates the traditional disconnect between software "
        "developers and infrastructure operators, ensuring high deployment velocity with zero regressions."
    )
    add_body_p(
        body_cell,
        "To guarantee that product deliverables directly satisfy end-user requirements, all functional requirements from Task 1 were decomposed "
        "into formal Agile User Stories utilizing the industry-standard Connextra template ('As a [role], I want to [action], so that [value]'). "
        "Each user story is coupled with testable Gherkin-syntax Acceptance Criteria ('Given-When-Then') that serve as the exact specification "
        "for our automated Selenium regression test suite in Task 9 and quality gates in Task 10."
    )

    # Section 2: User Stories and Acceptance Criteria
    add_heading(body_cell, "2. User Stories and Formal Acceptance Criteria", keep_with_next=True)
    add_body_p(
        body_cell,
        "Table 2.1 details the core user stories spanning user authentication, temperature-zoned directory browsing, booking reservation, "
        "lifecycle administration, and operational health probes:"
    )

    # Table 2.1: User Stories (Total = 7900 dxa: 800, 1400, 2900, 2800)
    table_us = body_cell.add_table(rows=6, cols=4)
    apply_table_styles(table_us, dxa_widths=[800, 1400, 2900, 2800])
    
    headers_us = ["Story ID", "Target Persona", "User Story Statement (Connextra)", "Acceptance Criteria (Gherkin Syntax)"]
    for i, h in enumerate(headers_us):
        style_cell(table_us.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    us_data = [
        ("US-01", "Farmer / Trader", 
         "As a produce farmer, I want to view active cold chambers categorized by temperature zone (Deep Freeze, Chilled, CA), so that I can identify suitable storage for my crop.",
         "Given the user is on the directory page (/slots),\nWhen they filter by 'Chilled' (0-4°C),\nThen only Chamber B slots suitable for apples/dairy shall be displayed."),
        ("US-02", "Farmer / Trader", 
         "As a farmer, I want to book a specific chamber slot by specifying commodity type, crate quantity, and dates, so that my harvest intake is reserved in advance.",
         "Given available slot capacity,\nWhen the user submits valid crate quantity and check-in/out dates,\nThen the booking is created in PENDING status and an instant confirmation code is generated."),
        ("US-03", "Validation Engine", 
         "As a system, I want to block reservation requests that exceed chamber crate limits or overlap with booked dates, so that double-booking is prevented.",
         "Given a slot is already booked for Date Range [D1, D2],\nWhen a user requests that slot for overlapping dates,\nThen the system rejects the submission with a clear validation error banner."),
        ("US-04", "Warehouse Manager", 
         "As a warehouse manager, I want to confirm or cancel pending bookings and track check-ins, so that facility capacity reflects physical inventory.",
         "Given a booking with status PENDING,\nWhen manager clicks 'Confirm Booking',\nThen status transitions to CONFIRMED and the slot availability count updates instantly."),
        ("US-05", "DevOps Engineer", 
         "As a DevOps engineer, I want an automated health check endpoint, so that Jenkins CI/CD and Ansible can verify application readiness post-deployment.",
         "Given the Spring Boot service is running,\nWhen an HTTP GET is made to /actuator/health,\nThen the system responds with HTTP 200 OK and JSON body {\"status\":\"UP\"}.")
    ]
    for r_idx, row_vals in enumerate(us_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_us.rows[r_idx].cells[c_idx], font_size=8.5, text=val)

    # Section 3: Product Backlog and Story Point Estimation
    add_heading(body_cell, "3. Prioritized Product Backlog & Story Point Estimation", keep_with_next=True)
    add_body_p(
        body_cell,
        "To establish realistic velocity and workload management, the product backlog is estimated using the modified Fibonacci "
        "sequence (1, 2, 3, 5, 8 story points). Story points encapsulate technical complexity, implementation uncertainty, and testing effort. "
        "Tasks are prioritized using the MoSCoW framework (Must Have, Should Have, Could Have). Table 2.2 defines the complete backlog:"
    )

    # Table 2.2: Product Backlog (Total = 7900 dxa: 800, 2400, 1100, 1400, 1100, 1100)
    table_pb = body_cell.add_table(rows=8, cols=6)
    apply_table_styles(table_pb, dxa_widths=[800, 2400, 1100, 1400, 1100, 1100])
    
    headers_pb = ["Backlog ID", "Feature / Epic Description", "Story Points", "MoSCoW Priority", "Sprint Target", "Primary Tech"]
    for i, h in enumerate(headers_pb):
        style_cell(table_pb.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.0, text=h)
        
    pb_data = [
        ("PB-01", "Application Foundation & H2 Data Models", "5 SP", "Must Have (M)", "Sprint 1", "Spring Data JPA"),
        ("PB-02", "Git VCS Setup & Branching Architecture", "3 SP", "Must Have (M)", "Sprint 1", "Git / GitHub"),
        ("PB-03", "Chamber Directory & Slot Grid UI", "5 SP", "Must Have (M)", "Sprint 2", "Thymeleaf / CSS"),
        ("PB-04", "Slot Booking & Date Overlap Validator", "5 SP", "Must Have (M)", "Sprint 2", "Spring Service"),
        ("PB-05", "Manager Lifecycle Status Machine", "3 SP", "Should Have (S)", "Sprint 2", "REST Controller"),
        ("PB-06", "Jenkins Continuous Integration Pipeline", "8 SP", "Must Have (M)", "Sprint 3", "Jenkins / Maven"),
        ("PB-07", "Selenium Automated Quality Gate Suite", "8 SP", "Must Have (M)", "Sprint 3", "Selenium 4 / JUnit")
    ]
    for r_idx, row_vals in enumerate(pb_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_pb.rows[r_idx].cells[c_idx], font_size=8.5, text=val)

    # Figure 2.1: DevOps Lifecycle Diagram
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task2/fig1_devops_lifecycle.png"),
        "Figure 2.1: Cold Storage Slot Booking System DevOps Continuous Delivery Lifecycle",
        width_inches=5.4
    )

    # Section 4: 15-Task Scrum & Kanban Sprint Plan
    add_heading(body_cell, "4. 15-Task Scrum & Kanban Sprint Execution Plan", keep_with_next=True)
    add_body_p(
        body_cell,
        "The fifteen laboratory tasks are distributed across four structured sprints, balancing conceptual architecture, "
        "feature coding, continuous integration, and infrastructure automation. Table 2.3 maps tasks to sprints, velocity allocations, "
        "and primary milestone outcomes:"
    )

    # Table 2.3: Sprint Plan (Total = 7900 dxa: 1100, 1600, 1800, 1400, 2000)
    table_sp = body_cell.add_table(rows=5, cols=5)
    apply_table_styles(table_sp, dxa_widths=[1100, 1600, 1800, 1400, 2000])
    
    headers_sp = ["Sprint #", "Sprint Focus & Theme", "Encompassed Tasks", "Total Points", "Key Milestone Outcome"]
    for i, h in enumerate(headers_sp):
        style_cell(table_sp.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    sp_data = [
        ("Sprint 1", "Foundations & VCS Initialization", "Tasks 1, 2, 3, 4", "13 SP", 
         "SRS, Agile Backlog, Spring Boot 3 architecture baselined, GitHub repository initialized with branch rules."),
        ("Sprint 2", "Feature Development & MVP Baseline", "Tasks 5, 6", "8 SP", 
         "Feature branching demonstrated, complete 5-module MVP implemented, merge conflict resolved, v1.0.0 tagged."),
        ("Sprint 3", "Continuous Testing & CI Quality Gate", "Tasks 7, 8, 9, 10", "20 SP", 
         "Jenkins pipeline configured, Tomcat deployment automated, Selenium tests written, quality gate defect-stop verified."),
        ("Sprint 4", "Container CD, Ansible & Final Release", "Tasks 11, 12, 13, 14, 15", "26 SP", 
         "Docker image lifecycle, automated continuous deployment, Ansible playbook idempotency, health checks, final viva release.")
    ]
    for r_idx, row_vals in enumerate(sp_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_sp.rows[r_idx].cells[c_idx], font_size=8.5, text=val)

    # Figure 2.2: Kanban Board
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task2/fig2_kanban_board.png"),
        "Figure 2.2: Cold Storage Slot Booking System 15-Task Kanban Sprint Board",
        width_inches=5.4
    )

    # Figure 2.3: Velocity Chart
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task2/fig3_sprint_velocity.png"),
        "Figure 2.3: Sprint Capacity and Story Point Velocity Distribution across 15 Tasks",
        width_inches=5.4
    )

    # Section 5: Definition of Done (DoD)
    add_heading(body_cell, "5. Formal Definition of Done (DoD) Quality Contract", keep_with_next=True)
    add_body_p(
        body_cell,
        "To ensure that no task or feature is marked complete prematurely, I established a rigorous, multifaceted Definition of Done (DoD). "
        "A user story, task, or pipeline release is classified as 'Done' strictly when all of the following criteria are validated:"
    )
    add_bullet_p(
        body_cell,
        "Code adheres to Java naming standards, Clean Code principles, and proper exception handling. Zero commented-out dead code.",
        bold_prefix="Source Code Quality: "
    )
    add_bullet_p(
        body_cell,
        "Every feature branch is merged into 'dev' exclusively through a reviewed Pull Request with conventional commit messages.",
        bold_prefix="Version Control Integrity: "
    )
    add_bullet_p(
        body_cell,
        "Maven wrapper successfully compiles the project ('./mvnw clean compile') with 0 compilation warnings or errors.",
        bold_prefix="Deterministic Build: "
    )
    add_bullet_p(
        body_cell,
        "All Selenium WebDriver end-to-end tests pass in headless execution mode. 100% of assertion checks must succeed.",
        bold_prefix="Automated Testing Gate: "
    )
    add_bullet_p(
        body_cell,
        "Jenkins pipeline executes Checkout -> Build -> Test -> Deploy without human intervention; failed tests halt deployment immediately.",
        bold_prefix="CI/CD Quality Enforcement: "
    )
    add_bullet_p(
        body_cell,
        "Multi-stage Docker image builds cleanly, runs on host port 8080, and exposes a healthy Spring Boot Actuator endpoint (/actuator/health).",
        bold_prefix="Containerization & Observability: "
    )
    add_bullet_p(
        body_cell,
        "Running the Ansible playbook a second time results in 'changed=0, failed=0', proving operational idempotency.",
        bold_prefix="Infrastructure Idempotency: "
    )
    add_bullet_p(
        body_cell,
        "Each task has an officially formatted Word document generated programmatically, containing centered diagrams and live terminal evidence.",
        bold_prefix="Academic Documentation: "
    )

    # Row 4: Conclusion
    conclusion_text = (
        "In this task, I successfully established the agile planning framework, product backlog, and DevOps workflow for the "
        "Cold Storage Slot Booking System (CSBS). I synthesized domain requirements into five formal Agile User Stories accompanied "
        "by testable Gherkin-syntax Acceptance Criteria, ensuring alignment between business needs and automated testing suites. "
        "I prioritized the product backlog across 67 story points and mapped all fifteen laboratory tasks across four structured sprints "
        "using a Kanban task board representation. The complete DevOps lifecycle was formulated—spanning continuous planning, coding, "
        "automated building, headless Selenium testing, Docker containerization, Jenkins continuous deployment, and Ansible provisioning. "
        "Finally, I codified an uncompromising eight-point Definition of Done (DoD) quality contract, providing the governing baseline "
        "for architectural implementation in Task 3 and version-controlled feature delivery in subsequent sprints."
    )
    t2.rows[4].cells[1].text = conclusion_text
    style_cell(t2.rows[4].cells[1], font_size=10.5, text=conclusion_text)
    
    output_path = os.path.abspath(f"docs/DevOps_Task2_{STUDENT_NAME.replace(' ', '')}_{STUDENT_ROLL}.docx")
    saved_file = save_and_archive(doc, output_path)
    print(f"Task 2 document successfully generated at: {saved_file}")

if __name__ == "__main__":
    generate_task2_document()
