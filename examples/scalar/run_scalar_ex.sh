#!/bin/bash

echo "Run lcm-gen on the example LCM definitions"
./buildlcm.sh

echo "Setup and run the graphing utility"
export PYTHONPATH=./
python ../../lcm-grapher.py graphing_ex &

echo "Run our example program to generate some LCM messages"
python scalar_sine_ex.py

