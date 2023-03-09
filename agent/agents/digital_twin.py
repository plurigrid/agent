from langchain import LLMChain, PromptTemplate
from base_agent import BaseAgent
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import Tool
from agent.config import config
from langchain.agents import ConversationalAgent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.document_loaders import DirectoryLoader
from langchain.vectorstores import Chroma
from agent.models.index_model import IndexModel
import os
from llama_index import GPTListIndex, GPTIndexMemory


class DigitalTwin(BaseAgent):
    def __init__(self, config):
        super().__init__(config)
        self.index_path = os.path.abspath(
                 os.path.join(os.getcwd(), config.INDEX_PATH)
        )
        # read OPENAI api key from OPENAI_CONFIG_PATH file and set env var
        openai_key_file = os.path.expanduser(config.OPENAI_CONFIG_PATH)
        if os.path.exists(openai_key_file):
             with open(openai_key_file) as f:
                 openai_key = f.read().strip()
                 os.environ['OPENAI_API_KEY'] = openai_key
        
        # Construct index 
        self.index_model = IndexModel(config.DATA_DIR, self.index_path)
        index = self.index_model.get_index()
        self.agent_chain = self.build_agent(index)

    def build_agent(self, index):
        print("building agent..")
        prefix = """
                You are the user's "digital twin". Your role is to help them record their daily intentions in the morning, and summarize their day in the evening.
                When a user says "gm", prompt them to share their intentions for the day. 
                When a user says "gn", prompt them to share what they accomplished that day, as well as any other thoughts or reflections they might have. Then, 
                summarize both what their intention was at the beginning of the day, and what they ended up accomplishing. 
                Let's think step by step.
                Good luck!"""

        suffix = """Begin!"
                {chat_history} 
                {input}
                Answer: 
                {agent_scratchpad}"""
        tools = [
            Tool(
                name="knowledge_base",
                func=lambda q: str(index.query(q)),
                description="useful for when you want to answer questions about the author. The input to this tool should be a complete english sentence.",
                return_direct=True,
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
        agent = ConversationalAgent(llm_chain=llm_chain)
        return AgentExecutor.from_agent_and_tools(
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
    agent.handle_message()
