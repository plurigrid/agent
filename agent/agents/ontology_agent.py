from langchain import LLMChain
from agent.agents.base_agent import BaseAgent
from langchain.agents import Tool
from agent.config import config
from agent.models.index_model import IndexModel
from langchain.chat_models import ChatOpenAI
from langchain.agents.conversational_chat.base import (
    ConversationalChatAgent,
    AgentOutputParser,
)

from langchain.callbacks.base import AsyncCallbackManager
from langchain.callbacks.base import CallbackManager
from langchain.agents import Tool, AgentExecutor
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from langchain.schema import HumanMessage


class OntologyAgent(BaseAgent):
    def __init__(self, config, mode):
        super().__init__(config, mode)
        self.index_model = IndexModel(config)
        self.index = self.index_model.get_index()
        # self.agent_chain = self.build_agent_streaming(
        #     index
        # )

    def build_agent(self, index):
        print("building agent..")
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        tools = [
            Tool(
                name="knowledge_base",
                func=lambda q: str(index.query(q)),
                description="useful for when you want to answer questions about the knowledge base. The input to this tool should be a complete english sentence.",
                return_direct=False,
            ),
        ]
        llm = ChatOpenAI(
            streaming=True,
            temperature=0,
            # model_name="gpt-4",
        )
        agent = ConversationalChatAgent.from_llm_and_tools(
            llm=llm,
            tools=tools,
            output_parser=AgentOutputParser(),
        )
        return AgentExecutor.from_agent_and_tools(
            agent=agent, tools=tools, verbose=True, memory=memory
        )

    def get_chain(self, streaming_handler):
        print("building agent..")
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        tools = [
            Tool(
                name="knowledge_base",
                func=lambda q: str(self.index.query(q)),
                description="useful for when you want to answer questions about the knowledge base. The input to this tool should be a complete english sentence.",
                return_direct=False,
            ),
        ]
        llm = ChatOpenAI(
            streaming=True,
            temperature=0,
            # model_name="gpt-4",
            callback_manager=AsyncCallbackManager([streaming_handler]),
        )
        agent = ConversationalChatAgent.from_llm_and_tools(
            llm=llm,
            tools=tools,
            output_parser=AgentOutputParser(),
        )
        chain = AgentExecutor.from_agent_and_tools(
            agent=agent,
            tools=tools,
            verbose=True,
            memory=memory,
            manager=AsyncCallbackManager([]),
        )
        self.agent_chain = chain
        return chain

    def handle_input(self, msg):
        return self.agent_chain(msg)


if __name__ == "__main__":
    agent = OntologyAgent(config.Config(), "fastapi")
