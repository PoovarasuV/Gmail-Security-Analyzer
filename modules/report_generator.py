from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

class PDFReportGenerator:
    def __init__(self, filename="Gmail_Security_Report.pdf"):
        self.filename = filename

    def generate(self, suspicious_events, risk_score):
        c = canvas.Canvas(self.filename, pagesize=A4)
        width, height = A4

        # Title
        c.setFont("Helvetica-Bold", 20)
        c.drawCentredString(width / 2, height - 50, "Gmail Security Report")

        # Date
        c.setFont("Helvetica", 12)
        c.drawString(50, height - 80, f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Risk Score
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, height - 120, f"Overall Risk Score: {risk_score}/100")

        # Suspicious Events
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, height - 160, "Suspicious Events:")
        c.setFont("Helvetica", 12)
        y = height - 180
        if not suspicious_events:
            c.drawString(60, y, "No suspicious events detected.")
        else:
            for event in suspicious_events:
                c.drawString(60, y, f"- {event}")
                y -= 20
                if y < 50:  # New page if space runs out
                    c.showPage()
                    y = height - 50

        # Recommendations
        y -= 30
        c.setFont("Helvetica-Bold", 14)
        c.drawString(50, y, "Recommendations:")
        c.setFont("Helvetica", 12)
        y -= 20
        recommendations = [
            "Review your account login history regularly.",
            "Enable 2-Factor Authentication (2FA) if not already enabled.",
            "Remove unnecessary third-party app access.",
            "Change passwords that are reused or weak."
        ]
        for rec in recommendations:
            c.drawString(60, y, f"- {rec}")
            y -= 20
            if y < 50:
                c.showPage()
                y = height - 50

        c.save()
        print(f"[SUCCESS] PDF report generated: {self.filename}")
