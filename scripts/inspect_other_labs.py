import fitz
import os
import glob

pdf_dir = r"E:\Dev\DevOPS\docs\Other labs"
files = glob.glob(os.path.join(pdf_dir, "*.pdf"))

for f in files:
    doc = fitz.open(f)
    print(f"\n==========================================")
    print(f"File: {os.path.basename(f)} (Pages: {len(doc)})")
    for pno in range(len(doc)):
        page = doc[pno]
        for term in ["Mubina", "23102A0039", "23102A039", "23102B0006"]:
            rects = page.search_for(term)
            if rects:
                for r in rects:
                    print(f"  Page {pno+1}: found '{term}' at rect {r}")
                    # Also get text font info around that rect
                    blocks = page.get_text("dict")["blocks"]
                    for b in blocks:
                        if "lines" in b:
                            for line in b["lines"]:
                                for span in line["spans"]:
                                    if term in span["text"]:
                                        print(f"    Font: {span['font']}, Size: {span['size']}, Color: {span['color']}, Origin: {span['origin']}")
