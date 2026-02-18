from modules.parser import GmailActivityParser
from modules.suspicious_detector import SuspiciousDetector
from modules.report_generator import PDFReportGenerator

def main():
    # Parse Gmail activity
    parser = GmailActivityParser("data/gmail")
    activities = parser.parse_html("MyActivity.html")

    print("\n=== FIRST 10 GMAIL ACTIVITIES ===")
    for act in activities[:10]:
        print(act)

    # Run Suspicious Activity Detection
    detector = SuspiciousDetector(activities)
    result = detector.run_detection()

    print("\n=== SUSPICIOUS ACTIVITY REPORT ===")
    print("Suspicious Events:")
    for event in result["suspicious_events"]:
        print(f"- {event}")
    print(f"\nOverall Risk Score: {result['risk_score']}/100")
    
    pdf_generator = PDFReportGenerator()
    pdf_generator.generate(result["suspicious_events"], result["risk_score"])

if __name__ == "__main__":
    main()
