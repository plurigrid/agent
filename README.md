# Agent

The Agent is a conversational assistant designed to help team members in organizations establish a shared information context and work more efficiently together. The agent is built using Python and the Langchain library.

## Organizational Loops

In its current form, the Agent facilitates a daily "gm --> gn" loop for team members. When a team member says "gm" to the agent, it prompts each team member to share their intentions for the day, starting with the person who initiated the conversation. The agent records each person's response. When a team member says "gn" to the agent, it prompts each team member to share what they accomplished that day, starting with the person who initiated the conversation. The agent records each person's response and can output a work dependency graph based on the data collected.

## Microworlds

The Agent will be used in the future to generate microworlds, which represent particular simulation contexts for various domains involving a set of coordination strategies, agents, and an environment. Human experts (or automated assurance systems) will validate the outputs of the agents and select which subset of microworlds they have generated are actually valid or safe. The output of this validation process will be used to re-train and fine-tune the agents, making them more effective at what they do.

## Conclusion

The Agent is a powerful tool for improving communication and collaboration among team members, generating valuable insights and data about organizations and their operations, and supporting the creation of safe and effective microworlds. By using prompts to initiate and record conversations with team members, the Agent helps establish a shared information context for organizations. By collecting and managing data, the Agent can output a work dependency graph to help team members better synthesize information about what the organization is, what others within the organization are working on, and how all of these elements compose together.