{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {

  buildInputs = with pkgs; [
    python3
    poetry
    texlive.combined.scheme-full
    gcc
    tree
    just
  ];
}