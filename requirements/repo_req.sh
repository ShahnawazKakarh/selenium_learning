#!/usr/bin/env bash

curl https://bootstrap.pypa.io/get-pip.py | python
pre-commit install --install-hooks
pip install -r $1requirements/requirements.txt
pre-commit install
