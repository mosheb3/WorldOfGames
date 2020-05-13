#!/bin/bash
if [ "$1" == "build" ];then
  docker build -t wog:latest .
elif [ "$1" == "run" ];then
  docker run -it --rm --name wog wog:latest python3 MainGame.py
else
  echo "Usage: bulid / run"
fi