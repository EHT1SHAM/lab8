from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from reportlab.lib import colors
import re

# Read the markdown file
with open('Lab_Task_8_Security_Report.md', 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Create PDF document
doc = SimpleDocTemplate("Lab_Task_8_Security_Report.pdf", pagesize=letter)
styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle(
    'Title',
    parent=styles['Heading1'],
    fontSize=24,
    spaceAfter=30,
    alignment=1,  # Center alignment
    textColor=colors.black,
)

heading1_style = ParagraphStyle(
    'Heading1',
    parent=styles['Heading1'],
    fontSize=18,
    spaceAfter=20,
    textColor=colors.darkblue,
)

heading2_style = ParagraphStyle(
    'Heading2',
    parent=styles['Heading2'],
    fontSize=14,
    spaceAfter=15,
    textColor=colors.darkslategray,
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=10,
    backgroundColor=colors.lightgrey,
    leftIndent=20,
)

normal_style = ParagraphStyle(
    'Normal',
    parent=styles['Normal'],
    fontSize=12,
    spaceAfter=12,
)

# Function to clean and parse markdown content
def clean_markdown(text):
    # Remove markdown links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove emphasis markers but keep text
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    return text

# Function to create flowables from markdown
def create_flowables(content):
    flowables = []
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('# '):
            # Title
            title_text = clean_markdown(line[2:])
            flowables.append(Paragraph(title_text, title_style))
            flowables.append(Spacer(1, 0.2*inch))

        elif line.startswith('## '):
            # Heading 1
            h1_text = clean_markdown(line[3:])
            flowables.append(Paragraph(h1_text, heading1_style))
            flowables.append(Spacer(1, 0.1*inch))

        elif line.startswith('### '):
            # Heading 2
            h2_text = clean_markdown(line[4:])
            flowables.append(Paragraph(h2_text, heading2_style))
            flowables.append(Spacer(1, 0.05*inch))

        elif line.startswith('- '):
            # List item
            list_text = clean_markdown(line[2:])
            flowables.append(Paragraph(f"• {list_text}", normal_style))

        elif line.startswith('```'):
            # Code block
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code_content = '\n'.join(code_lines)
            flowables.append(Paragraph(code_content, code_style))
            flowables.append(Spacer(1, 0.1*inch))

        elif line.strip() == '' or line.startswith('---'):
            # Empty line or horizontal rule
            flowables.append(Spacer(1, 0.05*inch))

        else:
            # Regular paragraph
            if line and not line.startswith('|'):  # Skip table rows for now
                clean_line = clean_markdown(line)
                if clean_line:
                    flowables.append(Paragraph(clean_line, normal_style))

        i += 1

    return flowables

# Clean the markdown content
clean_content = clean_markdown(markdown_content)

# Create flowables
flowables = create_flowables(clean_content)

# Build the PDF
doc.build(flowables)
print("PDF generated successfully!")