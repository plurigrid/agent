import json
from cosmos_sdk.client.lcd import LCDClient
from cosmos_sdk.key.mnemonic import MnemonicKey
from cosmos_sdk.core.wasm import MsgExecuteContract
from cosmos_sdk.client.lcd.api.tx import CreateTxOptions
import os

### Example wasm msg
# wasm_message = {
#     "propose": {
#         "msg": {
#             "propose": {
#                 "title": "propose microworld configuration",
#                 "description": 'this is a mock message, will be a real one later: \n\n{\n"brightness": 100,\n"color": "#FF0000"\n}',
#                 "msgs": [],
#             }
#         }
#     }
# }


async def execute_propose_msg(wasm_msg: dict):
    juno_client = LCDClient(chain_id="juno-1", url="https://lcd-juno.keplr.app")
    mnemonic = os.getenv("MNEMONIC")
    mk = MnemonicKey(mnemonic, "juno")
    wallet = juno_client.wallet(mk)

    data = {
        "contract": "juno177zg5chuaxelxhr7qjzgjrvhm75c042xtme564d3mf7g3928pydq3x8lku",
        "sender": wallet.key.acc_address,
        "msg": wasm_msg,
        "funds": [],
    }

    execute_msg = MsgExecuteContract.from_data(data)
    create_tx_options = CreateTxOptions(
        msgs=[execute_msg],
    )

    # Sign and Broadcast the transaction
    tx = wallet.create_and_sign_tx(create_tx_options)
    result = wallet.lcd.tx.broadcast(tx)
    print(result)
