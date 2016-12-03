#!/usr/bin/env bash

source env/bin/activate
python -m unittest discover

python setup.py sdist upload -r pypi
