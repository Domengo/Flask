FROM ubuntu:16.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install \
    build-essential libssl-dev vim git curl lsof python2.7 && \
    ln -s /usr/bin/python2.7 /usr/bin/python

RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh && \
    bash nodesource_setup.sh && \
    apt-get -y install nodejs && \
    npm i -g n

LABEL maintainer="fatima.abdullah@educative.io"
RUN apt-get install python3
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
    python3 get-pip.py && \
    python3 -m pip install --upgrade pip

RUN pip3 install flask && \
    pip3 install flask-sqlalchemy && \
    pip3 install Flask-WTF && \
    pip3 install watchdog

COPY . /usr/local/educative/
WORKDIR /usr/local/educative


EXPOSE 8100
