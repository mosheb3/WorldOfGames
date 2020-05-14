#!/bin/bash
#dos2unix /drives/d/PycharmProjects/${PROJ_NAME}/*.txt
#dos2unix /drives/d/PycharmProjects/${PROJ_NAME}/Jenkinsfile
#dos2unix /drives/d/PycharmProjects/${PROJ_NAME}/*.py

PROJ_NAME="WorldOfGames"

# scp /drives/d/PycharmProjects/${PROJ_NAME}/*.txt root@devops.local:/srv/projects/${PROJ_NAME}/
#scp /drives/d/PycharmProjects/${PROJ_NAME}/*.py root@devops.local:/srv/projects/${PROJ_NAME}/
#scp /drives/d/PycharmProjects/${PROJ_NAME}/Dockerfile root@devops.local:/srv/projects/${PROJ_NAME}/
#scp /drives/d/PycharmProjects/${PROJ_NAME}/Jenkinsfile root@devops.local:/srv/projects/${PROJ_NAME}/

rsync -rv --exclude=.git/ --exclude=.idea/ --exclude=__pycache__ /drives/d/PycharmProjects/${PROJ_NAME}/* root@devops.local:/srv/projects/${PROJ_NAME}/
ssh root@devops.local "cd /srv/projects/${PROJ_NAME}/ ; dos2unix *;git commit -am 'commit from local copy'"
