from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
import gradio as gr
import cosmwasm
import re


template = "{history}{mw_input}"
human_input = ""

mw_prompt = PromptTemplate(input_variables=["history", "mw_input"], template=template)

mw_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=mw_prompt,
    verbose=True,
    memory=ConversationalBufferWindowMemory(k=2),
)

mw_learnings = """
Whenever I say "Microworld Update:" followed by a description of the aesthetic, modify the following message
with the hexadecimal color value and brightness value that may best represent the mood and vibes of the specification.
Include specification string itself instead of <specification> into the title field. The output must be valid JSON.

{
  "propose": {
    "msg": {
      "propose": {
        "title": "<specification>",
        "description": "'brightness': '<brightness-value>', 'color': '<hexadecimal-color-value>'",
        "msgs": []
      }
    }
  }
}

Please make sure to only edit brightness and color and keep the message structure in tact.

For example:

Input: shadowy supercoder
Output: 
{
  "propose": {
    "msg": {
      "propose": {
        "title": "shadowy supercoder",
        "description": "'brightness': 40, color: '#333333'",
        "msgs": []
      }
    }
  }
}

Input: luxury space gay communism
Out
{
  "propose": {
    "msg": {
      "propose": {
        "title": "luxury space gay communism",
        "description": "'brightness': '100', 'color': '#C0C0C0'",
        "msgs": []
      }
    }
  }
}

Thanks!
"""

mw_chain.predict(mw_input=mw_learnings)


async def output(your_microworld_aesthetic):
    print(your_microworld_aesthetic)
    msg = mw_chain.predict(
        mw_input="Microworld Update: {}".format(your_microworld_aesthetic)
    )
    # if needed structurally edit with regex: msg_edited = re.sub("^AI:\s*", "", output)
    print(msg)
    # Retry cosmwasm msg automatically until valid
    try:
        retries = 0
        await cosmwasm.execute_propose_msg(msg)
    except Exception as e:
        print(e)
        print("CosmWasm message not valid, retrying...")
        retries += 1
        if retries < 5:
            await output(your_microworld_aesthetic)
        else:
            print("CosmWasm message not valid, giving up.")
    return (
        "View your proposal here!: https://daodao.zone/dao/juno1jeq3xqkn9kypghjeqjnhsdlnjsltajm8r3s80tem3juxsjlfan3s2kzmsd#proposals\n"
        + msg
    )


demo = gr.Interface(
    fn=output, inputs="text", outputs="text", input_desc="Microworld vibe"
)
demo.launch()
