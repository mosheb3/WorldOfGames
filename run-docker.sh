#!/bin/bash

IMG_APP="mosheb3/wog"
IMG_WEB="mosheb3/wog-web"
IMG_APP_NAME="wog"
IMG_WEB_NAME="wog-web"

if [ "$1" == "build" ];then
   if [ `/sbin/sysctl net.ipv4.conf.all.forwarding -n` != 1 ]; then
      /sbin/sysctl -w net.ipv4.conf.all.forwarding=1
      /sbin/sysctl -p
   fi

   docker build -t ${IMG_APP}:latest .
   docker build -f Dockerfile.web -t ${IMG_WEB}:latest .
elif [ "$1" == "run" ];then
   if [ "$(docker inspect -f '{{.State.Running}}' ${IMG_WEB_NAME} 2>/dev/null)" != "true" ]; then
      docker stop ${IMG_WEB_NAME}
   fi
      docker run --rm -d -p 8081:8081 --name ${IMG_WEB_NAME} -v $(pwd):/app ${IMG_WEB}:latest
      docker run -it --rm --name ${IMG_APP_NAME} -v $(pwd):/app ${IMG_APP}:latest
else
   echo "Usage: run / bulid"
fi
