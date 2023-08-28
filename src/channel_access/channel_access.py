# channel_access/channel_access.py

import requests

def grant_channel_access(user_id, role, api_token_placeholder):
    """
    Grants access to relevant Slack channels based on the member's role.
    Args:
    - user_id (str): The Slack user ID of the new member.
    - role (str): The role or department of the new member.
    - api_token_placeholder (str): Placeholder for the Slack API token.
    """
    url = "https://slack.com/api/conversations.invite"
    headers = {
        "Authorization": f"Bearer {api_token_placeholder}"
    }
    
    # Define channel IDs for different roles
    channel_ids = {
        "developer": "C1234567890",
        "designer": "C0987654321",
        "hr": "C1122334455"
    }
    
    payload = {
        "channel": channel_ids.get(role, "C0000000000"),
        "users": user_id
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
