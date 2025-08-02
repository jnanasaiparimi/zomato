#!/usr/bin/env python3

import io
import sys

def create_simple_pdf():
    """
    Create a simple PDF-like file using basic text formatting.
    Since we don't have access to PDF libraries, we'll create a formatted text file
    that can be easily converted to PDF later.
    """
    
    resume_content = """
YOUR NAME
LinkedIn: your-linkedin-profile | GitHub: your-github-profile
Email: your.email@example.com | Mobile: +1 234-567-8900
================================================================================

                                   EDUCATION

Your University Name                                      City, Country
Master of Computer Application, GPA: X.XX               Month Year - Month Year

Your College Name                                        City, Country
Bachelor of Science (HONORS) - Your Major, GPA: X.XX   Month Year - Month Year

                                SKILLS SUMMARY

Languages:      Python, Java, JavaScript, SQL, etc.
Frameworks:     React, Node.js, Django, Flask, etc.
Tools:          Git, Docker, AWS, MongoDB, etc.
Platforms:      Linux, Windows, MacOS, Cloud Platforms
Soft Skills:    Leadership, Communication, Problem Solving, Team Collaboration

                               WORK EXPERIENCE

JOB TITLE | COMPANY NAME | LINK                        Month Year - Month Year
• Describe your key achievement or responsibility with quantifiable results
• Another significant contribution you made to the organization
• Third major accomplishment with specific metrics or outcomes
• Additional responsibility that demonstrates your skills and impact

                                  PROJECTS

Project Name | LINK                                     Month Year - Month Year
• Describe the project objective and your role in achieving it
• Explain the technologies used and methodologies applied
• Highlight the results, accuracy rates, or performance improvements achieved
• Mention any specific techniques or innovations you implemented

Another Project Name | LINK                             Month Year - Month Year
• Brief description of the project and its objectives
• Your specific contributions and technical approach
• Results achieved and impact of the project
• Any challenges overcome or innovations implemented

                                CERTIFICATES

Certificate Name | CERTIFICATE                                        Month Year
• Key skill or knowledge area covered in the certification
• Another important aspect learned through this certification

Another Certificate | CERTIFICATE                                     Month Year
• Description of skills gained from this certification
• Practical applications or tools mastered

================================================================================
"""
    
    # Write to a text file that can be easily converted to PDF
    with open('resume.txt', 'w', encoding='utf-8') as f:
        f.write(resume_content)
    
    print("Resume text file created: resume.txt")
    print("You can convert this to PDF using:")
    print("1. Online converters (text to PDF)")
    print("2. Print to PDF from any text editor")
    print("3. Use pandoc if available: pandoc resume.txt -o resume.pdf")
    
    return True

