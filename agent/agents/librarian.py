import os
from pathlib import Path
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.agents import initialize_agent
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from agent.agents.base_agent import BaseAgent
from agent.config import config
from llama_index import LlamaIndex
from gpt_index import download_loader

PDFReader = download_loader("PDFReader")
loader = PDFReader()


class Librarian(BaseAgent, PromptTemplate):
    def __init__(self, config, bot_type, prompt):
        super().__init__(config, bot_type)

        # Construct index
        self.llama_index = LlamaIndex()

        # Load data into index
        self.load_data_to_index()

        index = self.llama_index.get_index()
        self.agent_chain = self.build_agent(index, prompt)

    def load_data_to_index(self):
        # Define the paths for books, reviews, and critical theory data
        paths = [
            Path("./books/"),
            Path("./reviews/"),
            Path("./critical_theory/"),
        ]

        # Load data from PDF files in the paths
        for path in paths:
            for file in path.iterdir():
                if file.is_file() and file.suffix.lower() == ".pdf":
                    documents = loader.load_data(file=file)
                    self.llama_index.add_documents(documents)

    def build_agent(self, index, prompt):
        tools = [
            Tool(
                name="knowledge_base",
                func=lambda q: str(index.query(q)),
                description="useful for when you want to answer questions about the author. The input to this tool should be a complete english sentence.",
                return_direct=True,
            ),
        ]
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm = OpenAI(temperature=0)
        agent_kwargs = {"prefix": prompt}
        return initialize_agent(
            tools,
            llm,
            agent="conversational-react-description",
            verbose=True,
            memory=memory,
            agent_kwargs=agent_kwargs,
        )

    def __call__(self, message):
        return self.process_message(message.content)

    def process_message(self, msg):
        return self.agent_chain.run(msg)


librarian_agent = Librarian(config, "librarian", "Your prompt here")

# Initialize the ChatOpenAI and LLMChain
chat = ChatOpenAI(temperature=0)
chain = LLMChain([librarian_agent, chat])

# Send a message to the LLMChain
response = chain([HumanMessage(content="Translate this sentence from English to French. I love programming.")])
print(response)
