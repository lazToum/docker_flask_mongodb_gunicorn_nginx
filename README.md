# Docker Playground
A simple [Docker](https://www.docker.com "Docker") and [Docker Compose](https://docs.docker.com/compose/ "Docker Compose") project. It can be used for flask with mongodb applications development.
* Three docker images are created:
  * A base image from Ubuntu 16.04, including [gosu](https://github.com/tianon/gosu "gosu") 
  * A mongodb image, with a root user and a database owner
  * A third image with flask (project files inside a volume), gunicorn (with the `--reload` option for autoreload on file change)  and nginx. Flask mongoengine's [example](https://github.com/MongoEngine/flask-mongoengine/tree/master/examples) is included.

## Getting Started
### Images and containers setup
Docker is required. You can either 
* run `setup.sh` inside the project's root directory or 
* install docker-compose *version >= 1.6* and use the docker-compose.yml. Just run `docker-compose up` (optionally include the *-d* option to detach it) 

You can then change anything inside the flask project [*flask-gunicorn-nginx/flask-app/*](./flask-gunicorn-nginx/flask-app) and view the changes on http://localhost.

### Start | stop the containers
either with
* `docker start | stop flask-mongo && docker start | stop flask-gunicorn-nginx` or
* `docker-compose start|stop` inside the folder containing *docker-compose.yml*
The mongo container has to start before the flask/gunicorn/nginx container.
