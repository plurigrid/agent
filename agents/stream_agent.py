from base_agent import BaseAgent

class StreamAgent(BaseAgent):
    def __init__(self):
        super().__init__()

    def handle_message(self, message):
        # Check if the message is in the right stream
        if message["type"] == "stream" and message["display_recipient"] == Config.ZULIP_STREAM:
            # Respond to the message
            response = {
                "type": "stream",
                "to": message["display_recipient"],
                "subject": message["subject"],
                "content": "Hello, world!",
            }
            self.send_message(response)