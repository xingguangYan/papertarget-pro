#!/usr/bin/env python3
"""
Paper Analyzer - Extract and analyze paper text for submission intelligence.

Supports: PDF, DOCX, TXT, LaTeX input.
Outputs: structured paper DNA fields for PaperTarget Pro analysis.

Usage:
    python analyze_paper.py paper.pdf
    python analyze_paper.py manuscript.docx
    python analyze_paper.py paper.tex
"""

import re
import sys
from pathlib import Path


def extract_text_from_pdf(path):
    """Extract text from PDF using available libraries."""
    try:
        import PyPDF2
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "".join(page.extract_text() or "" for page in reader.pages)
    except ImportError:
        pass
    try:
        import pdfplumber
        with pdfplumber.open(path) as pdf:
            return "".join(page.extract_text() or "" for page in pdf.pages)
    except ImportError:
        print("[WARN] No PDF library found. Install: pip install PyPDF2 pdfplumber")
        return ""


def extract_text_from_docx(path):
    """Extract text from DOCX file."""
    try:
        from docx import Document
        doc = Document(path)
        return "".join(p.text + "
" for p in doc.paragraphs)
    except ImportError:
        print("[WARN] python-docx not found. Install: pip install python-docx")
        return ""


def extract_text_from_tex(path):
    """Extract readable text from LaTeX file."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    # Remove LaTeX commands
    text = re.sub(r"\\(?:[a-zA-Z]+|\[[^]]*\]|\{[^}]*\})", "", text)
    # Remove comments
    text = re.sub(r"(?m)^%.*", "", text)
    # Remove math delimiters
    text = text.replace("$$", "").replace("$", "")
    return text


def extract_paper_sections(text):
    """Extract common paper sections from raw text."""
    sections = {}
    pattern = r"(?m)^(Abstract|Introduction|Method|Methodology|Experiment|Result|Discussion|Conclusion|Conclusion and Future Work|Related Work|Reference)s?\s*$"
    current_section = "preamble"
    sections[current_section] = []
    for line in text.split("
"):
        m = re.match(pattern, line.strip(), re.IGNORECASE)
        if m:
            current_section = m.group(1).lower()
            sections[current_section] = []
        else:
            sections[current_section].append(line)
    return {k: "".join(v).strip() for k, v in sections.items() if "".join(v).strip()}


def analyze_paper(filepath):
    """Main analysis pipeline."""
    path = Path(filepath)
    if not path.exists():
        print(f"[ERROR] File not found: {path}")
        return None

    ext = path.suffix.lower()
    if ext == ".pdf":
        text = extract_text_from_pdf(path)
    elif ext == ".docx":
        text = extract_text_from_docx(path)
    elif ext == ".tex":
        text = extract_text_from_tex(path)
    elif ext == ".txt":
        text = path.read_text(encoding="utf-8", errors="ignore")
    else:
        print(f"[ERROR] Unsupported format: {ext}")
        return None

    if not text.strip():
        print("[ERROR] No text extracted from file.")
        return None

    print(f"[OK] Extracted {len(text)} characters from {path.name}")

    # Extract sections
    sections = extract_paper_sections(text)
    print(f"[OK] Found sections: {", ".join(sections.keys())}")

    # Extract title (first substantial line)
    lines = [l.strip() for l in text.split("
") if l.strip()]
    title = lines[0][:200] if lines else "Unknown"
    print(f"\n=== Paper Analysis Summary ===")
    print(f"Title: {title}")
    print(f"Total chars: {len(text)}")
    print(f"Word count: {len(text.split())}")
    print(f"Sections: {len(sections)}")

    # Word count by section
    for sec_name, sec_text in sections.items():
        words = len(sec_text.split())
        print(f"  {sec_name}: {words} words")

    # Extract key fields for Paper DNA
    abstract = sections.get("abstract", "")
    intro = sections.get("introduction", "")
    method = sections.get("method", "") or sections.get("methodology", "")
    results = sections.get("result", "") or sections.get("results", "")

    return {
        "title": title,
        "abstract": abstract[:2000],
        "introduction": intro[:1000],
        "methods": method[:2000],
        "results": results[:2000],
        "full_text": text[:15000],
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_paper.py <paper-file>")
        sys.exit(1)
    result = analyze_paper(sys.argv[1])
    if result:
        print("\n[OK] Ready for PaperTarget Pro analysis.")
    else:
        sys.exit(1)