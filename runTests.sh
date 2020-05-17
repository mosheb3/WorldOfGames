#!/bin/bash
python3 MainGame.py < test_answers.txt

grep "test123" data/data.json

cat data/data.json | grep -i "test123"

if [ $? == 0 ]; then
  echo "Test Success"
else
  echo "Test Not Success"
fi