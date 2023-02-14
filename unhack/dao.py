from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
import gradio as gr
import re


template = "{history}{mw_input}"
human_input = ""

mw_prompt = PromptTemplate(input_variables=["history", "mw_input"],
                           template=template)

mw_chain = LLMChain(
  llm=OpenAI(temperature=0),
  prompt=mw_prompt,
  verbose=True,
  memory=ConversationalBufferWindowMemory(k=2),
)

mw_learnings = """
Whenever I say "Microworld Update:" followed by a description of the aesthetic, modify the following message
with the hexadecimal color value and brightness that may best represent the mood and vibes of the specification.
Include specification string itself instead of <specification> into the description field.

{
  "propose": {
    "msg": {
      "propose": {
        "title": "propose microworld configuration",
        "description": "<specification>: \n\n{\n  \"brightness\": 100,\n  \"color\": \"#FF0000\"\n}",
        "msgs": []
      }
    }
  }
}

Please make sure to only edit brightness and color and keep the message structure in tact.

For example:

Input: shadowy supercoder
{
  "propose": {
    "msg": {
      "propose": {
        "title": "propose microworld configuration",
        "description": "shadowy supercoder: \n\n{\n  \"brightness\": 40,\n  \"color\": \"#333333\"\n}",
        "msgs": []
      }
    }
  }
}

Input: luxury space gay communism
{
  "propose": {
    "msg": {
      "propose": {
        "title": "propose microworld configuration",
        "description": "luxury space gay communism: \n\n{\n  \"brightness\": 100,\n  \"color\": \"#C0C0C0\"\n}",
        "msgs": []
      }
    }
  }
}

Thanks!
"""

mw_chain.predict(mw_input=mw_learnings)


def output(human_input):
  print(human_input)
  msg = mw_chain.predict(mw_input="Microworld Update: {}".format(human_input))
  # if needed structurally edit with regex: msg_edited = re.sub("^AI:\s*", "", output)
  print(msg)
  # validate msg CosmWasm and retry automatically until valid
  return msg

#print(output)

demo = gr.Interface(fn=output, inputs="text", outputs="text", input_desc="Microworld vibe")
demo.launch()
