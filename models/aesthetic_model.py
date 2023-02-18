from langchain import LLMChain, OpenAI, PromptTemplate
from utils import cosmos

import asyncio


class AestheticModel:
    # This is an LLM which translates an aesthetic into brightness and color values.
    def translate_aesthetic(self, aesthetic):
        template = """
        Take an aesthetic and translate it into an HSV value. Format the response as JSON where there is a different key for each variable:
        hue, saturation, and value. Each value must be an integer. 
        What is a good brightness and color that represents {aesthetic}?
        """
        prompt = PromptTemplate(
            input_variables=["aesthetic"],
            template=template,
        )

        llm = OpenAI(temperature=0.9)
        chain = LLMChain(llm=llm, prompt=prompt)
        output = format_aesthetic_msg(chain.run(aesthetic))
        print(output)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(cosmos.CosmosSDKClient().execute_wasm_msg(output))


def format_aesthetic_msg(msg):
    msg = msg.replace("\n", "")
    return {
        "propose": {
            "msg": {
                "propose": {
                    "title": "propose microworld configuration",
                    "description": f"this is a mock message, will be a real one later: {msg}",
                    "msgs": [],
                }
            }
        }
    }
