# Getting started
## Using `just`
`just shell`
## Manually
0. Clone this repo
1. Install [nix](https://nixos.org/download.html#nix-install-macos)
2. Run `poetry update`
3. Run `poetry shell` inside `agent/agent`
4. ??? (e.g. `python <...>`)
5. PROFIT!11!!!
## Appendix
### Reproducibility
`nix` and `poetry` allow [packaging for serverless execution](https://github.com/bananaml/serverless-template) with reliable system, package, and other application dependencies like Secrets correctly derived for individual `agent` runtime environment.

