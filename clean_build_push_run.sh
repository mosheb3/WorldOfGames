#!/bin/bash

docker stop wog wog-web
docker rm wog wog-web
docker image rm mosheb3/wog-web mosheb3/wog

./run-docker.sh build

docker push mosheb3/wog:latest
docker push mosheb3/wog-web:latest

docker-compose up -d wog-web
