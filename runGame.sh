#!/bin/bash

## run game
service_name="wog-web"
docker_compose_dir="/usr/local/bin"

if [ -z `$docker_compose_dir/docker-compose ps -q $service_name` ] || [ -z `docker ps -q --no-trunc | grep $($docker_compose_dir/docker-compose ps -q $service_name)` ]; then
   $docker_compose_dir/docker-compose stop && $docker_compose_dir/docker-compose rm -f
   $docker_compose_dir/docker-compose up -d wog-web
   $docker_compose_dir/docker-compose run wog && $docker_compose_dir/docker-compose rm -f
else
   $docker_compose_dir/docker-compose run wog && $docker_compose_dir/docker-compose rm -f
fi


