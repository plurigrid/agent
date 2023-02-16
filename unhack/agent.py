from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
from langchain.chains.conversation.memory import ConversationalBufferWindowMemory
import gradio as gr
import cosmwasm
import re
from plurigrid import PlurigridOlog #, topics

# depending on where we come from, we load the memory of the appropriate chatbot
# we know which <topic> - 0,1,..,9 - derives actual config from file
# topics = {"0": "p0.json", "1": "p1.json"}
# start 9 instances for each coalition's Plurigrid

p = PlurigridOlog("p0.json", "<dao_address>", "<agent_address>")
# p1 ...
member_username = "plurality@plurigrid.art"
dao = p.dao_address
member = "juno1337133713371337133713371337"
#member = members[member_username]

add_member_learnings = """
Whenever I say things like:

- include juno9000 into DAO
- add to Plurigrid juno9000
- + juno9000 to DAO
- juno9000 add plzzzz

and similar things, where "juno9000" is the address of the member to be added,
I want to get the following:
add_members_msg = {
     "update_members": {
        "add": [{"weight": 1, "addr": "<addr>"}],
         "remove": [],
     }
}
"""

add_member_prompt = PromptTemplate(input_variables=[],
                                   template=add_member_learnings)

add_member_chain = LLMChain(
    llm=OpenAI(temperature=0),
    prompt=add_member_prompt,
    verbose=True,
    memory=ConversationalBufferWindowMemory(k=2),
)

def process_response_to_msg(llm_response):
    llm_response = add_member_chain.predict(add_member_input=add_member_learnings)
    response_bytes = response.encode('ascii')
    base64_bytes = base64.b64encode(response_bytes)
    base64_response = base64_bytes.decode('ascii')

    msg = """
    {
        "propose": {
            "msg": {
                "propose": {
                    "title": "Add member to a DAO",
                    "description": "Adding a new member",
                    "msgs": [
                        {
                            "wasm": {
                                "execute": {
                                    "contract_addr": "{%s}",
                                    "funds": [],
                                    "msg": "{%s}"
                                }
                            }
                        }
                    ]
                }
            }
        }
    }
    """ % (dao, base64_response)

# template = "{history}{mw_input}"



#human_input = ""

#mw_prompt = PromptTemplate(input_variables=["history", "mw_input"], template=template)

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

# mw_chain.predict(mw_input=mw_learnings)


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


def chattwat(bird):
    process_response_to_msg(bird)


chatui = gr.Interface(
    fn=chattwat,
    inputs=gr.inputs.Textbox(lines=3, label="e-gen:"),
    outputs=gr.outputs.Textbox(label="Plurigrid #0")
)

chatui.launch()
