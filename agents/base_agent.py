from abc import ABC, abstractmethod
from zulip import Client
from config import Config

class BaseAgent(ABC):
    def __init__(self):
        self.client = Client(config_file="zuliprc", client="MyApp/1.0")

    def send_message(self, message):
        self.client.send_message(message)

    @abstractmethod
    def handle_message(self, message):
        pass

    def run(self):
        last_event_id = -1
        while True:
            # Get the most recent events from the Zulip server
            events = self.client.get_events(
                queue_id=None,
                last_event_id=last_event_id,
                dont_block=True,
            )

            # Handle each event
            for event in events["events"]:
                last_event_id = max(last_event_id, int(event["id"]))
                if event["type"] == "message":
                    self.handle_message(event["message"])