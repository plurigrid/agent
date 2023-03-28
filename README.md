# Agent

The Agent is a conversational assistant designed to help team members in organizations establish a shared information context and work more efficiently together. The agent is built using Python and langchain.


## Setup and Installation

1. Install [nix](https://nixos.org/download.html#nix-install-macos)

2. To test installation, run `echo $PATH` and ensure `{...}/.nix-profile/bin` is the first element; if not, try `export PATH=$HOME/.nix-profile/bin:$PATH`

3. Make sure you have the nix-pkgs channel set, ie.

```
nix-channel --add https://nixos.org/channels/nixpkgs-unstable
nix-channel --update
```

## Easiest: Running the agent with 'just'

1. If it's the first time running after pulling changes, run "just install" to install all dependencies.
2. Then, run "just play {gradio, repl}" to start the agent.

## Running the agent as a zulip or discord bot

1. Set the OPENAI_API_KEY environment variable in your shell.

2. The agent_config.json file in this directory is a sample configuration file. Copy it to ~/agent_config.json (aka, your home directory) and set the DATA_DIR variable in that file to the absolute path of the directory of files that you want to input to the agent. This should be a directory containing any notes or thoughts you have about Plurigrid. Don't include any nested directories, all files should be at the top level. (# NOTE: THIS WILL SOON BE AUGMENTED WITH SUMMONING SPELLS)

3. If you instead want to the agent's index to be constructed from channels on a discord server, add the relevant discord channel IDs to the `CHANNEL_IDS` variable in agent_config.json. Make sure you set the INDEX_MODE variable to either "discord" or "directory". In order for the channels to be read, you need to set the `DISCORD_TOKEN` environment variable to your discord bot's API key.

5. If running a zulip bot, you will also need a zulip bot API key. You already have a bot created for you, so go to Zulip and navigate to 'Settings' --> 'Personal Settings' --> 'Bots'. Download the zuliprc file. Copy the api key and use it to set the `ZULIP_API_KEY` environment variable in your shell. Then, in ~/agent_config.json, set the BOT_EMAIL variable to your bot's email address. Set the SERVER_URL variable to the zulip server url. (This is because you are trying to separate API keys from other text configurations.)

5.5. If running a discord bot, you will need to set the `DISCORD_TOKEN` environment variable to your bot's API key.

7. Run your agent and indicate which mode you want: `just play {repl, gradio, zulip, discord}`. Make sure you run this command from the root of the repo.


## Tips

- To exit the poetry shell, type `exit`
- To exit the nix shell, use `Ctrl + d`
- If you need to reinstantiate your env, do `poetry env list` and then paste the outputted env into `poetry env remove {env-name}`. Then, run `poetry install` and `poetry shell` again to instantiate a new env.

## Appendix

### Reproducibility

`nix` and `poetry` allow for [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.
