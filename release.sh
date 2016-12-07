#!/usr/bin/env bash

VERSION=$1

if [ -z "$VERSION" ]; then
    echo "Usage: ./release.sh [VERSION]"
fi

source env/bin/activate
python -m unittest discover

git tag $VERSION
tag push --tags origin

python setup.py sdist upload -r pypi
