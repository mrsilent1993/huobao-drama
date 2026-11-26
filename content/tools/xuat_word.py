#!/usr/bin/env python3
"""Xuất file kịch bản .md sang Word (.docx), có ảnh Anh Tư ở đầu file.
Dùng: python3 xuat_word.py <file.md> [<file.md> ...]   → content/xuat/word/<tên>.docx
Hiểu các dạng md mà các _tapN.py sinh ra: tiêu đề #/##, đoạn văn, danh sách "- " và "1. ",
bảng "| … |", khối ``` (prompt: chữ đơn cách trong khung xám để copy), **đậm**, `mã`.
"""
import os
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANH_TU = os.path.join(ROOT, "nhan-vat", "anh_tu_ref.png")
ANH_TU_MAT = os.path.join(ROOT, "nhan-vat", "anh_tu_mat.png")
OUT_DIR = os.path.join(ROOT, "xuat", "word")


def shade(cell_or_par, hex_fill):
    el = cell_or_par._tc if hasattr(cell_or_par, "_tc") else cell_or_par._p
    pr = el.get_or_add_tcPr() if hasattr(cell_or_par, "_tc") else el.get_or_add_pPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), hex_fill)
    pr.append(shd)


def add_inline(par, text, size=None):
    """**đậm** và `mã` trong một dòng."""
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = par.add_run(part[2:-2])
            r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = par.add_run(part[1:-1])
            r.font.name = "Consolas"
            r.font.color.rgb = RGBColor(0x8A, 0x3B, 0x12)
        else:
            r = par.add_run(part.replace("*", ""))
        if size:
            r.font.size = Pt(size)


def add_code(doc, lines):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.rows[0].cells[0]
    shade(cell, "F2F2F2")
    p = cell.paragraphs[0]
    r = p.add_run("\n".join(lines))
    r.font.name = "Consolas"
    r.font.size = Pt(9)
    doc.add_paragraph()


def add_table(doc, rows):
    rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c) for c in r)]
    tbl = doc.add_table(rows=len(rows), cols=len(rows[0]))
    tbl.style = "Table Grid"
    for i, r in enumerate(rows):
        for j, c in enumerate(r[:len(rows[0])]):
            cell = tbl.cell(i, j)
            cell.paragraphs[0].text = ""
            add_inline(cell.paragraphs[0], c, size=9)
            if i == 0:
                shade(cell, "E7DCC8")
                for run in cell.paragraphs[0].runs:
                    run.bold = True
    doc.add_paragraph()


def _jpg(path):
    """Ảnh nhúng vào Word dùng bản JPEG nhẹ (ảnh gốc PNG vẫn giữ nguyên trong nhan-vat/)."""
    from PIL import Image
    out = os.path.splitext(path)[0] + "_word.jpg"
    if not os.path.exists(out) or os.path.getmtime(out) < os.path.getmtime(path):
        Image.open(path).convert("RGB").save(out, quality=85)
    return out


def header_block(doc):
    if not os.path.exists(ANH_TU):
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(_jpg(ANH_TU), height=Cm(9))
    if os.path.exists(ANH_TU_MAT):
        p.add_run("   ")
        p.add_run().add_picture(_jpg(ANH_TU_MAT), height=Cm(5))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_inline(cap, "**Anh Tư** · ảnh mẫu `anh_tu_ref.png`: đính kèm ảnh này ở **mọi clip** có Anh Tư (ảnh khung đầu và video). "
               "File ảnh gốc: `content/nhan-vat/anh_tu_ref.png`.", size=9)


def convert(md_path):
    lines = open(md_path, encoding="utf-8").read().split("\n")
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Arial"
    st.font.size = Pt(11)
    for s in doc.sections:
        s.left_margin = s.right_margin = Cm(2)
        s.top_margin = s.bottom_margin = Cm(1.8)
    i, first_h1 = 0, True
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            add_code(doc, lines[i + 1:j])
            i = j + 1
            continue
        if ln.startswith("|"):
            j = i
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            add_table(doc, lines[i:j])
            i = j
            continue
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            level = len(m.group(1))
            doc.add_heading(re.sub(r"[`*]", "", m.group(2)), level=level)
            if level == 1 and first_h1:
                header_block(doc)
                first_h1 = False
        elif re.match(r"^\s*- ", ln):
            add_inline(doc.add_paragraph(style="List Bullet"), ln.strip()[2:])
        elif re.match(r"^\d+\. ", ln):
            add_inline(doc.add_paragraph(style="List Number"), re.sub(r"^\d+\. ", "", ln))
        elif ln.strip():
            add_inline(doc.add_paragraph(), ln)
        i += 1
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, os.path.splitext(os.path.basename(md_path))[0] + ".docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(convert(path))
