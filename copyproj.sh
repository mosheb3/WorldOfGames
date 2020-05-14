#!/bin/bash

PROJ_NAME="WorldOfGames"
rsync -rv --exclude=.git/ --exclude=.idea/ --exclude=__pycache__ /drives/d/PycharmProjects/${PROJ_NAME}/* root@devops.local:/srv/projects/${PROJ_NAME}/
ssh root@devops.local "cd /srv/projects/${PROJ_NAME}/ ; dos2unix *;git commit -am 'commit from local copy'"
