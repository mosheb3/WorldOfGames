#!/bin/bash

if [ "$1" == "build" ];then
  if [ `/sbin/sysctl net.ipv4.conf.all.forwarding -n` != 1 ]; then
    /sbin/sysctl -w net.ipv4.conf.all.forwarding=1
    /sbin/sysctl -p
  fi

  docker build -t mosheb3/wog:latest .
  docker build -f Dockerfile_web -t mosheb3/wog-web:latest .
elif [ "$1" == "run" ];then
  docker stop wog-web
  docker run --rm -d -p 8081:8081 --name wog-web -v $(pwd):/app mosheb3/wog-web:latest
  docker run -it --rm --name wog -v $(pwd):/app mosheb3/wog:latest
else
  echo "Usage: run / bulid"
fi