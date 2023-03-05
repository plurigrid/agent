# Agent
The Agent is a conversational assistant designed to help team members in organizations establish a shared information context and work more efficiently together. The agent is built using Python and the Langchain library.
## Using `just`
`just shell`
## Manually
0. Clone this repo
1. Install [nix](https://nixos.org/download.html#nix-install-macos)
To test installation:
1.1 run `echo $PATH` and ensure `{...}/.nix-profile/bin` is the first element; if not, try `export PATH=$HOME/.nix-profile/bin:$PATH`
1.2 create `shell.nix`:
```
{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  buildInputs = with pkgs; [
    sl
    wget
  ];
}
```
1.2 if you run `nix-shell` from the directory where `shell.nix` exists, you should be dropped into a new shell and now have `sl` and `wget` binaries which you can test by running
2. Run `poetry update`
3. Run `poetry shell` inside `agent/agent`
4. ??? (e.g. `python <...>`)
5. PROFIT!11!!!


## Running it
Set `OPENAI_API_KEY` environment varibale if accessing models by OpenAI.

## Organizational Loops

In its current form, the Agent facilitates a daily "gm --> gn" loop for team members. When a team member says "gm" to the agent, it prompts each team member to share their intentions for the day, starting with the person who initiated the conversation. The agent records each person's response. When a team member says "gn" to the agent, it prompts each team member to share what they accomplished that day, starting with the person who initiated the conversation. The agent records each person's response and can output a work dependency graph based on the data collected.

## Microworlds

The Agent will be used in the future to generate microworlds, which represent particular simulation contexts for various domains involving a set of coordination strategies, agents, and an environment. Human experts (or automated assurance systems) will validate the outputs of the agents and select which subset of microworlds they have generated are actually valid or safe. The output of this validation process will be used to re-train and fine-tune the agents, making them more effective at what they do.

## Conclusion

The Agent is a powerful tool for improving communication and collaboration among team members, generating valuable insights and data about organizations and their operations, and supporting the creation of safe and effective microworlds. By using prompts to initiate and record conversations with team members, the Agent helps establish a shared information context for organizations. By collecting and managing data, the Agent can output a work dependency graph to help team members better synthesize information about what the organization is, what others within the organization are working on, and how all of these elements compose together.

## Appendix
### Reproducibility
`nix` and `poetry` allow [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.