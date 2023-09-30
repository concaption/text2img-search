#!/usr/bin/env bash

### Sets up python packages in for devcontainer.json

#create a virtualenv
python -m venv .venv

# append it to bash so every shell launches with it 
echo 'source .venv/bin/activate' >> ~/.bashrc

# source virtualenv
source .venv/bin/activate

# install all software 
make install
