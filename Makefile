all:
	git submodule update --init --recursive
	cd Sparrow && SPARROW_INSTALL_PATH=.. make install-dev
	bin/sparrow up
