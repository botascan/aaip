{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
	packages = [ pkgs.python313 ];
	LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
		pkgs.stdenv.cc.cc.lib
		pkgs.zlib
	];
}
