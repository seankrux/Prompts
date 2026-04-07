#!/usr/bin/env python3
"""Generate a PDF from all markdown technique files."""

import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Preformatted, Table, TableStyle
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

BASE = "/Users/sean/Downloads/promptingguide-techniques"
OUTPUT = os.path.join(BASE, "Prompting-Techniques-Guide.pdf")

# Ordered files
FILES = [
    "01-techniques-overview.md",
    "02-zero-shot-prompting.md",
    "03-few-shot-prompting.md",
    "04-chain-of-thought.md",
    "05-meta-prompting.md",
    "06-self-consistency.md",
    "07-generated-knowledge.md",
    "08-prompt-chaining.md",
    "09-tree-of-thoughts.md",
    "10-rag.md",
    "11-art.md",
    "12-ape.md",
    "13-active-prompt.md",
    "14-directional-stimulus.md",
    "15-pal.md",
    "16-react.md",
    "17-reflexion.md",
    "18-multimodal-cot.md",
    "19-graph-prompting.md",
]

def escape_xml(text):
    """Escape XML special characters for ReportLab."""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text

def md_to_flowables(md_text, styles):
    """Convert markdown text to ReportLab flowables."""
    flowables = []
    lines = md_text.split("\n")
    i = 0
    in_code = False
    code_block = []

    while i < len(lines):
        line = lines[i]

        # Code block toggle
        if line.strip().startswith("```"):
            if in_code:
                # End code block
                code_text = "\n".join(code_block)
                if code_text.strip():
                    flowables.append(Spacer(1, 6))
                    flowables.append(Preformatted(code_text, styles["CodeBlock"]))
                    flowables.append(Spacer(1, 6))
                code_block = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue

        if in_code:
            code_block.append(line)
            i += 1
            continue

        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            i += 1
            continue

        # Skip source lines
        if stripped.startswith("Source:"):
            flowables.append(Paragraph(escape_xml(stripped), styles["Source"]))
            flowables.append(Spacer(1, 8))
            i += 1
            continue

        # H1
        if stripped.startswith("# ") and not stripped.startswith("## "):
            text = stripped[2:].strip()
            flowables.append(Paragraph(escape_xml(text), styles["H1"]))
            flowables.append(Spacer(1, 12))
            i += 1
            continue

        # H2
        if stripped.startswith("## "):
            text = stripped[3:].strip()
            flowables.append(Spacer(1, 8))
            flowables.append(Paragraph(escape_xml(text), styles["H2"]))
            flowables.append(Spacer(1, 8))
            i += 1
            continue

        # H3
        if stripped.startswith("### "):
            text = stripped[4:].strip()
            flowables.append(Spacer(1, 6))
            flowables.append(Paragraph(escape_xml(text), styles["H3"]))
            flowables.append(Spacer(1, 6))
            i += 1
            continue

        # Blockquote
        if stripped.startswith("> "):
            text = stripped[2:].strip()
            flowables.append(Paragraph(escape_xml(text), styles["Blockquote"]))
            flowables.append(Spacer(1, 4))
            i += 1
            continue

        # Bullet list
        if stripped.startswith("- ") or stripped.startswith("* "):
            text = stripped[2:].strip()
            # Handle bold in list items
            text = escape_xml(text)
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            flowables.append(Paragraph(f"&bull; {text}", styles["ListItem"]))
            i += 1
            continue

        # Numbered list
        m = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if m:
            num = m.group(1)
            text = escape_xml(m.group(2))
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            flowables.append(Paragraph(f"{num}. {text}", styles["ListItem"]))
            i += 1
            continue

        # Bold line (like **Prompt:**)
        if stripped.startswith("**") and stripped.endswith("**"):
            text = stripped[2:-2]
            flowables.append(Paragraph(f"<b>{escape_xml(text)}</b>", styles["Normal"]))
            i += 1
            continue

        # Regular paragraph - collect consecutive lines
        para_lines = [stripped]
        i += 1
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("#") and not lines[i].strip().startswith("```") and not lines[i].strip().startswith("- ") and not lines[i].strip().startswith("* ") and not re.match(r'^\d+\.', lines[i].strip()):
            para_lines.append(lines[i].strip())
            i += 1

        text = " ".join(para_lines)
        text = escape_xml(text)
        # Handle inline bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        # Handle inline italic
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        # Handle inline code
        text = re.sub(r'`(.*?)`', r'<font face="Courier" size="9">\1</font>', text)
        flowables.append(Paragraph(text, styles["Normal"]))
        flowables.append(Spacer(1, 4))

    return flowables


