#!/bin/bash

if [ "$1" == "build" ];then
  docker build -t wog:latest .
  docker build -f Dockerfile_web -t wog-web:latest .
elif [ "$1" == "run" ];then
  docker stop wog-web
  docker run --rm -d -p 8081:8081 --name wog-web -v $(pwd):/app wog-web:latest
  docker run -it --rm --name wog -v $(pwd):/app wog:latest
else
  echo "Usage: run / bulid"
fi