# src/main.py
import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from initial_greeting.greeting import send_welcome_message
from onboarding_guidance.guidance import send_onboarding_guidance
from project_management_tools_access.pm_tools import grant_pm_tools_access
from sharing_relevant_info.share_info import share_relevant_info
from channel_access.channel_access import grant_channel_access

# Initialize Slack bot
client = WebClient(token=os.environ['SLACK_API_TOKEN'])

def listen_for_events():
    """
    Listens for events from Slack's RTM API and triggers appropriate actions.
    """
    while True:
        events = client.rtm_read()
        
        for event in events:
            if event["type"] == "member_joined_channel":
                user_id = event["user"]
                role = "developer"  # Placeholder, would typically fetch this from a database or another source

                send_welcome_message(user_id, os.environ['SLACK_API_TOKEN'])
                send_onboarding_guidance(user_id, os.environ['SLACK_API_TOKEN'])
                grant_pm_tools_access(user_id, os.environ['SLACK_API_TOKEN'])
                share_relevant_info(user_id, os.environ['SLACK_API_TOKEN'])
                grant_channel_access(user_id, role, os.environ['SLACK_API_TOKEN'])
        
        time.sleep(1)

if __name__ == "__main__":
    listen_for_events()
