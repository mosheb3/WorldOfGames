#!/bin/bash
python3 MainGame.py < test_answers.txt

grep "test123" data/data.json

if [ $? ]; then
  echo "aaaaaaaaaa"
else
  echo "bbbbbbbbbb"
fi