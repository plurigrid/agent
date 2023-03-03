from abc import ABC, abstractmethod
from agent.utils import zulip

class BaseAgent(ABC):
    def __init__(self, config):
        self.client = zulip.ZulipClient(config)

    def handle_message(self):
        print("waiting for messages..")
        self.client.client.call_on_each_message(
            lambda msg: self.respond_to_message(msg)
        )
    
    @abstractmethod
    def respond_to_message(self, msg):
        pass