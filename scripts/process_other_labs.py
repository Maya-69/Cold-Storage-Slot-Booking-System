import fitz
import os
import glob

src_dir = r"E:\Dev\DevOPS\docs\Other labs"
dst_dir = r"E:\Dev\DevOPS\docs\Mayuresh_Other_Labs"
os.makedirs(dst_dir, exist_ok=True)

files = [
    ("23102A039_DevOps_Lab-3.pdf", "23102A0029_MayureshSawant_DevOps_Lab-3.pdf"),
    ("23102A039_DevOps_Lab-4.pdf", "23102A0029_MayureshSawant_DevOps_Lab-4.pdf"),
    ("23102A0039_DevOps_Lab_5.pdf", "23102A0029_MayureshSawant_DevOps_Lab-5.pdf"),
    ("23102A0039_DevOps_lab6.docx (1).pdf", "23102A0029_MayureshSawant_DevOps_Lab-6.pdf"),
]

for src_name, dst_name in files:
    src_path = os.path.join(src_dir, src_name)
    dst_path = os.path.join(dst_dir, dst_name)
    
    doc = fitz.open(src_path)
    page = doc[0] # All names and roll numbers are on page 1 (index 0)
    
    # 1. Search for Mubina
    name_rects = page.search_for("Mubina")
    # 2. Search for 23102A0039 or 23102A039
    roll_rects = page.search_for("23102A0039") + page.search_for("23102A039")
    
    print(f"\nProcessing {src_name}:")
    print(f"  Found {len(name_rects)} name rects, {len(roll_rects)} roll rects")
    
    # Redact and replace Name
    for r in name_rects:
        # Expand slightly to clean the cell contents without touching table borders
        clean_rect = fitz.Rect(r.x0, r.y0 - 1, r.x0 + 250, r.y1 + 1)
        page.add_redact_annot(clean_rect, fill=(1, 1, 1))
    
    # Redact and replace Roll
    for r in roll_rects:
        clean_rect = fitz.Rect(r.x0, r.y0 - 1, r.x0 + 250, r.y1 + 1)
        page.add_redact_annot(clean_rect, fill=(1, 1, 1))
        
    page.apply_redactions()
    
    # Insert new text at exact origins
    for r in name_rects:
        # Determine font size from rect height or origin
        fsize = 11.5 if "Lab-3" in src_name or "Lab-4" in src_name else 12.0
        # Text baseline is roughly y1 - 2
        page.insert_text(fitz.Point(r.x0, r.y1 - 2.5), "Mayuresh Sawant", fontname="helv", fontsize=fsize, color=(0, 0, 0))
        print(f"  Inserted 'Mayuresh Sawant' at ({r.x0}, {r.y1 - 2.5})")
        
    for r in roll_rects:
        fsize = 11.5 if "Lab-3" in src_name or "Lab-4" in src_name else 12.0
        page.insert_text(fitz.Point(r.x0, r.y1 - 2.5), "23102A0029", fontname="helv", fontsize=fsize, color=(0, 0, 0))
        print(f"  Inserted '23102A0029' at ({r.x0}, {r.y1 - 2.5})")
        
    doc.save(dst_path)
    doc.close()
    print(f"  Saved updated PDF to: {dst_path}")
