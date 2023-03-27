from langchain import PromptTemplate
from agent.agents.prompt_templates.play_coplay_template import (
    PLAY_COPLAY_PROMPT_PREFIX,
    PLAY_COPLAY_PROMPT_SUFFIX,
)
from agent.agents.base_agent import BaseAgent
from langchain.agents.chat.base import ChatAgent
from langchain.agents.conversational_chat.base import (
    ConversationalChatAgent,
    AgentOutputParser,
)
from langchain.agents import Tool, AgentExecutor
from langchain.chains import LLMChain
from langchain.agents import Tool
from agent.config import config
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
import gradio
from agent.models.tasks_json_model import TasksJsonModel


class PlayCoplayAgent(BaseAgent):
    def __init__(self, config, bot_type):
        super().__init__(config, bot_type)
        self.agent_chain = self.build_agent()

    def build_agent(self):
        task_model = TasksJsonModel()
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks(name)),
                description="Useful for when you want to load tasks for a player. The input to this tool should be a single english word.",
                return_direct=True,
            ),
        ]
        tool_names = [tool.name for tool in tools]
        prompt = ConversationalChatAgent.create_prompt(
            system_message=PLAY_COPLAY_PROMPT_PREFIX,
            human_message=PLAY_COPLAY_PROMPT_SUFFIX,
            tools=tools,
        )

        llm_chain = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name="gpt-4"), prompt=prompt
        )

        agent = ConversationalChatAgent(
            llm_chain=llm_chain,
            allowed_tools=tool_names,
            output_parser=AgentOutputParser(),
        )
        return AgentExecutor.from_agent_and_tools(
            agent=agent, tools=tools, verbose=True, memory=memory
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
            inputs=gradio.inputs.Textbox(label="..."),
            outputs="text",
            title="Play-Coplay Agent",
            description="GM!",
        )
        iface.launch(share=True)


if __name__ == "__main__":
    config = config.Config()
    agent = PlayCoplayAgent(config, "zulip")
    agent.repl()
