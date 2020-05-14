#!/bin/bash
python3 MainGame.py < test_answers.txt

grep "test123" data/data.json

cat data/data.json

if [ $? == 0 ]; then
  echo "aaaaaaaaaa"
else
  echo "bbbbbbbbbb"
fi