# Try to create a proper PDF using a web-based approach
def create_html_to_pdf():
    """
    Create an HTML file optimized for PDF conversion
    """
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Resume</title>
    <style>
        @page {
            margin: 0.75in;
            size: A4;
        }
        body {
            font-family: Arial, sans-serif;
            font-size: 11pt;
            line-height: 1.3;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            border-bottom: 2px solid #000;
            padding-bottom: 10pt;
            margin-bottom: 15pt;
        }
        .name {
            font-size: 18pt;
            font-weight: bold;
            margin-bottom: 5pt;
        }
        .contact {
            font-size: 10pt;
        }
        .section-title {
            font-size: 12pt;
            font-weight: bold;
            text-align: center;
            margin: 15pt 0 10pt 0;
            letter-spacing: 1pt;
        }
        .item {
            margin-bottom: 10pt;
        }
        .item-header {
            display: flex;
            justify-content: space-between;
            font-weight: bold;
            margin-bottom: 3pt;
        }
        .item-details {
            margin-bottom: 3pt;
        }
        .skills-table {
            width: 100%;
            border-collapse: collapse;
        }
        .skills-table td {
            padding: 2pt 5pt;
            vertical-align: top;
        }
        .skills-table td:first-child {
            font-weight: bold;
            width: 20%;
        }
        ul {
            margin: 0;
            padding-left: 15pt;
        }
        li {
            margin-bottom: 2pt;
        }
        @media print {
            body { print-color-adjust: exact; }
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="name">YOUR NAME</div>
        <div class="contact">
            LinkedIn: your-linkedin-profile | GitHub: your-github-profile<br>
            Email: your.email@example.com | Mobile: +1 234-567-8900
        </div>
    </div>

    <div class="section-title">EDUCATION</div>
    
    <div class="item">
        <div class="item-header">
            <span>Your University Name</span>
            <span>City, Country</span>
        </div>
        <div class="item-details">Master of Computer Application, GPA: X.XX</div>
        <div style="text-align: right; font-size: 10pt;">Month Year - Month Year</div>
    </div>
    
    <div class="item">
        <div class="item-header">
            <span>Your College Name</span>
            <span>City, Country</span>
        </div>
        <div class="item-details">Bachelor of Science (HONORS) - Your Major, GPA: X.XX</div>
        <div style="text-align: right; font-size: 10pt;">Month Year - Month Year</div>
    </div>

    <div class="section-title">SKILLS SUMMARY</div>
    
    <table class="skills-table">
        <tr><td>Languages:</td><td>Python, Java, JavaScript, SQL, etc.</td></tr>
        <tr><td>Frameworks:</td><td>React, Node.js, Django, Flask, etc.</td></tr>
        <tr><td>Tools:</td><td>Git, Docker, AWS, MongoDB, etc.</td></tr>
        <tr><td>Platforms:</td><td>Linux, Windows, MacOS, Cloud Platforms</td></tr>
        <tr><td>Soft Skills:</td><td>Leadership, Communication, Problem Solving, Team Collaboration</td></tr>
    </table>

    <div class="section-title">WORK EXPERIENCE</div>
    
    <div class="item">
        <div class="item-header">
            <span>JOB TITLE | COMPANY NAME | LINK</span>
            <span>Month Year - Month Year</span>
        </div>
        <ul>
            <li>Describe your key achievement or responsibility with quantifiable results</li>
            <li>Another significant contribution you made to the organization</li>
            <li>Third major accomplishment with specific metrics or outcomes</li>
            <li>Additional responsibility that demonstrates your skills and impact</li>
        </ul>
    </div>

    <div class="section-title">PROJECTS</div>
    
    <div class="item">
        <div class="item-header">
            <span>Project Name | LINK</span>
            <span>Month Year - Month Year</span>
        </div>
        <ul>
            <li>Describe the project objective and your role in achieving it</li>
            <li>Explain the technologies used and methodologies applied</li>
            <li>Highlight the results, accuracy rates, or performance improvements achieved</li>
            <li>Mention any specific techniques or innovations you implemented</li>
        </ul>
    </div>
    
    <div class="item">
        <div class="item-header">
            <span>Another Project Name | LINK</span>
            <span>Month Year - Month Year</span>
        </div>
        <ul>
            <li>Brief description of the project and its objectives</li>
            <li>Your specific contributions and technical approach</li>
            <li>Results achieved and impact of the project</li>
            <li>Any challenges overcome or innovations implemented</li>
        </ul>
    </div>

    <div class="section-title">CERTIFICATES</div>
    
    <div class="item">
        <div class="item-header">
            <span>Certificate Name | CERTIFICATE</span>
            <span>Month Year</span>
        </div>
        <ul>
            <li>Key skill or knowledge area covered in the certification</li>
            <li>Another important aspect learned through this certification</li>
        </ul>
    </div>
    
    <div class="item">
        <div class="item-header">
            <span>Another Certificate | CERTIFICATE</span>
            <span>Month Year</span>
        </div>
        <ul>
            <li>Description of skills gained from this certification</li>
            <li>Practical applications or tools mastered</li>
        </ul>
    </div>
</body>
</html>"""
    
    with open('resume_pdf_ready.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("PDF-ready HTML file created: resume_pdf_ready.html")
    print("To convert to PDF:")
    print("1. Open resume_pdf_ready.html in Chrome/Firefox")
    print("2. Press Ctrl+P (or Cmd+P on Mac)")
    print("3. Choose 'Save as PDF' as destination")
    print("4. Set margins to 'Minimum' for best results")
    
    return True

if __name__ == "__main__":
    print("Creating resume files...")
    create_simple_pdf()
    print()
    create_html_to_pdf()
    print("\nResume files created successfully!")