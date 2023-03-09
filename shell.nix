{ pkgs ? import <nixpkgs> {} }:

let
  libxml2 = pkgs.libxml2;
  libxslt = pkgs.libxslt;
in

pkgs.mkShell {
  buildInputs = with pkgs; [
    python3
    poetry
    texlive.combined.scheme-full
    gcc
    nodejs
    tree
    libxml2
    libxslt
  ];

  shellHook = ''
    export PKG_CONFIG_PATH=${libxml2.dev}/lib/pkgconfig:${libxslt.dev}/lib/pkgconfig
  '';
}
