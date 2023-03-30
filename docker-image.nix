{ pkgs ? import <nixpkgs> {}, lib ? pkgs.lib }:

let

  python310 = pkgs.python310;
  pythonPackages = python310.pkgs;
  cmake_3_26_1 = pkgs.cmake.override {
    version = "3.26.1";
  };
  # Create the Python application derivation
  app = pkgs.poetry2nix.mkPoetryApplication {
    projectDir = ./.;
    overrides = pkgs.poetry2nix.overrides.withDefaults (self: super: { orjson =
        let
          getCargoHash = version: {
            "3.6.7" = "sha256-sz2k9podPB6QSptkyOu7+BoVTrKhefizRtYU+MICPt4=";
            "3.6.8" = "sha256-vpfceVtYkU09xszNIihY1xbqGWieqDquxwsAmDH8jd4=";
            "3.7.2" = "sha256-2U37IhftNYjH7sV7Nh51YpR/WjmPmmzX/aGuHsFgwf4=";
            "3.7.9" = "sha256-QHzAhjHgm4XLxY2zUdnIsd/WWMI7dJLQQAvTXC+2asQ=";
            "3.8.0" = "sha256-8k0DetamwLqkdcg8V/D2J5ja6IJSLi50CE+ZjFa7Hdc=";
            "3.8.1" = "sha256-QXguyDxQHW9Fd3Nhmi5JzSxZQuk3HGPhhh/RGuOTZNY=";
            "3.8.3" = "sha256-oSZO4cN1sJKd0T7pYrKG63is8AZMKaLRZqj5UCVY/14=";
            "3.8.4" = "sha256-O2W9zO7qHWG+78T+uECICAmecaSIbTTJPktJIPZYElE=";
            "3.8.5" = "sha256-JtUCJ3TP9EKGcddeyW1e/72k21uKneq9SnZJeLvn9Os=";
            "3.8.6" = "sha256-8T//q6nQoZhh8oJWDCeQf3gYRew58dXAaxkYELY4CJM=";
            "3.8.7" = "sha256-JBO8nl0sC+XIn17vI7hC8+nA1HYI9jfvZrl9nCE3k1s=";
            "3.8.8" = "sha256-AK4HtqPKg2O2FeLHCbY9o+N1BV4QFMNaHVE1NaFYHa4=";
          }.${version} or (
            lib.warn "Unknown orjson version: '${version}'. Please update getCargoHash." lib.fakeHash
          );
        in
        super.orjson.overridePythonAttrs (old: {
          cargoDeps = pkgs.rustPlatform.fetchCargoTarball {
            inherit (old) src;
            name = "${old.pname}-${old.version}";
            hash = getCargoHash old.version;
          };
          nativeBuildInputs = (old.nativeBuildInputs or [ ]) ++ [
            pkgs.rustPlatform.cargoSetupHook
            pkgs.rustPlatform.maturinBuildHook
          ];
          buildInputs = (old.buildInputs or [ ]) ++ lib.optional pkgs.stdenv.isDarwin pkgs.libiconv;
        }); 
             # workaround https://github.com/nix-community/poetry2nix/issues/568
            # Add flit-core and platformdirs as build inputs for wheel
            wheel = super.wheel.overridePythonAttrs (old: {
              buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.flit-core ];
            });
              argparse = super.argparse.overridePythonAttrs (old: {
                buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.setuptools ];
            });
              clang = super.clang.overridePythonAttrs (old: {
                buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.setuptools ];
            });
              slugify = super.slugify.overridePythonAttrs (old: {
                buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.setuptools ];
            });
            cmake = with pkgs; cmake_3_26_1.overridePythonAttrs (old: {
                # Add any additional build inputs here
                buildInputs = old.buildInputs or [python310.pkgs.setuptools python310.pkgs.scikit-build ];
              });
  
  # super.cmake.overridePythonAttrs (old: {
  #               buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.setuptools python310.pkgs.scikit-build];
  #           });
            pypdf = super.pypdf.overridePythonAttrs (old: {
                buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.flit-core ];
            });
            pypdf2 = super.pypdf2.overridePythonAttrs (old: {
                buildInputs = old.buildInputs or [ ] ++ [ python310.pkgs.flit-core ];
            });
              });
  };

  # Define the Docker image
  dockerImage = pkgs.dockerTools.buildImage {
    name = "plurigrid";
    tag = "latest";
    copyToRoot = app;
    config = {
      Cmd = [ "${app}/bin/python3" "-m" "agent" "--agent" "play_coplay" "--mode" "gradio" ];
      WorkingDir = "${app}";
    };
  };
in
  dockerImage
