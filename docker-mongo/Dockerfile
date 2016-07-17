############################################################
# Dockerfile to build MongoDB container image
# Based on Ubuntu 16.04
############################################################

# Set the base image to Ubuntu
FROM laztoum/base

MAINTAINER laztoum "laztoum@gmail.com"

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN groupadd -r mongodb && useradd -r -g mongodb mongodb

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		numactl \
	&& rm -rf /var/lib/apt/lists/*

# Import the public key used by the package management system
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

# Create a list file for MongoDB
RUN echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# install mongodb
RUN apt update \
	&& apt install -y mongodb-org \
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -rf /var/lib/mongodb \
	&& mv /etc/mongod.conf /etc/mongod.conf.orig

# create mongo dirs
RUN mkdir -p /data/db /data/configdb \
	&& chown -R mongodb:mongodb /data/db /data/configdb

# create root user, database and database user
COPY setup.sh /setup.sh
RUN /bin/bash /setup.sh

RUN mkdir -p /data/db /data/configdb \
	&& chown -R mongodb:mongodb /data/db /data/configdb
VOLUME /data/db /data/configdb
COPY mongod.conf /mongod.conf

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 27017
CMD ["/usr/bin/mongod","--config","/mongod.conf"]