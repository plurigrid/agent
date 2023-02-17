# Agent

# Organization
`agents/` Contains task-specific agents that interact with the shared state to perform specific tasks.

`config/` Contains configuration files for the agent and the blockchain.

`models/` Contains conversational large language model interfaces for various tasks the agents might perform.

`utils/` Contains client logic for various services the agent interacts with, such as Zulip and Cosmos SDK.

# Agents
`ValueAgent` This agent elicits the most important personal values of an individual, such as their political ideology, their moral philosophy, and their favorite writers, and summarizes the values for use by other agents downstream.
`CoalitionAgent` This agent forms coalitions by grouping users together in pairings that are most likely to agree to agree based on their elicited values.
`PersuasionAgent` This agent engages in persuasive dialogue with users to convince them to switch coalitions or to adopt a particular stance on a particular issue.
# Configuration

`config.py` This file contains configuration information for the agent, such as the Zulip credentials, the DAO address and key pair, and the entity memory for the LLMChain.
microworld_prompt.json: This file contains a template for the LLMChain to use when prompting users for an aesthetic that needs to be translated into a brightness and color value.
Models

# Models
`ValueModel` This model is used by the ValueAgent to elicit values from users.
`CoalitionModel` This model is used by the CoalitionAgent to form coalitions based on the values elicited by the ValueAgent.
`PersuasionModel` This model is used by the PersuasionAgent to engage in persuasive dialogue with users.
# Utils
`CosmosSdkClient` This client is used to execute transactions on the Cosmos blockchain.
`ZulipClient` This client is used to interact with the Zulip chat service.
