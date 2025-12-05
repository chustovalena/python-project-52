curl -LsSf https://astral.sh/uv/install.sh -o uv_install.sh
sh uv_install.sh

source $HOME/.local/bin/env


make install && make collectstatic && make migrate