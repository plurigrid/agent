# Agent
The Agent is a conversational assistant designed to help team members in organizations establish a shared information context and work more efficiently together. The agent is built using Python and langchain.

## Setup 

1. Install [nix](https://nixos.org/download.html#nix-install-macos)

2. To test installation, run `echo $PATH` and ensure `{...}/.nix-profile/bin` is the first element; if not, try `export PATH=$HOME/.nix-profile/bin:$PATH`

3. Make sure you have the nix-pkgs channel set, ie.

```
nix-channel --add https://nixos.org/channels/nixpkgs-unstable
nix-channel --update
```

## Running the agent

1. Run `nix-shell` from the directory where `shell.nix` exists (ie the root of this repo), and you should be dropped into a new shell environment with the necessary dependencies installed.

2. Run `poetry install` to install the python dependencies from pyproject.toml. This will create a virtual environment and install the necessary python dependencies within. 

3. Run `poetry shell`. This will run the virtual environment that was created in the previous step.

4. Set the `OPENAI_API_KEY` environment variable if accessing models by OpenAI.

5. In `agent/config/config.py`, set your DATA_DIR to the directory of files that you want to input to the agent.

6. Run your agent, e.g. `python agent/agents/digital_twin.py`


## Organizational Loops

In its current form, the Agent facilitates a daily "gm --> gn" loop for team members. When a team member says "gm" to the agent, it prompts each team member to share their intentions for the day, starting with the person who initiated the conversation. The agent records each person's response. When a team member says "gn" to the agent, it prompts each team member to share what they accomplished that day, starting with the person who initiated the conversation. The agent records each person's response and can output a work dependency graph based on the data collected.

The agent can also be fed an index based on a user's personal markdown files, and the agent can then be used to query this knowledge.  

## Microworlds

The Agent will be used in the future to generate microworlds, which represent particular simulation contexts for various domains involving a set of coordination strategies, agents, and an environment. Human experts (or automated assurance systems) will validate the outputs of the agents and select which subset of microworlds they have generated are actually valid or safe. The output of this validation process will be used to re-train and fine-tune the agents, making them more effective at what they do.


## Appendix
### Reproducibility
`nix` and `poetry` allow for [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.