#!/bin/bash

if ! command -v docker &> /dev/null;
then
    echo "docker is not installed"
else
    echo "Docker is installed."
    docker_version=$(docker --version)
    echo "Docker VERSION: $docker_version"
fi
