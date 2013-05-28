#!/bin/bash

echo "Cleaning pycaches..."

find . -name '*pycache*' | xargs rm -rf
