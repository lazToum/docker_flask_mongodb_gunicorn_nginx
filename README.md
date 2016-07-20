# Docker Playground
A simple [Docker](https://www.docker.com "Docker") and [Docker Compose](https://docs.docker.com/compose/, "Docker Compose") project. It can be used for flask with mongodb applications development.
* Three docker images are created:
  * A base image from Ubuntu 16.04, including [gosu](https://github.com/tianon/gosu "gosu") 
  * A mongodb image, with a root user and a database owner
  * A third image with flask (project files inside a volume), gunicorn and nginx. Flask mongoengine's [example](https://github.com/MongoEngine/flask-mongoengine/tree/master/examples) is included

## Getting Started 
Docker is required. You can either 
* run `setup.sh` inside the project's root directory or 
* install docker-compose *version >= 6.1* and use the docker-compose.yml. Just run `docker-compose` (optionally include the *-d* option to detach it)

### Start|stop the containers either
* with `docker start|stop flask-mongo && flask-gunicorn-nginx` or
* `docker-compose start|stop` inside the folder containing *docker-compose.yml*

the included folder *flask-gunicorn-nginx/flask-app* is shared with the host and any change made is these files will reload the gunicorn service.
