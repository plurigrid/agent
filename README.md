# Agent


## Setup and Installation

1. Install [nix](https://nixos.org/download.html#nix-install-macos)

2. To test installation, run `echo $PATH` and ensure `{...}/.nix-profile/bin` is the first element; if not, try `export PATH=$HOME/.nix-profile/bin:$PATH`

3. Make sure you have the nix-pkgs channel set, ie.

```
nix-channel --add https://nixos.org/channels/nixpkgs-unstable
nix-channel --update
```

## Running with 'just'

1. If it's the first time running after pulling changes, run "just install" to install all dependencies.
2. Set the OPENAI_API_KEY environment variable in your shell.
<<<<<<< HEAD
3. For the play-coplay agent, run `just play {gradio, repl, zulip, discord}`. (This will start nix and poetry shell and the agent for you.)
4. To summon a digital twin, run `just summon {bartonus, ianita, luke, agatha, andreus} {gradio, repl}`.
5. To start an ontology agent, run `just ontology {gradio, repl}`. This will load the digital twin from the prompt you input, and it can also answer questions over the knowledge base you provide. Protip: make sure the knowledge base does not have nested directories. scripts/copy_files_flat.sh can help with this.
=======
3. Run `just shell` to run the nix and poetry shells.
4. For the play-coplay agent, run `just play {gradio, repl, zulip, discord}`. Default mode if you don't provide one will create a link to a gradio UI.
5. To summon a twin with a prompt, run `just summon <prompt-file-path> {gradio, repl, zulip, discord}`.
6. To start an ontology agent, run `just ontology <path-to-knowledge-base> {gradio, repl, zulip, discord}`. This will allow you to ask questions over the knowledge base you provide. Protip: make sure the knowledge base does not have nested directories. scripts/copy_files_flat.sh can help with this.
>>>>>>> main

## Extra configuration for running in zulip or discord

1. The agent_config.json file in this directory is a sample configuration file. Copy it to ~/agent_config.json.

<<<<<<< HEAD
2. If you want to the agent's index to be constructed from channels on a discord server, add the relevant discord channel IDs to the `CHANNEL_IDS` variable in agent_config.json. Make sure you set the INDEX_MODE variable to either "discord" or "directory". In order for the channels to be read, you need to set the `DISCORD_TOKEN` environment variable to your discord bot's API key.

3. If running a zulip agent, you will also need a zulip bot API key. Go to Zulip and navigate to 'Settings' --> 'Personal Settings' --> 'Bots'. Download the .zuliprc file and copy it to ~/.zuliprc.

4. If running in discord, you will need to set the `DISCORD_TOKEN` environment variable to your bot's API key.

=======
2. DISCORD: If you want to the agent's index to be constructed from channels on a discord server, add the relevant discord channel IDs to the `CHANNEL_IDS` variable in agent_config.json. Make sure you set the INDEX_MODE variable to either "discord" or "directory". In order for the channels to be read, you need to set the `DISCORD_TOKEN` environment variable to your discord bot's API key. If you're otherwise running as a discord bot, you also need to set the `DISCORD_TOKEN` environment variable to your bot's API key.

3. ZULIP: If running a zulip agent, you will also need a zulip config file. Go to Zulip and navigate to 'Settings' --> 'Personal Settings' --> 'Bots'. Download the .zuliprc file and copy it to ~/.zuliprc.

>>>>>>> main

## Tips

- To exit the poetry shell, type `exit`
- To exit the nix shell, use `Ctrl + d`
- If you need to reinstantiate your env, do `poetry env list` and then paste the outputted env into `poetry env remove {env-name}`. Then, run `poetry install` and `poetry shell` again to instantiate a new env.

## Appendix

### Reproducibility

`nix` and `poetry` allow for [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.
