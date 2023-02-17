from cosmos_sdk.client.lcd import LCDClient
from cosmos_sdk.key.mnemonic import MnemonicKey
from cosmos_sdk.core.wasm import MsgExecuteContract
from cosmos_sdk.client.lcd.api.tx import CreateTxOptions
from config import Config


class CosmosSDKClient:
    def __init__(self):
        self.chain_id = Config.CHAIN_ID
        self.lcd_url = Config.LCD_URL
        self.mnemonic = Config.MNEMONIC
        self.contract_address = Config.CONTRACT_ADDRESS
        self.wallet = None
        self.juno_client = None

    def connect(self):
        self.juno_client = LCDClient(chain_id=self.chain_id, url=self.lcd_url)
        mk = MnemonicKey(self.mnemonic, "juno")
        self.wallet = self.juno_client.wallet(mk)

    async def execute_wasm_msg(self, wasm_msg: dict):
        if not self.wallet:
            self.connect()

        data = {
            "contract": self.contract_address,
            "sender": self.wallet.key.acc_address,
            "msg": wasm_msg,
            "funds": [],
        }

        execute_msg = MsgExecuteContract.from_data(data)
        create_tx_options = CreateTxOptions(
            msgs=[execute_msg],
        )

        # Sign and Broadcast the transaction
        tx = self.wallet.create_and_sign_tx(create_tx_options)
        result = self.wallet.lcd.tx.broadcast(tx)
        print(result)
