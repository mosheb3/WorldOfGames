#!/bin/bash

## run game
service_name="wog-web"

if [ -z `docker-compose ps -q $service_name` ] || [ -z `docker ps -q --no-trunc | grep $(docker-compose ps -q $service_name)` ]; then
   docker-compose stop && docker-compose rm -f
   docker-compose up -d wog-web
else
   docker-compose run wog
fi


