#!/bin/bash
if [ "$1" == "build" ];then
  docker build -t wog:latest .
  docker build -t -f Dockerfile_web wogweb:latest .
elif [ "$1" == "run" ];then
  docker run --rm -d -p 8081:8081 --name wogweb -v $(pwd):/app wogweb:latest
  docker run -it --rm --name wog -v $(pwd):/app wog:latest
else
  echo "Usage: bulid / run"
fi