#!/usr/bin/env bash

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: ./release.sh [VERSION]"
fi

source env/bin/activate
python -m unittest discover

git tag $VERSION
tag push --tags origin

rm -rf dist/
python setup.py sdist
python -m twine upload -repository pypi dist/*
