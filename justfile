default := "repl"
play mode=default:
    nix-shell --run "poetry run python3 -m agent --agent play_coplay --mode {{mode}}"

install:
    nix-shell --run "poetry install"

update: 
    nix-shell --run "poetry update"

