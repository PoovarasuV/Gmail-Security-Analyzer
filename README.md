# Gmail Security Analyzer & Exposure Audit Tool

![Project Banner](https://img.shields.io/badge/Status-Completed-green)  

A **Python-based cybersecurity tool** that analyzes a user's Gmail activity (via Google Takeout) to detect suspicious events, generate risk scores, and produce a professional PDF security report.  

This project demonstrates **Cloud Security, Identity & Access Management (IAM), Threat Detection, and Security Reporting**, making it highly relevant for cybersecurity portfolios.

---

## 🔹 Features

1. **Gmail Activity Parser**
   - Reads Gmail Takeout HTML (`MyActivity.html`)  
   - Extracts all email-related events into structured Python objects  

2. **Suspicious Activity Detection**
   - Flags high-frequency Gmail usage  
   - Detects activity at odd hours (late night / early morning)  
   - Generates an overall **risk score** (0–100)  

3. **PDF Security Report**
   - Professional report including:  
     - Risk Score  
     - List of suspicious events  
     - Security recommendations  
   - Recruiter-ready and visually clear  

4. **Modular & Scalable**
   - Separate modules for parsing, detection, and reporting  
   - Easy to extend (e.g., OAuth scanner, cloud apps audit)

---

## 🔹 Tech Stack

- **Python 3.x**  
- **BeautifulSoup4** – HTML parsing  
- **ReportLab** – PDF report generation  
- **OSINT concepts** – Risk analysis & account auditing  
- **Pandas** (optional for future data analytics)

---

## 🔹 Folder Structure

gmail-security-analyzer/
│
├── data/ # ⚠️ Optional: Add sample/dummy Takeout files here
│ └── MyActivity.html
│
├── modules/ 
│ ├── parser.py
│ ├── suspicious_detector.py
│ └── report_generator.py
│
├── main.py # Entry point
├── requirements.txt 
├── README.md 
└── .gitignore 

---

## 🔹 Expected Output
=== FIRST 10 GMAIL ACTIVITIES ===
{'event': 'Opened Gmail'}
{'event': 'Sent Email'}
...

=== SUSPICIOUS ACTIVITY REPORT ===
Suspicious Events:
- High number of Gmail activities detected
Overall Risk Score: 10/100

PDF: Gmail_Security_Report.pdf generated in project root with:

- Risk score

- Suspicious events

- Security recommendations


