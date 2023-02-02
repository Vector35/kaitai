# use symlinks to implement "development mode" or "editable installs"
# https://setuptools.pypa.io/en/latest/userguide/development_mode.html

.PHONY: install uninstall

install:
	@if [ -L "$(BN_PLUGINS)/kaitai" ]; then \
		echo "already installed"; \
	else \
		echo "installing"; \
		ln -s "$(PWD)/plugin" "$(BN_PLUGINS)/kaitai"; \
	fi

uninstall:
	@if [ -L "$(BN_PLUGINS)/kaitai" ]; then \
		echo "uninstalling"; \
		rm "$(BN_PLUGINS)/kaitai"; \
	else \
		echo "not installed"; \
	fi
