#!/bin/bash

if [ $1 -eq 1 ]; then

docker build -t app:boyceing .
docker run -d -p 8000:8000 --name boyceing_app app:boyceing
docker ps -a

fi

if [ $1 -eq 2 ]; then

docker rm -f boyceing_app
docker rmi app:boyceing

fi