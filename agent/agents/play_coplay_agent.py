from agent.agents.prompt_templates.play_coplay_template import PLAY_COPLAY_PROMPT
from agent.agents.base_agent import BaseAgent
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import Tool
from agent.config import config
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from agent.models.index_model import IndexModel
import gradio

from agent.models.tasks_json_model import TasksJsonModel


class PlayCoplayAgent(BaseAgent):
    def __init__(self, config, bot_type, prompt=PLAY_COPLAY_PROMPT):
        super().__init__(config, bot_type)
        # Construct index
        self.index_model = IndexModel(config)
        index = self.index_model.get_index()
        self.agent_chain = self.build_agent(index, prompt)

    def build_agent(self, index, prompt):
        print("building agent..")
        task_model = TasksJsonModel()
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks_for_name(name)),
                description="Useful for when you want to load tasks for a user. The input to this tool should be a user's name.",
                return_direct=True,
            ),
            Tool(
                name="",
                func=lambda q: str(index.query(q)),
                description="Useful for when you want to answer questions about open games, play, and coplay. The input to this tool should be a complete english sentence.",
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
