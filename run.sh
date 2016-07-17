#!/bin/bash
cd docker-base
docker build -t laztoum/base -f Dockerfile .
cd ../docker-mongo
docker build -t laztoum/mongo -f Dockerfile .
docker run --name flask-mongo -d -p 27027:27017 laztoum/mongo
cd ../docker-flask
docker build -t laztoum/flask-uwsgi-nginx -f Dockerfile .
cd ..
docker run --name flask-nginx -d -v $PWD/docker-app:/flaskApp  -p 80:80 laztoum/flask-uwsgi-nginx