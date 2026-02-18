from datetime import datetime

class SuspiciousDetector:
    def __init__(self, activities):
        """
        activities: list of dicts
        Each dict: {"event": "Opened Gmail"}
        """
        self.activities = activities
        self.suspicious_events = []

    def detect_rapid_events(self):
        """
        Detect multiple Gmail actions in short time (if timestamps exist)
        Currently placeholder: counts events > 20 as suspicious
        """
        if len(self.activities) > 20:
            self.suspicious_events.append(
                f"High number of Gmail activities detected: {len(self.activities)}"
            )

    def detect_odd_hours(self):
        """
        Detect events at odd hours (12 AM - 5 AM)
        Only works if timestamp exists, skip if not
        """
        for act in self.activities:
            ts = act.get("timestamp")
            if isinstance(ts, datetime):
                hour = ts.hour
                if 0 <= hour <= 5:
                    self.suspicious_events.append(
                        f"Activity during odd hours: {ts} -> {act.get('event')}"
                    )

    def calculate_risk_score(self):
        """
        Assign points for suspicious patterns
        """
        score = 0
        # +10 points for each suspicious event
        score += len(self.suspicious_events) * 10
        # Cap at 100
        if score > 100:
            score = 100
        return score

    def run_detection(self):
        self.detect_rapid_events()
        self.detect_odd_hours()
        risk_score = self.calculate_risk_score()
        return {
            "suspicious_events": self.suspicious_events,
            "risk_score": risk_score
        }
