from langchain import LLMChain, PromptTemplate
from langchain.agents.mrkl.base import ZeroShotAgent
from agent.agents.prompt_templates.gm_agent_template import PREFIX
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
import gradio


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
        tools = [
            Tool(
                name="knowledge_base",
                func=lambda q: str(index.query(q)),
                description="useful for when you want to answer questions about the author. The input to this tool should be a complete english sentence.",
                return_direct=True,
            ),
        ]
        memory = ConversationBufferMemory(memory_key="chat_history")
        llm=OpenAI(temperature=0)
        agent_kwargs = {'prefix': PREFIX}
        return initialize_agent(tools, llm, agent="conversational-react-description", verbose=True, memory=memory, agent_kwargs=agent_kwargs)

    def respond_to_message(self, msg):
        stream = msg["stream_id"]
        topic = msg["subject"]
        output = self.agent_chain.run(msg["content"])
        result = self.client.send_message("stream", stream, topic, output)
        
    def repl(self):
            while True:
                user_input = input(">>> ")
                print(self.agent_chain.run(user_input))

    def gradio(self):
        iface = gradio.Interface(fn=self.agent_chain.run, 
                             inputs=gradio.inputs.Textbox(label="question"), 
                             outputs="text",
                             title="Digital Twin",
                             description="Ask anything!")
        iface.launch(share = True)

if __name__ == "__main__":
    agent = DigitalTwin(config.Config())
    agent.handle_message()
