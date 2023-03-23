from agent.agents.prompt_templates.play_coplay_template import PLAY_COPLAY_PROMPT
from agent.agents.base_agent import BaseAgent
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import Tool
from agent.config import config
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from agent.models.index_model import IndexModel
import gradio
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from agent.models.tasks_json_model import TasksJsonModel


class PlayCoplayAgent(BaseAgent):
    def __init__(self, config, bot_type, prompt=PLAY_COPLAY_PROMPT):
        super().__init__(config, bot_type)
        # Construct index
        # self.index_model = IndexModel(config)
        # index = self.index_model.get_index()
        self.agent_chain = self.build_agent(prompt)

    def build_agent(self, prompt):
        print("building agent..")
        task_model = TasksJsonModel()
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks(name)),
                description="Useful for when you want to load tasks for a user. The input to this tool should be a single english word.",
                return_direct=True,
            ),
        ]
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        llm = ChatOpenAI(temperature=0, model_name="gpt-4")
        agent_kwargs = {"prefix": prompt}
        return initialize_agent(
            tools,
            llm,
            agent="chat-conversational-react-description",
            verbose=True,
            memory=memory,
            agent_kwargs=agent_kwargs,
        )

    def handle_input(self, msg):
        return self.agent_chain.run(msg)

    def repl(self):
        while True:
            user_input = input(">>> ")
            print(self.agent_chain.run(user_input))

    def gradio(self):
        iface = gradio.Interface(
            fn=self.agent_chain.run,
            inputs=gradio.inputs.Textbox(label="question"),
            outputs="text",
            title="Digital Twin",
            description="Ask anything!",
        )
        iface.launch(share=True)


if __name__ == "__main__":
    config = config.Config()
    agent = PlayCoplayAgent(config, "zulip", prompt=PLAY_COPLAY_PROMPT)
    agent.repl()
