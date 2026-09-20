import os
import shutil
from datetime import datetime
import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

STUDENT_NAME = "Mayuresh Sawant"
STUDENT_ROLL = "23102A0029"
SUBJECT_NAME = "DevOps Lab"
SEMESTER = "B.E. Semester VII – Computer Engineering"
TEACHER_NAME = "Dr. Snehal Andhare"
PROJECT_TITLE = "Jenkins Deployment for a Cold Storage Slot Booking System"

def set_student_identity(doc):
    """
    Enforces Mayuresh Sawant and 23102A0029 in Table 1 across all templates.
    Also verifies Table 0.
    """
    if len(doc.tables) >= 2:
        # Table 0: Verification
        t0 = doc.tables[0]
        if len(t0.rows) >= 3:
            t0.rows[0].cells[1].text = SEMESTER
            style_cell(t0.rows[0].cells[1], font_size=10, text=SEMESTER)
            t0.rows[1].cells[1].text = SUBJECT_NAME
            style_cell(t0.rows[1].cells[1], font_size=10, text=SUBJECT_NAME)
            t0.rows[2].cells[1].text = TEACHER_NAME
            style_cell(t0.rows[2].cells[1], font_size=10, text=TEACHER_NAME)
        
        # Table 1: Student details
        t1 = doc.tables[1]
        if len(t1.rows) >= 2:
            t1.rows[0].cells[1].text = STUDENT_NAME
            style_cell(t1.rows[0].cells[1], font_size=10, bold=False, text=STUDENT_NAME)
            t1.rows[1].cells[1].text = STUDENT_ROLL
            style_cell(t1.rows[1].cells[1], font_size=10, bold=False, text=STUDENT_ROLL)

def apply_table_styles(table, dxa_widths=None):
    """
    Department styling enforcement:
    - Fixed table width: 7900 dxa (5.486 inches) fitting inside the cell
    - Fixed table layout (w:tblLayout type='fixed')
    - Clean single borders on all edges and inside cells (#CCCCCC)
    - Cell margins: top=80, bottom=80, left=80, right=80 dxa
    - tblHeader on row 0 so headers repeat across page breaks
    - cantSplit on every row so rows don't get sliced across page breaks
    - Exact dxa column widths applied to every cell
    """
    tblPr = table._tbl.tblPr
    
    for jc in tblPr.xpath('./w:jc'):
        tblPr.remove(jc)
        
    for w in tblPr.xpath('./w:tblW'):
        tblPr.remove(w)
    tblPr.append(parse_xml(r'<w:tblW %s w:w="7900" w:type="dxa"/>' % nsdecls('w')))
    
    for l in tblPr.xpath('./w:tblLayout'):
        tblPr.remove(l)
    tblPr.append(parse_xml(r'<w:tblLayout %s w:type="fixed"/>' % nsdecls('w')))
    
    for b in tblPr.xpath('./w:tblBorders'):
        tblPr.remove(b)
    tblBorders = parse_xml(r'''
        <w:tblBorders %s>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CCCCCC"/>
        </w:tblBorders>
    ''' % nsdecls('w'))
    tblPr.append(tblBorders)
    
    for m in tblPr.xpath('./w:tblCellMar'):
        tblPr.remove(m)
    tblCellMar = parse_xml(r'''
        <w:tblCellMar %s>
            <w:top w:w="80" w:type="dxa"/>
            <w:bottom w:w="80" w:type="dxa"/>
            <w:left w:w="80" w:type="dxa"/>
            <w:right w:w="80" w:type="dxa"/>
        </w:tblCellMar>
    ''' % nsdecls('w'))
    tblPr.append(tblCellMar)

    if len(table.rows) > 0:
        header_trPr = table.rows[0]._tr.get_or_add_trPr()
        if not header_trPr.xpath('./w:tblHeader'):
            header_trPr.append(parse_xml(r'<w:tblHeader %s/>' % nsdecls('w')))
        if not header_trPr.xpath('./w:cantSplit'):
            header_trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))
    
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if not trPr.xpath('./w:cantSplit'):
            trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))
        if dxa_widths:
            for idx, dxa_w in enumerate(dxa_widths):
                if idx < len(row.cells):
                    cell = row.cells[idx]
                    tcPr = cell._tc.get_or_add_tcPr()
                    for w in tcPr.xpath('./w:tcW'):
                        tcPr.remove(w)
                    tcPr.append(parse_xml(r'<w:tcW %s w:w="%s" w:type="dxa"/>' % (nsdecls('w'), str(dxa_w))))

def style_cell(cell, bg_color=None, bold=False, font_size=9.5, font_name="Calibri", text=None, align=WD_ALIGN_PARAGRAPH.LEFT):
    if bg_color:
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
        cell._tc.get_or_add_tcPr().append(shading)
    if text is not None:
        cell.text = text
    for p in cell.paragraphs:
        p.alignment = align
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        for r in p.runs:
            r.font.name = font_name
            r.font.size = Pt(font_size)
            r.bold = bold

def add_heading(cell, text, bold=True, size=12, keep_with_next=True):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = keep_with_next
    run = p.add_run(text)
    run.bold = bold
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    return p

def add_subheading(cell, text, bold=True, size=11, keep_with_next=True):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = keep_with_next
    run = p.add_run(text)
    run.bold = bold
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    return p

def add_body_p(cell, text, bold_prefix=None, space_after=3):
    p = cell.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(11)
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    return p

def add_bullet_p(cell, text, bold_prefix=None, space_after=2):
    p = cell.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    bullet_run = p.add_run("• ")
    bullet_run.bold = True
    bullet_run.font.name = "Calibri"
    bullet_run.font.size = Pt(11)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(11)
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(11)
    return p

def add_figure(cell, image_path, caption_text, width_inches=5.4):
    p = cell.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    run = p.add_run()
    run.add_picture(image_path, width=Inches(width_inches))
    
    cap = cell.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_before = Pt(2)
    cap.paragraph_format.space_after = Pt(8)
    cap.paragraph_format.keep_with_next = True
    c_run = cap.add_run(caption_text)
    c_run.bold = True
    c_run.font.name = "Calibri"
    c_run.font.size = Pt(10)
    return p, cap

def save_and_archive(doc, canonical_path):
    """
    Ensures docs/ directory has only the single canonical file.
    Whenever a new version is saved, any existing version is automatically
    moved into the docs/prev/ folder with a timestamp.
    """
    directory = os.path.dirname(canonical_path)
    filename = os.path.basename(canonical_path)
    base_name, ext = os.path.splitext(filename)
    
    prev_dir = os.path.join(directory, "prev")
    os.makedirs(prev_dir, exist_ok=True)
    
    if os.path.exists(canonical_path):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archived_filename = f"{base_name}_prev_{timestamp}{ext}"
        archived_path = os.path.join(prev_dir, archived_filename)
        try:
            shutil.move(canonical_path, archived_path)
            print(f"Previous version archived to: {archived_path}")
        except PermissionError:
            print(f"WARNING: '{canonical_path}' is open in Microsoft Word.")
            print("Please close it in Microsoft Word to allow archival.")
            draft_path = os.path.join(prev_dir, f"{base_name}_draft_{timestamp}{ext}")
            doc.save(draft_path)
            print(f"Draft saved to: {draft_path}")
            return draft_path

    doc.save(canonical_path)
    print(f"Canonical document saved to: {canonical_path}")
    return canonical_path
