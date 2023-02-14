## Agent

This directory contains multiple gpt_index readers -- one for an obsidian vault, and one for the plurigrid knowledge base.

### Obsidian

Make sure you set the OBSIDIAN_VAULT_PATH environment variable to the path to your obsidian vault. Also
ensure that you have the OPENAI_API_KEY environment variable set to your OpenAI API key.

Then, you can run:

```bash
python obsidian.py
```

This will start a repl in which you can ask questions to the agent.

### Plurigrid

Make sure you have the OPENAI_API_KEY environment variable set to your OpenAI API key.

Then, you can run:

```bash
python plurigrid.py
```

This will start a repl in which you can ask questions to the agent.

### Plurigrid zulip bot

Check out plurigrid/python-zulip-api and follow the installation steps here: <https://zulip.com/api/writing-bots>. Also, make sure you
download the bot's rc file as described here: <https://zulip.com/api/running-bots>.

Modify the plurigrid.conf file in the plurigrid bot's subdir to include the right DATA_DIR, INDEX_PATH, and OPENAI_API_KEY variables.

Run, in the root of the repo:

```bash
python3 ./tools/provision
```

Run the venv from the command output.

Then, you can run the bot with:

```bash

zulip-run-bot plurigrid --config-file {path-to-rc-file} --bot-config-file {path-to-plurigrid.conf}
```
