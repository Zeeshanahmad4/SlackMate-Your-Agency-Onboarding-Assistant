# onboarding_guidance/guidance.py

import requests

def send_onboarding_guidance(user_id, api_token_placeholder):
    """
    Sends onboarding guidance to a new user.
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
        "text": ("Here are the steps for your onboarding:\n"
                 "1. Complete HR documentation.\n"
                 "2. Set up your development environment.\n"
                 "3. Go through the following tutorials: [Link]\n"
                 "4. Read the FAQs: [Link]\n"
                 "5. Meet your team.\n"
                 "If you have any questions, feel free to ask!")
    }
    
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

