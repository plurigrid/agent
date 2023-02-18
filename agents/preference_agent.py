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


class PreferenceAgent(BaseAgent):
    def __init__(self, config):
        # super().__init__()
        self.config = config
        self.values = {}
        prefix = """I want you to talk to the user and prompt them to share their aesthetics with you.
        Once they share their aesthetic, use the aesthetic_chain tool and make sure you
        pass in the user's aesthetic as a single parameter. 
        You have the following tools:"""
        suffix = """Begin!"
        {chat_history}
        Question: {input}
        {agent_scratchpad}"""
        tools = [
            Tool(
                name="aesthetic_chain",
                func=aesthetic_model.AestheticModel().translate_aesthetic,
                description="useful for when you need to describe an aesthetic",
            )
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

    def run(self):
        while True:
            user_input = input(">>> ")
            print(self.agent_chain.run(user_input))

    def handle_message(self, message):
        if message["content"] == "GM" or message["content"] == "GM":
            # Send a DM to the user to start value elicitation
            self.client.send_message(
                {
                    "type": "private",
                    "to": message["sender_email"],
                    "content": "Hello! I'm the preference elicitation agent. Can you tell me a bit about your lamp aesthetics?",
                }
            )
        else:
            # Parse the message and update the user's values
            # Assumes messages will be of the format "key: value"
            key, value = message["content"].split(":")
            self.values[key.strip()] = value.strip()

            # Send a confirmation message to the user
            self.client.send_message(
                {
                    "type": "private",
                    "to": message["sender_email"],
                    "content": f"Thanks for sharing! I've updated your {key.strip()} value to {value.strip()}.",
                }
            )


if __name__ == "__main__":
    agent = PreferenceAgent(config.Config())
    agent.run()
