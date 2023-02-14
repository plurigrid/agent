import json
from cosmos_sdk import CosmoSdkClient

# Connect to the Juno blockchain
client = CosmoSdkClient(
    f"https://rpc.junonetwork.com"
)

# Prepare the message
message = {
    "contract": "cosmwasm",
    "params": [
        {
            "key": "example_key",
            "value": "example_value"
        }
    ]
}

# Sign the message
signed_message = client.wallet.sign_message(json.dumps(message).encode())

# Broadcast the message
result = client.broadcast_tx_async(signed_message)
print(result)
