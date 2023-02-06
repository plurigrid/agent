import requests
import signal

def query_openai_api(message):
    """Query OpenAI API with the given message and return the response."""
    api_key = "YOUR_API_KEY"
    endpoint = "https://api.openai.com/v1/engines/text-davinci/jobs"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": message,
        "max_tokens": 100,
        "temperature": 0.5
    }

    response = requests.post(endpoint, headers=headers, json=data)

    if response.status_code == 200:
        response_text = response.json().get("choices")[0].get("text")
        return response_text
    else:
        return "Sorry, I wasn't able to process your request at this time."

def on_group_message_received(message, group_id):
    """Handle incoming messages in the group thread."""
    if message.startswith("OpenAI: "):
        message = message.replace("OpenAI: ", "", 1)
        response = query_openai_api(message)

        # Send the response back to the group
        signal.send_message(group_id, response)

# Add the Signal client to a group thread
signal.add_group_listener(on_group_message_received)