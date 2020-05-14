#!/bin/bash

python3 MainGame.py < test_answers.txt

grep "test123" data/data.json

echo $?