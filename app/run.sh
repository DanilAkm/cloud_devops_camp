#!/bin/bash

if [ $# -eq 1 ]; then  # argv mode
if [ $1 -eq 1 ]; then  # valid argc

docker build -t app:boyceing .
docker run -d -p 8000:8000 --name boyceing_app app:boyceing
docker ps -a

sleep 1

echo "The hostname is: $(curl -s http://localhost:8000/hostname)"
echo "The UUID is: $(curl -s http://localhost:8000/id)"
echo "The Author is: $(curl -s http://localhost:8000/author)"

fi

if [ $1 -eq 2 ]; then

docker rm -f boyceing_app
docker rmi app:boyceing

fi

if [ $1 -eq 3 ]; then

echo "The hostname is: $(curl -s http://localhost:8000/hostname)"
echo "The UUID is: $(curl -s http://localhost:8000/id)"
echo "The Author is: $(curl -s http://localhost:8000/author)"

fi  # argv mode
fi  # valid argc