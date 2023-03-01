import sys
from langchain import LLMChain, PromptTemplate
from base_agent import BaseAgent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import Tool
from agent.models import aesthetic_model
from config import config
from langchain.agents import ConversationalAgent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor


class DigitalTwin(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        prefix = """
        You are the user's "digital twin". Your role is to help them record their daily intentions in the morning, and summarize their day in the evening.
        When a user says "gm", prompt them to share their intentions for the day. 
        When a user says "gn", prompt them to share what they accomplished that day, as well as any other thoughts or reflections they might have. Then, 
        summarize both what their intention was at the beginning of the day, and what they ended up accomplishing. 
        Good luck!"""
                
        suffix = """Begin!"
                {chat_history} 
                {input}
                Answer: 
                {agent_scratchpad}"""
        tools = []
        self.values = {}
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

    def repl(self):
        while True:
            user_input = input(">>> ")
            print(self.agent_chain.run(user_input))

    def respond_to_message(self, msg):
            stream = msg["stream_id"]
            topic = msg["subject"]
            output = self.agent_chain.run(msg["content"])
            result = self.client.send_message("stream", stream, topic, output)

if __name__ == "__main__":
    agent = DigitalTwin(config.Config())
    agent.repl()
