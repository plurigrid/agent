default_mode := "gradio"
play mode=default_mode:
    nix-shell --run "poetry run python3 -m agent --agent play_coplay --mode {{mode}}"

summon mode=default_mode:
    nix-shell --run "poetry run python3 -m agent --agent digital_twin --mode {{mode}}"

ontology knowledge-base mode="repl": 
    python3 -m agent --agent ontology --mode {{mode}} --path {{knowledge-base}}

install:
    nix-shell --run "poetry install"

update: 
    nix-shell --run "poetry update"

shell:
    nix-shell --run "poetry shell"


