import requests
import json
import os

# IBM Watson API credentials (store securely in environment variables)
IBM_WATSON_API_URL = os.getenv("IBM_WATSON_API_URL")
IBM_WATSON_API_KEY = os.getenv("IBM_WATSON_API_KEY")


def generate_response_from_ibm_watson(prompt):
    """
    Sends a prompt to IBM Watson's Granite Model and returns the response.

    Args:
        prompt (str): The text prompt for IBM Watson's AI model.

    Returns:
        str: The AI-generated response.
    """
    if not IBM_WATSON_API_URL or not IBM_WATSON_API_KEY:
        raise ValueError("IBM Watson API credentials are missing.")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {IBM_WATSON_API_KEY}"
    }

    data = json.dumps({"prompt": prompt, "max_tokens": 150})

    try:
        response = requests.post(IBM_WATSON_API_URL, headers=headers, data=data)
        response.raise_for_status()  # Raise error if request fails
        return response.json().get("text", "No response from AI.")
    except requests.exceptions.RequestException as e:
        return f"Error communicating with IBM Watson API: {e}"


def project_analysis_with_ibm_watson(project):
    """
    Generates a project analysis summary using IBM Watson's Granite Model.

    Args:
        project (str): The project details to analyze.

    Returns:
        str: A 3-sentence summary of the project.
    """
    prompt = f"Summarize the project '{project}' in 3 sentences."
    return generate_response_from_ibm_watson(prompt)


def task_creation_with_ibm_watson(project_model, team_member_number):
    """
    Generates a task description for a team member using IBM Watson's Granite Model.

    Args:
        project_model (str): The project model details.
        team_member_number (int): The assigned team member number.

    Returns:
        str: AI-generated task description for the team member.
    """
    prompt = f"Create a task with description for the project '{project_model}' assigned to team member {team_member_number}."
    return generate_response_from_ibm_watson(prompt)
