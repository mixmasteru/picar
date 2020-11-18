#!/bin/bash
FOLDER=${1}

docker build --tag myros:noetic .
docker run -d \
    -it \
    --name noeticros \
    --rm \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$FOLDER:/root/ros:rw" \
    -p 127.0.0.1:2223:22 \
    myros:noetic