def build_pdf():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=letter,
        leftMargin=0.75*inch,
        rightMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch,
    )

    # Custom styles
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="H1",
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=HexColor("#1a1a2e"),
        spaceAfter=12,
    ))
    styles.add(ParagraphStyle(
        name="H2",
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        textColor=HexColor("#16213e"),
        spaceAfter=8,
    ))
    styles.add(ParagraphStyle(
        name="H3",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=15,
        textColor=HexColor("#0f3460"),
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name="Source",
        fontName="Helvetica-Oblique",
        fontSize=8,
        leading=10,
        textColor=HexColor("#666666"),
    ))
    styles.add(ParagraphStyle(
        name="CodeBlock",
        fontName="Courier",
        fontSize=8,
        leading=10,
        leftIndent=20,
        backColor=HexColor("#f5f5f5"),
        borderColor=HexColor("#cccccc"),
        borderWidth=0.5,
        borderPadding=6,
    ))
    styles.add(ParagraphStyle(
        name="Blockquote",
        fontName="Helvetica-Oblique",
        fontSize=10,
        leading=13,
        leftIndent=20,
        textColor=HexColor("#555555"),
    ))
    styles.add(ParagraphStyle(
        name="ListItem",
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        leftIndent=20,
        bulletIndent=10,
    ))

    # Override Normal
    styles["Normal"].fontSize = 10
    styles["Normal"].leading = 14
    styles["Normal"].fontName = "Helvetica"

    story = []

    # Title page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Prompting Techniques", ParagraphStyle(
        name="Title",
        fontName="Helvetica-Bold",
        fontSize=32,
        leading=38,
        alignment=TA_CENTER,
        textColor=HexColor("#1a1a2e"),
    )))
    story.append(Spacer(1, 20))
    story.append(Paragraph("Complete Guide", ParagraphStyle(
        name="Subtitle",
        fontName="Helvetica",
        fontSize=18,
        leading=22,
        alignment=TA_CENTER,
        textColor=HexColor("#555555"),
    )))
    story.append(Spacer(1, 40))
    story.append(Paragraph("Source: promptingguide.ai/techniques", ParagraphStyle(
        name="TitleSource",
        fontName="Helvetica-Oblique",
        fontSize=11,
        alignment=TA_CENTER,
        textColor=HexColor("#888888"),
    )))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Extracted: March 25, 2026", ParagraphStyle(
        name="TitleDate",
        fontName="Helvetica",
        fontSize=10,
        alignment=TA_CENTER,
        textColor=HexColor("#888888"),
    )))
    story.append(PageBreak())

    # Table of Contents
    story.append(Paragraph("Table of Contents", styles["H1"]))
    story.append(Spacer(1, 12))
    toc_items = [
        "1. Techniques Overview",
        "2. Zero-Shot Prompting",
        "3. Few-Shot Prompting",
        "4. Chain-of-Thought Prompting",
        "5. Meta Prompting",
        "6. Self-Consistency",
        "7. Generated Knowledge Prompting",
        "8. Prompt Chaining",
        "9. Tree of Thoughts",
        "10. Retrieval Augmented Generation (RAG)",
        "11. Automatic Reasoning and Tool-use (ART)",
        "12. Automatic Prompt Engineer (APE)",
        "13. Active-Prompt",
        "14. Directional Stimulus Prompting",
        "15. Program-Aided Language Models (PAL)",
        "16. ReAct Prompting",
        "17. Reflexion",
        "18. Multimodal CoT Prompting",
        "19. Graph Prompting",
    ]
    for item in toc_items:
        story.append(Paragraph(item, styles["ListItem"]))
        story.append(Spacer(1, 2))
    story.append(PageBreak())

    # Process each file
    for fname in FILES:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r") as f:
            content = f.read()
        flowables = md_to_flowables(content, styles)
        story.extend(flowables)
        story.append(PageBreak())

    doc.build(story)
    print(f"PDF created: {OUTPUT}")
    print(f"Size: {os.path.getsize(OUTPUT):,} bytes")


if __name__ == "__main__":
    build_pdf()
