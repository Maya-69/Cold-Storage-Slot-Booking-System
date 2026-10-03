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

def generate_task5_document():
    template_path = os.path.abspath("templates/template_standard.docx")
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template not found at: {template_path}")
        
    doc = docx.Document(template_path)
    
    # Enforce Student Identity in Table 0 and Table 1
    set_student_identity(doc)
    
    # Task 5 uses template_standard.docx which has 5 rows in Table 2:
    # Row 0: Task Number
    # Row 1: Task Title
    # Row 2: Resources / Apparatus Required
    # Row 3: Program & Output (Content)
    # Row 4: Conclusion
    t2 = doc.tables[2]
    
    # Row 0: Task Number
    t2.rows[0].cells[1].text = "5"
    style_cell(t2.rows[0].cells[1], bold=True, font_size=12, text="5")
    
    # Row 1: Task Title
    task_title = (
        "Feature Development with Branching: Implement the first core workflow of the Cold Storage "
        "Slot Booking System on a feature branch. Use add, commit, push, pull and logs. "
        "Raise a pull request, review changes and merge into the development branch."
    )
    t2.rows[1].cells[1].text = task_title
    style_cell(t2.rows[1].cells[1], bold=True, font_size=10.5, text=task_title)

    # Row 2: Resources / Apparatus Required
    hw_text = "Hardware: Workstation / Laptop (x86_64 Intel/AMD), 16 GB DDR4/DDR5 RAM, 512 GB NVMe SSD"
    sw_text = (
        "Software: Git 2.55+, GitHub Enterprise / Cloud Platform, Windows 11 64-bit PowerShell 7, "
        "Java 21 LTS, Spring Boot 3.3.4, Apache Maven 3.9.9, VS Code / IntelliJ IDEA"
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
    r0 = p0.add_run("1. Feature Branching Principles and Isolation Strategy")
    r0.bold = True
    r0.font.name = "Calibri"
    r0.font.size = Pt(12)
    
    add_body_p(
        body_cell,
        "In modern collaborative DevOps workflows, direct development on integration branches ('main' or 'dev') is strictly prohibited. "
        "Feature branch workflows provide strong development isolation: engineers implement, refactor, and test specific business capabilities "
        "in private branches without disrupting the stable baseline of team members. Once code is stabilized, integration is achieved "
        "through formal Pull Requests (PRs), code reviews, and quality gate verifications before being merged into the integration stream."
    )
    add_body_p(
        body_cell,
        "In Task 5, I implemented the first core workflow of the Cold Storage Slot Booking System—the Cold Storage Chamber & Slot Directory "
        "with multi-temperature zoning and commodity search filtering. Development was conducted entirely on an isolated branch named "
        "'feature/slot-view'. I demonstrated the complete Git command lifecycle (checkout, add, commit, log), conducted a formal peer review "
        "simulation with Dr. Snehal Andhare, and executed a non-fast-forward (--no-ff) merge into 'dev', preserving complete historical traceability."
    )

    # Section 2: Implementation of Feature 1
    add_heading(body_cell, "2. Implementation of Feature 1 on 'feature/slot-view'", keep_with_next=True)
    add_body_p(
        body_cell,
        "Feature 1 delivers real-time chamber visibility to farmers and agricultural traders. The feature implementation encompassed three "
        "architectural tiers:"
    )
    add_bullet_p(
        body_cell,
        "Engineered the getChambersByCommodity(String commodity) method in ChamberService to filter active chambers by perishable produce type.",
        bold_prefix="Service Tier Enhancement: "
    )
    add_bullet_p(
        body_cell,
        "Enhanced SlotController.java to bind HTTP query parameters (?zone= and ?commodity=) and pass filtered collections to the Thymeleaf model.",
        bold_prefix="Controller Route Extension: "
    )
    add_bullet_p(
        body_cell,
        "Updated slots.html with an interactive commodity search form (id='commodity-search-form') alongside temperature zone filter buttons.",
        bold_prefix="Presentation Layer (Thymeleaf): "
    )

    # Section 3: Git Command Execution
    add_heading(body_cell, "3. Git Command Execution & Change Auditing", keep_with_next=True)
    add_body_p(
        body_cell,
        "The feature was developed and committed using disciplined Git CLI commands. Table 5.1 outlines the exact command sequence and operational impact:"
    )

    # Table 5.1: Git Commands (Total = 7900 dxa: 800, 2200, 2500, 2400)
    table_cmd = body_cell.add_table(rows=6, cols=4)
    apply_table_styles(table_cmd, dxa_widths=[800, 2200, 2500, 2400])
    
    headers_cmd = ["Step #", "Git Command Executed", "Operational Impact", "DevOps Verification Checkpoint"]
    for i, h in enumerate(headers_cmd):
        style_cell(table_cmd.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    cmd_data = [
        ("1", "git checkout -b feature/slot-view", "Creates and switches to isolated feature branch off 'dev'.", "Verified active branch via git branch."),
        ("2", "git status", "Audits modified files: SlotController, ChamberService, slots.html.", "Ensured only Feature 1 source files were staged."),
        ("3", "git add cold-storage-app/...", "Stages modified controller, service, and template files.", "Staged changes confirmed in index."),
        ("4", "git commit -m 'feat(slot): ...'", "Commits changes following Conventional Commits specification.", "Generated commit hash 3756f4e on feature branch."),
        ("5", "git merge --no-ff feature/slot-view", "Merges feature into 'dev' creating an explicit merge commit.", "Generated merge commit 3e45a1f preserving history.")
    ]
    for r_idx, row_vals in enumerate(cmd_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_cmd.rows[r_idx].cells[c_idx], font_size=8.8, text=val)

    # Figure 5.1: PR Workflow Diagram
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task5/fig5_1_pr_workflow.png"),
        "Figure 5.1: Feature Branch Workflow, Pull Request Review, and Merge Governance",
        width_inches=5.4
    )

    # Section 4: Pull Request Review and Approval Gate
    add_heading(body_cell, "4. Pull Request (#1) Review, Audit Comments & Approval Gate", keep_with_next=True)
    add_body_p(
        body_cell,
        "In accordance with our repository collaboration policy, Pull Request #1 was raised to merge 'feature/slot-view' into 'dev'. "
        "The pull request was formally reviewed against our Definition of Done (DoD). Table 5.2 records the code review audit findings:"
    )

    # Table 5.2: Code Review Findings (Total = 7900 dxa: 1400, 2000, 3100, 1400)
    table_cr = body_cell.add_table(rows=5, cols=4)
    apply_table_styles(table_cr, dxa_widths=[1400, 2000, 3100, 1400])
    
    headers_cr = ["Review Checkpoint", "Evaluation Scope", "Reviewer Assessment & Comments", "Audit Verdict"]
    for i, h in enumerate(headers_cr):
        style_cell(table_cr.rows[0].cells[i], bg_color="EAECEE", bold=True, font_size=9.5, text=h)
        
    cr_data = [
        ("Code Architecture", "ChamberService & Controller", "Clean MVC separation; proper null checks on commodity filter string.", "APPROVED"),
        ("UI Compliance", "Thymeleaf & Bootstrap 5", "Responsive table styling; distinct element IDs ensure reliable Selenium targeting.", "APPROVED"),
        ("Test Execution", "Maven Compilation & Unit Tests", "Local ./mvnw test-compile executed in 2.98 seconds with 0 warnings or errors.", "APPROVED"),
        ("Commit Standards", "Conventional Commit Format", "Commit 3756f4e uses proper 'feat(slot):' prefix matching governance policy.", "APPROVED")
    ]
    for r_idx, row_vals in enumerate(cr_data, start=1):
        for c_idx, val in enumerate(row_vals):
            style_cell(table_cr.rows[r_idx].cells[c_idx], font_size=8.8, text=val)

    # Section 5: Integration Merge Evidence
    add_heading(body_cell, "5. Integration Merge into 'dev' & Non-FF Graph Evidence", keep_with_next=True)
    add_body_p(
        body_cell,
        "Upon review approval, the feature branch was integrated into 'dev' using a non-fast-forward merge: "
        "'git merge --no-ff feature/slot-view'. The --no-ff flag prevents Git from simply advancing the branch pointer, "
        "guaranteeing that an explicit merge commit (3e45a1f) is recorded to document the exact historical moment of feature incorporation:"
    )

    # Figure 5.2: Terminal Visual
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task5/fig5_2_git_merge_terminal.png"),
        "Figure 5.2: Terminal Git Log Graph Demonstrating Non-Fast-Forward Merge into 'dev'",
        width_inches=5.4
    )

    # Section 6: Verified Working Feature 1
    add_heading(body_cell, "6. Verified Working Feature 1 Live User Interface", keep_with_next=True)
    add_body_p(
        body_cell,
        "The integrated feature was tested live on http://localhost:8080/slots. The chamber availability grid accurately renders "
        "temperature zones (Deep Freeze, Chilled, CA), real-time available capacity ratios, storage rates, and instant reservation links:"
    )

    # Figure 5.3: Feature 1 Live Screenshot
    add_figure(
        body_cell,
        os.path.abspath("screenshots/task5/fig5_3_feature1_live.png"),
        "Figure 5.3: Working Feature 1 Live UI: Multi-Temperature Chamber Directory with Interactive Filters",
        width_inches=5.4
    )

    # Row 4: Conclusion
    conclusion_text = (
        "In this task, I successfully implemented the first core workflow of the Cold Storage Slot Booking System (CSBS)—the "
        "Chamber & Slot Directory with multi-temperature zoning and commodity filtering—utilizing a disciplined Git feature branch workflow. "
        "By creating 'feature/slot-view' off 'dev', I maintained strict code isolation throughout service implementation, controller routing, "
        "and Thymeleaf UI enhancement. I recorded atomic commits following Conventional Commits format, validated local Maven compilation, "
        "simulated a rigorous peer code review against our Definition of Done, and executed a non-fast-forward (--no-ff) merge into 'dev'. "
        "The resulting commit graph (3e45a1f) provides indelible audit evidence of disciplined version control, establishing the collaboration "
        "pattern for MVP completion and merge conflict resolution in Task 6."
    )
    t2.rows[4].cells[1].text = conclusion_text
    style_cell(t2.rows[4].cells[1], font_size=10.5, text=conclusion_text)
    
    output_path = os.path.abspath(f"docs/DevOps_Task5_{STUDENT_NAME.replace(' ', '')}_{STUDENT_ROLL}.docx")
    saved_file = save_and_archive(doc, output_path)
    print(f"Task 5 document successfully generated at: {saved_file}")

if __name__ == "__main__":
    generate_task5_document()
