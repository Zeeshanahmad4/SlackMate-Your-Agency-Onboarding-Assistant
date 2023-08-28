# project_management_tools_access/pm_tools.py

import requests

def grant_pm_tools_access(user_id, api_token_placeholder):
    """
    Grants access or provides instructions for accessing project management tools.
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
        "text": ("To access our project management tools, please follow the instructions below:\n"
                 "1. Jira: Access via [Jira Link]. Use your company email to login.\n"
                 "2. Asana: You'll receive an invitation email. Follow the steps to join.\n"
                 "3. Trello: Invitation will be sent to your email.\n"
                 "Please complete these steps as part of your onboarding.")
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
