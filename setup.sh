#!/bin/bash
#docker stop flask-gunicorn-nginx && docker rm flask-gunicorn-nginx
#docker stop flask-mongo && docker rm flask-mongo
#docker rmi laztoum/flask-gunicorn-nginx && docker rmi laztoum/mongo
cd docker-base
docker build -t laztoum/base -f Dockerfile .
cd ../docker-mongo
docker build -t laztoum/mongo -f Dockerfile .
docker run --name flask-mongo -d -p 27017:27017 laztoum/mongo
cd ../flask-gunicorn-nginx
docker build -t laztoum/flask-gunicorn-nginx -f Dockerfile .
docker run --name flask-gunicorn-nginx --link flask-mongo:flask-mongo -d -v $PWD/flask-app:/flaskApp  -p 80:80 laztoum/flask-gunicorn-nginx
