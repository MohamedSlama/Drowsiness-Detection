#!/bin/bash

cd "$(dirname "$0")"
python detect.py 1

# 1 if you have multi cameras delete it if you want to use the default camera
