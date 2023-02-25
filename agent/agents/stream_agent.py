import json
from langchain import OpenAI
from langchain.chains import LLMChain
import config
from prompt_templates import microworld_prompt
from cosmos_sdk_client import CosmosSdkClient
import base64


class StreamAgent(BaseAgent):
    def __init__(self, stream):
        super().__init__()
        self.stream = stream
        self.client = CosmosSdkClient()
        llm = OpenAI(temperature=0)
        self.chain = LLMChain(llm=llm, prompt=microworld_prompt)

    def handle_message(self, message):
        if message["type"] == "stream" and message["display_recipient"] == self.stream:
            text = message["content"].strip()
            if text.startswith("Microworld Update:"):
                aesthetic = text.replace("Microworld Update:", "").strip()
                output = self.chain.run(aesthetic)["output_text"]
                try:
                    # todo: move this to utils
                    wasm_msg = json.loads(output)
                    encoded_wasm_msg = base64.b64encode(
                        json.dumps(wasm_msg).encode()
                    ).decode()
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
                                                        "contract_addr": "%s",
                                                        "funds": [],
                                                        "msg": "%s"
                                                    }
                                                }
                                            }
                                        ]
                                    }
                                }
                            }
                        }
                        """ % (
                        config.DAO_ADDRESS,
                        encoded_wasm_msg,
                    )

                    self.client.send_wasm_message(msg)
                    self.send_message("Microworld configuration successfully proposed!")
                except Exception as e:
                    self.send_message(
                        f"An error occurred while proposing microworld configuration: {e}"
                    )
