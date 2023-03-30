from abc import ABC, abstractmethod
from agent.utils import fastapi, gradio, repl, zulip
from agent.utils import discord


class BaseAgent(ABC):
    def __init__(self, config, mode):
        self.mode = mode
        if mode == "zulip":
            self.client = zulip.ZulipClient(self.handle_input)
        elif mode == "discord":
            self.client = discord.DiscordClient(self.handle_input)
        elif mode == "repl":
            self.client = repl.Repl(self.handle_input)
        elif mode == "gradio":
            self.client = gradio.Gradio(self.handle_input)
        elif mode == "fastapi":
            self.client = fastapi.App(self.get_chain)
        else:
            raise ValueError("Invalid agent mode")

    def run(self):
        self.client.run()

    ## Returns LLM output given an input message
    @abstractmethod
    def handle_input(self, msg):
        pass

    ## Returns LLM Chain
    @abstractmethod
    def get_chain(self, msg):
        pass
