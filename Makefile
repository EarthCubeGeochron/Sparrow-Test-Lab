all:
	git submodule update --init --recursive
	cp pgweb-addon/nginx-location.conf Sparrow/nginx-config/locations/pgweb.conf
	cd Sparrow && SPARROW_INSTALL_PATH=.. make install-dev
	bin/sparrow up
