#!/usr/bin/env -S just --justfile

update:
    poetry update
    
nix:
    nix-shell
    
shell: nix update

gmi:
    echo "only GMI in retrospect!"