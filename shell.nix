{ pkgs ? import <nixpkgs> {} }:
pkgs.mkShell {
  name = "compressor-python";
  buildInputs = with pkgs; [ (python3.withPackages (p: with p; [ numpy ]) ) ];
}
