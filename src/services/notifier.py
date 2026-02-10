import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LogNotifier:
  def __init__(self):
    self.slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
  
  def send_slack_alert(self, log_content, ai_analysis):
    """Sends a Slack notification"""

    payload = {
      "blocks" : [
        {
          "type" : "header",
          "text" : {"type" : "plain_text", "text" : "New Laravel Error Detected"}
        },
        {
          "type" : "section",
          "text" : {
            "type" : "mrkdwn",
            "text": f"*Raw Log Entry:*\n`{log_content[:200]}...`"
          }
        },
        {
          "type": "divider"
        },
        {
          "type": "section",
          "text": {
              "type": "mrkdwn",
              "text": f"*💡 AI Analysis & Fix:*\n{ai_analysis}"
          }
        },
        {
          "type": "context",
          "elements": [
              {"type": "mrkdwn", "text": "Sent by *LaravelLogSentinel-AI*"}
          ]
        }
      ]
    }
    
    try:
      response = requests.post(self.slack_webhook_url, json=payload)
      if response.status_code == 200:
        print("Slack notification sent successfully.")
      else:
        print(f"Failed to send Slack notification. Status code: {response.text}")
    except Exception as e:
      print(f"Error sending Slack notification: {str(e)}")

if __name__ == "__main__":
  notifier = LogNotifier()
  notifier.send_slack_alert("Sample log content", "AI analysis and fix")