#!/bin/bash

## stop and remove old image
docker stop wog wog-web
docker rm wog wog-web
docker image rm mosheb3/wog-web mosheb3/wog

## buid
./run-docker.sh build

## push to remote
docker push mosheb3/wog:latest
docker push mosheb3/wog-web:latest
