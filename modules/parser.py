from bs4 import BeautifulSoup
import os

class GmailActivityParser:
    def __init__(self, data_path):
        self.data_path = data_path

    def parse_html(self, filename="MyActivity.html"):
        file_path = os.path.join(self.data_path, filename)
        if not os.path.exists(file_path):
            print(f"[ERROR] File not found: {file_path}")
            return []

        # Read HTML file
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Extract all text and split by lines
        all_text = soup.get_text(separator="\n")
        lines = all_text.split("\n")

        activities = []

        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            activities.append({
                 "event": line
            })

        return activities
