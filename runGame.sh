#!/bin/bash

## run game
docker-compose stop && docker-compose rm -f
docker-compose up -d wog-web
docker-compose run wog
