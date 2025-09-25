FROM nvidia/cuda:13.0.1-base-ubuntu24.04

ENV LANG="C.UTF-8"
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL=/bin/bash
ENV DOCKER_BUILDKIT=1

RUN yes | unminimize 2>&1

# Install basic build tools
RUN     apt-get update &&  apt-get upgrade -y \
    &&  apt-get install -y --no-install-recommends \
            make unzip git build-essential swig3.0 unixodbc-dev libpq-dev \
            default-libmysqlclient-dev moreutils rsync zip libgdiplus jq \
            python3-setuptools-whl python3-pip-whl libc6 libgcc1 libgssapi-krb5-2 \
            libncurses6 liblttng-ust1t64 libssl-dev libstdc++6 zlib1g libuuid1 \
            libunwind8 sqlite3 libsqlite3-dev software-properties-common tk-dev \
            uuid-dev curl gettext inotify-tools \
    &&  add-apt-repository universe \
    &&  apt-get update && apt-get upgrade -y \
    &&  apt-get clean -y \
    &&  rm -rf /var/lib/apt/lists/*

# Verify expected build and debug tools are present
RUN     apt-get update && apt-get upgrade -y \
    &&  apt-get install -y --no-install-recommends \
            build-essential cmake cppcheck valgrind clang lldb llvm gdb python3-dev \
    &&  apt-get install -yq \
            vim vim-doc xtail software-properties-common libsecret-1-dev \
    &&  apt-get install -y --no-install-recommends \
            libnss3 libnspr4 libatk-bridge2.0-0 libatk1.0-0 libx11-6 \
            libpangocairo-1.0-0 libx11-xcb1 libcups2 libxcomposite1 libxdamage1 \
            libxfixes3 libpango-1.0-0 libgbm1 libgtk-3-0 \
    &&  mkdir -p "/usr/local/etc/vscode-dev-containers/" \
    &&  touch /usr/local/etc/vscode-dev-containers/first-notice.txt \
    &&  apt-get clean -y \
    &&  rm -rf /var/lib/apt/lists/*

# Install and setup fish
RUN     apt-get update &&  apt-get upgrade -y \
    &&  apt-get install -yq --no-install-recommends fish \
    &&  FISH_PROMPT="function fish_prompt\n    set_color green\n    echo -n (whoami)\n    set_color normal\n    echo -n \":\"\n    set_color blue\n    echo -n (pwd)\n    set_color normal\n    echo -n \"> \"\nend\n" \
    &&  printf "$FISH_PROMPT" >> /etc/fish/functions/fish_prompt.fish \
    &&  printf "if type code-insiders > /dev/null 2>&1; and not type code > /dev/null 2>&1\n  alias code=code-insiders\nend" >> /etc/fish/conf.d/code_alias.fish \
    &&  apt-get autoremove -y \
    &&  apt-get clean -y \
    &&  rm -rf /var/lib/apt/lists/* \
    &&  rm -rf /tmp/scripts

# Mount for docker-in-docker 
VOLUME [ "/var/lib/docker" ]

# [Optional] Install debugger for development of Codespaces - Not in resulting image by default
ARG DeveloperBuild
RUN if [ -z $DeveloperBuild ]; then \
        echo "not including debugger" ; \
    else \
        curl -sSL https://aka.ms/getvsdbgsh | bash /dev/stdin -v latest -l /vsdbg ; \
    fi


### CUDA 


# Set CUDA environment variables
ENV PATH=/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}
ENV CUDA_HOME=/usr/local/cuda

RUN     apt-get update && apt-get upgrade -y \
    &&  apt-get install -y --no-install-recommends \
            bash curl wget \
            python3 python3-pip python3-venv \
    &&  apt-get clean -y \
    &&  rm -rf /var/lib/apt/lists/*

RUN     usermod -s /bin/bash ubuntu

USER ubuntu
WORKDIR /home/ubuntu

RUN     curl -LsSf https://astral.sh/uv/install.sh | sh
RUN     echo "which tox >/dev/null || uv tool install tox --with tox-uv" >> ~/.bashrc
RUN     echo "alias tox='tox --workdir=$HOME/.tox'" >> ~/.bashrc
RUN     echo "cd app" >> ~/.bashrc

COPY --chown=ubuntu:ubuntu . /home/ubuntu/app/

CMD [ "sleep", "infinity" ]
