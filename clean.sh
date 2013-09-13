#!/bin/bash

#echo "Cleaning local..."
rm -rf setenv.sh
rm -rf config
rm -rf ~/.morse

#echo "Cleaning pycaches..."
find . -name '*pycache*' -not -path "./3rd-party-build/*" -exec rm -rf {} +

#echo "Cleaning blender files..."
find -regex '.*blend[1234567890]' -exec rm -rf {} +
