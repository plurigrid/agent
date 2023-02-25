import sys
from langchain import LLMChain, PromptTemplate
from base_agent import BaseAgent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import Tool
from models import aesthetic_model
from config import config
from langchain.agents import ConversationalAgent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from utils import render
from utils import zulip


class PreferenceAgent(BaseAgent):
    def __init__(self, config):
        # super().__init__()
        self.config = config
        self.values = {}
        prefix = """
        You are a friendly agent who is helping users translate their aesthetic preferences into
        HSV (hue, saturation, and color) values. You will guide the user through the process of
        communicating their aesthetic preference and then finalizing their aesthetic. 

        You should talk to the user and prompt them to share their aesthetic preference with you.
        Once they share their aesthetic, use the aesthetic_image tool and make sure you
        pass in the user's aesthetic as a single parameter. The aesthetic_image tool will send the user
        an image that represents their aesthetic. Instruct the user to modify their aesthetic by providing a new one
        if they don't like the image that was generated. Also instruct the user to tell you to finalize
        their aesthetic preference once they are satisfied with it. Always use the aesthetic_image tool 
        to handle any modifications to the user's aesthetic. Don't worry about the linking the user to the
        generated image yourself, the tool will handle that part.

        Once the user tells you that they would like to finalize their aesthetic preference, 
        you must use the aesthetic_finalize tool to finalize their aesthetic. You should always use the aesthetic_finalize tool
        to finalize a user's aesthetic.
        You have the following tools:"""
        suffix = """Begin!"
        {chat_history}
        Question: {input}
        {agent_scratchpad}"""
        self.client = zulip.ZulipClient(config)
        self.aesthetic_model = aesthetic_model.AestheticModel(self.client, config)
        tools = [
            Tool(
                name="aesthetic_image",
                func=self.aesthetic_model.aesthetic_to_image,
                description="useful for when you need to translate a user's aesthetic to an image",
            ),
            Tool(
                name="aesthetic_finalize",
                func=self.aesthetic_model.aesthetic_to_json,
                description="useful for when you need to finalize a user's aesthetic preference",
            ),
        ]
        prompt = ConversationalAgent.create_prompt(
            tools,
            prefix=prefix,
            suffix=suffix,
            input_variables=["input", "chat_history", "agent_scratchpad"],
        )
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
        agent = ConversationalAgent(llm_chain=llm_chain, tools=tools, verbose=True)
        self.agent_chain = AgentExecutor.from_agent_and_tools(
            agent=agent, tools=tools, verbose=True, memory=memory
        )

    def respond_to_message(self, msg):
        stream = msg["stream_id"]
        topic = msg["subject"]
        output = self.agent_chain.run(msg["content"])
        result = self.client.send_message(stream, topic, output)
        print(result)

    def repl(self):
        while True:
            user_input = input(">>> ")
            print(self.agent_chain.run(user_input))

    def handle_message(self):
        print("waiting for messages..")
        self.client.client.call_on_each_message(
            lambda msg: self.respond_to_message(msg)
        )


if __name__ == "__main__":
    agent = PreferenceAgent(config.Config())
    agent.handle_message()
