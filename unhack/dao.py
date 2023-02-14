from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
import gradio as gr

template = "{history}{human_input}"
human_input = ""

prompt = PromptTemplate(input_variables=["history", "human_input"],
                        template=template)

chatgpt_chain = LLMChain(
  llm=OpenAI(temperature=0),
  prompt=prompt,
  verbose=True,
  memory=ConversationalBufferWindowMemory(k=2),
)

def output(input):
  return chatgpt_chain.predict(human_input="what kind of person would say: {input}")

#print(output)

demo = gr.Interface(fn=output, inputs="text", outputs="text")
#demo.launch()   
