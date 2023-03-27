from langchain import PromptTemplate
from agent.agents.prompt_templates.play_coplay_template import (
    CHAT_PROMPT,
    PLAY_COPLAY_PROMPT_PREFIX,
)
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from agent.agents.base_agent import BaseAgent
from langchain.agents.chat.base import ChatAgent
from langchain.agents.conversational_chat.base import (
    ConversationalChatAgent,
    AgentOutputParser,
)
from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.agents import Tool, initialize_agent
from agent.config import config
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from agent.models.index_model import IndexModel
import gradio
from agent.models.tasks_json_model import TasksJsonModel


class PlayCoplayAgent(BaseAgent):
    def __init__(self, config, bot_type, prompt=PLAY_COPLAY_PROMPT_PREFIX):
        super().__init__(config, bot_type)
        # Construct index
        # self.index_model = IndexModel(config)
        # index = self.index_model.get_index()
        # self.agent_chain = self.build_agent_2()
        # self.agent_chain = self.build_agent_3()
        # self.agent_chain = self.langchain_example()
        self.agent_chain = self.build_agent_4(prompt)

    # doesn't work because prompt template is not right format
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
        llm = ChatOpenAI(temperature=0.2, model_name="gpt-4")
        chain = LLMChain(llm=llm, prompt=PLAY_COPLAY_PROMPT_PREFIX)
        tool_names = [tool.name for tool in tools]
        agent = ChatAgent(llm_chain=chain, allowed_tools=tool_names)
        return AgentExecutor.from_agent_and_tools(
            agent=agent, tools=tools, verbose=True, memory=memory
        )

    # doesn't work because gpt-4 does not get the prompt
    # it doesn't get the prompt because "prefix" is the wrong kwarg, it should be "system_message". If you change that, this
    # way will also be correct
    def build_agent_2(self):
        task_model = TasksJsonModel()
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        llm = ChatOpenAI(temperature=0, model="gpt-4")
        agent_kwargs = {"prefix": PLAY_COPLAY_PROMPT_PREFIX}
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks(name)),
                description="Useful for when you want to load tasks for a user. The input to this tool should be a single english word.",
                return_direct=True,
            ),
        ]
        return initialize_agent(
            tools,
            llm,
            agent="chat-conversational-react-description",
            verbose=True,
            memory=memory,
            agent_kwargs=agent_kwargs,
        )

    # this one runs but fails on the first query because the returned format is not as expected
    # debugging
    # to fix this one, we need to use the prompt template, ie ConversationalChatAgent.create_prompt
    def build_agent_3(self):
        task_model = TasksJsonModel()
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        llm_chain = LLMChain(
            llm=ChatOpenAI(temperature=0, model_name="gpt-4"), prompt=CHAT_PROMPT
        )
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks(name)),
                description="Useful for when you want to load tasks for a user. The input to this tool should be a single english word.",
                return_direct=True,
            ),
        ]
        tool_names = [tool.name for tool in tools]
        # wrong - we should use ConversationalChatAGent
        agent = ChatAgent(llm_chain=llm_chain, allowed_tools=tool_names)
        return AgentExecutor.from_agent_and_tools(
            agent=agent, tools=tools, verbose=True, memory=memory
        )

    def langchain_example(self):
        human_message_prompt = HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                template="What is a good name for a company that makes {product}?",
                input_variables=["product"],
            )
        )
        chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])
        chat = ChatOpenAI(temperature=0.9)
        return LLMChain(llm=chat, prompt=chat_prompt_template)

    # this one will be the correct one
    def build_agent_4(self, prompt):
        task_model = TasksJsonModel()
        memory = ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        )
        tools = [
            Tool(
                name="tasks_json_loader",
                func=lambda name: str(task_model.get_tasks(name)),
                description="Useful for when you want to load tasks for a user. The input to this tool should be a single english word.",
                return_direct=True,
            ),
        ]
        tool_names = [tool.name for tool in tools]
        prompt = ConversationalChatAgent.create_prompt(
            system_message=prompt, tools=tools
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
            inputs=gradio.inputs.Textbox(label="question"),
            outputs="text",
            title="Digital Twin",
            description="Ask anything!",
        )
        iface.launch(share=True)


if __name__ == "__main__":
    config = config.Config()
    agent = PlayCoplayAgent(config, "zulip", prompt=PLAY_COPLAY_PROMPT_PREFIX)
    agent.repl()
