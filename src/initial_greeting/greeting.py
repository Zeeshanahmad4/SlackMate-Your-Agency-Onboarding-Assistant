# initial_greeting/greeting.py

import requests

def send_welcome_message(user_id, api_token_placeholder):
    """
    Sends a welcome message to a new user.
    Args:
    - user_id (str): The Slack user ID of the new member.
    - api_token_placeholder (str): Placeholder for the Slack API token.
    """
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {api_token_placeholder}"
    }
    payload = {
        "channel": user_id,
        "text": "Welcome to the workspace! :tada:"
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
