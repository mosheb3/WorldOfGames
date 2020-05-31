#!/bin/bash
echo "loading webServer ..."
nohup python3 webServer.py  >> webServer.log &

python3 MainGame.py < test_answers.txt

grep "test123" data/data.json

cat data/data.json | grep -i "test123"

if [ $? == 0 ]; then
  echo "Test Success"
  exit 0
else
  echo "Test Not Success"
  exit 1
fi