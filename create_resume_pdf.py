#!/usr/bin/env python3

import sys
import os

# Try to use available PDF libraries
try:
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER
    HAS_REPORTLAB = True
except ImportError:
    HAS_REPORTLAB = False

def create_resume_pdf():
    if not HAS_REPORTLAB:
        print("ReportLab not available. Creating HTML version only.")
        return False
    
    # Create PDF document
    doc = SimpleDocTemplate("resume.pdf", pagesize=A4, 
                          rightMargin=0.75*inch, leftMargin=0.75*inch,
                          topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=12,
        textColor=colors.black,
        fontName='Helvetica-Bold'
    )
    
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        spaceBefore=12,
        textColor=colors.black,
        fontName='Helvetica-Bold',
        alignment=TA_CENTER
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        fontName='Helvetica'
    )
    
    bold_style = ParagraphStyle(
        'CustomBold',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    # Content list
    content = []
    
    # Header
    header_data = [
        [Paragraph("YOUR NAME", title_style), 
         Paragraph("Email: your.email@example.com<br/>Mobile: +1 234-567-8900", normal_style)]
    ]
    header_table = Table(header_data, colWidths=[4*inch, 2.5*inch])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (-1, 0), 2, colors.black),
    ]))
    content.append(header_table)
    content.append(Spacer(1, 12))
    
    # LinkedIn and GitHub
    content.append(Paragraph("LinkedIn: your-linkedin-profile | GitHub: your-github-profile", normal_style))
    content.append(Spacer(1, 12))
    
    # Education Section
    content.append(Paragraph("EDUCATION", section_style))
    
    edu_data = [
        ["Your University Name", "City, Country\nMonth Year - Month Year"],
        ["Master of Computer Application, GPA: X.XX", ""],
        ["", ""],
        ["Your College Name", "City, Country\nMonth Year - Month Year"],
        ["Bachelor of Science (HONORS) - Your Major, GPA: X.XX", ""]
    ]
    edu_table = Table(edu_data, colWidths=[4*inch, 2.5*inch])
    edu_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 3), (0, 3), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(edu_table)
    content.append(Spacer(1, 12))
    
    # Skills Summary
    content.append(Paragraph("SKILLS SUMMARY", section_style))
    
    skills_data = [
        ["Languages:", "Python, Java, JavaScript, SQL, etc."],
        ["Frameworks:", "React, Node.js, Django, Flask, etc."],
        ["Tools:", "Git, Docker, AWS, MongoDB, etc."],
        ["Platforms:", "Linux, Windows, MacOS, Cloud Platforms"],
        ["Soft Skills:", "Leadership, Communication, Problem Solving, Team Collaboration"]
    ]
    skills_table = Table(skills_data, colWidths=[1.5*inch, 5*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 12))
    
    # Work Experience
    content.append(Paragraph("WORK EXPERIENCE", section_style))
    
    work_header = [
        ["JOB TITLE | COMPANY NAME | LINK", "Month Year - Month Year"]
    ]
    work_table = Table(work_header, colWidths=[4*inch, 2.5*inch])
    work_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(work_table)
    
    content.append(Paragraph("• Describe your key achievement or responsibility with quantifiable results", normal_style))
    content.append(Paragraph("• Another significant contribution you made to the organization", normal_style))
    content.append(Paragraph("• Third major accomplishment with specific metrics or outcomes", normal_style))
    content.append(Paragraph("• Additional responsibility that demonstrates your skills and impact", normal_style))
    content.append(Spacer(1, 12))
    
    # Projects
    content.append(Paragraph("PROJECTS", section_style))
    
    project1_header = [
        ["Project Name | LINK", "Month Year - Month Year"]
    ]
    project1_table = Table(project1_header, colWidths=[4*inch, 2.5*inch])
    project1_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(project1_table)
    
    content.append(Paragraph("• Describe the project objective and your role in achieving it", normal_style))
    content.append(Paragraph("• Explain the technologies used and methodologies applied", normal_style))
    content.append(Paragraph("• Highlight the results, accuracy rates, or performance improvements achieved", normal_style))
    content.append(Paragraph("• Mention any specific techniques or innovations you implemented", normal_style))
    content.append(Spacer(1, 8))
    
    project2_header = [
        ["Another Project Name | LINK", "Month Year - Month Year"]
    ]
    project2_table = Table(project2_header, colWidths=[4*inch, 2.5*inch])
    project2_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(project2_table)
    
    content.append(Paragraph("• Brief description of the project and its objectives", normal_style))
    content.append(Paragraph("• Your specific contributions and technical approach", normal_style))
    content.append(Paragraph("• Results achieved and impact of the project", normal_style))
    content.append(Paragraph("• Any challenges overcome or innovations implemented", normal_style))
    content.append(Spacer(1, 12))
    
    # Certificates
    content.append(Paragraph("CERTIFICATES", section_style))
    
    cert1_header = [
        ["Certificate Name | CERTIFICATE", "Month Year"]
    ]
    cert1_table = Table(cert1_header, colWidths=[4*inch, 2.5*inch])
    cert1_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(cert1_table)
    
    content.append(Paragraph("• Key skill or knowledge area covered in the certification", normal_style))
    content.append(Paragraph("• Another important aspect learned through this certification", normal_style))
    content.append(Spacer(1, 8))
    
    cert2_header = [
        ["Another Certificate | CERTIFICATE", "Month Year"]
    ]
    cert2_table = Table(cert2_header, colWidths=[4*inch, 2.5*inch])
    cert2_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    content.append(cert2_table)
    
    content.append(Paragraph("• Description of skills gained from this certification", normal_style))
    content.append(Paragraph("• Practical applications or tools mastered", normal_style))
    
    # Build PDF
    doc.build(content)
    return True

if __name__ == "__main__":
    if create_resume_pdf():
        print("PDF resume created successfully: resume.pdf")
    else:
        print("Could not create PDF. HTML version is available in resume.html")