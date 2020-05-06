#!/bin/bash

if [[ $1 == "stop" ]];then
    echo "stoping webServer"
    for pid in `ps -ef |grep -i webserver | grep -v grep | awk '{print $2}'`; do kill -9 $pid;done;
else
    echo "loading webServer"
    nohup python3 webServer.py  >> webServer.log &
fi
