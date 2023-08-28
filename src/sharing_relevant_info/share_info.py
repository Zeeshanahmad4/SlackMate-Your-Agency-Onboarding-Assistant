# sharing_relevant_info/share_info.py

import requests

def share_relevant_info(user_id, api_token_placeholder):
    """
    Shares important information like code repositories, documentation, and team contacts.
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
        "text": ("Here are some important resources you'll need:\n"
                 "1. Code Repositories: [GitHub Link]\n"
                 "2. Documentation: [Confluence/Wiki Link]\n"
                 "3. Team Contact List: [Contact List]\n"
                 "Make sure to go through these as part of your onboarding.")
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
