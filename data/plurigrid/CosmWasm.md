https://cosmwasm.tools

Interacting with CosmWasm contracts is done using message-passing. The 3 broad types of messages are:


**Instantiate**
The stage at which you use an existing wasm Code ID to create a new instance of a contract and configure it.

**Execute**
Runs a corresponding piece of CosmWasm code to calculate and propose a state transition.

**Query**
Checks the current state of contract on-chain.

Example:
https://github.com/wasmswap/wasmswap-contracts
https://www.mintscan.io/juno/wasm/code/16
juno124d0zymrkdxv72ccyuqrquur8dkesmxmx2unfn7dej95yqx5yn8s70x3yj

Instantiate message:
```
{
  "token1_denom": {
    "native": "ujuno"
  },
  "token2_denom": {
    "cw20": "juno15u3dt79t6sxxa3x3kpkhzsy56edaa5a66wvt3kxmukqjz2sx0hes5sn38g"
  },
  "lp_token_code_id": 1
}
```

Info:

```
junod query wasm contract-state smart "juno124d0zymrkdxv72ccyuqrquur8dkesmxmx2unfn7dej95yqx5yn8s70x3yj" '{"info":{}}'
data:
  lp_token_address: juno1u57ju64c5qdmkrjgch2e3amutpjqrez6cq0jp7h2pytuthpfns7s4jln57
  lp_token_supply: "1405250993232"
  token1_denom:
    native: ujuno
  token1_reserve: "557389307135"
  token2_denom:
    cw20: juno15u3dt79t6sxxa3x3kpkhzsy56edaa5a66wvt3kxmukqjz2sx0hes5sn38g
  token2_reserve: "83159437615010"
```


