#!/bin/sh

cp *.py docker
cp -Rf franken docker
docker build -t $1 docker
rm docker/*.py
rm -Rf docker/franken