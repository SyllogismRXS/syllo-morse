#!/bin/bash

echo "Cleaning pycaches..."

find . -name '*pycache*' | xargs rm -rf

echo "Cleaning blender files..."
find -regex '.*blend[1234567890]' | xargs rm

# Removes files from git repo that have been deleted
#git rm $(git ls-files --deleted)  