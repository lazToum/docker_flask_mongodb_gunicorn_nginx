############################################################
# Dockerfile to build flask image
# Based on Ubuntu 16.04
############################################################

# Set the base image to Ubuntu

FROM laztoum/base

MAINTAINER laztoum "laztoum@gmail.com"

RUN mkdir /flaskApp \
	&& cd flaskApp

RUN apt-get update \
	&& apt-get install -y python-pip \
	gcc \
	nginx \
	supervisor \
	&& rm -rf /var/lib/apt/lists/*

COPY docker-app/requirements.txt /flaskApp/
RUN pip install -r /flaskApp/requirements.txt

COPY site.conf /etc/nginx/sites-available/default

# Custom Supervisord config
COPY nginflask.conf /etc/supervisor/conf.d/

# Make NGINX run on the foreground
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY docker-app/* /flaskApp/

WORKDIR /flaskApp
VOLUME /flaskApp

# Expose ports
EXPOSE 80 443

# Set the default command to execute when creating a new container
CMD ["supervisord", "-n"]

