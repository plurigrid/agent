import wandb
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory, ConversationSummaryMemory, CombinedMemory

conv_memory = ConversationBufferMemory(
    memory_key="chat_history_lines",
    input_key="input"
)

summary_memory = ConversationSummaryMemory(llm=OpenAI(), input_key="input")
# Combined
memory = CombinedMemory(memories=[conv_memory, summary_memory])
_DEFAULT_TEMPLATE = """So it begins and continues...

Summary of conversation:
{history}
Current conversation:
{chat_history_lines}
Human: {input}
AI:
PROMPT = PromptTemplate(
    input_variables=["history", "input", "chat_history_lines"], template=_DEFAULT_TEMPLATE
)
llm = Anthropic()
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=memory,
    prompt=PROMPT
)
"""

PROMPT = PromptTemplate(
    input_variables=["history", "input", "chat_history_lines"], template=_DEFAULT_TEMPLATE
)
llm = OpenAI()
conversation = ConversationChain(
    llm=llm, 
    verbose=True, 
    memory=memory,
    prompt=PROMPT
)

conversation.run("gm")
