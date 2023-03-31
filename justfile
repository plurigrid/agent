default_mode := "gradio"
play mode=default_mode:
    poetry run python3 -m agent --agent play_coplay --mode {{mode}}

summon prompt mode=default_mode:
    poetry run python3 -m agent --agent digital_twin --prompt {{prompt}} --mode {{mode}}

ontology knowledge-base mode="repl": 
    python3 -m agent --agent ontology --mode {{mode}} --path {{knowledge-base}}

install:
    nix-shell --run "poetry install"

update: 
    nix-shell --run "poetry update"

shell:
    nix-shell --run "poetry shell"


