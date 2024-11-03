#!/bin/sh
JOVEO_ENV=$1
echo $JOVEO_ENV

## cleanup
cleanup()
{
    docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
}

cleanup

# copy the nginx config file based on environment
cp .docker/nginx-${JOVEO_ENV}.conf .docker/nginx.conf
if [ $? -ne 0 ];then
    ## cleanup
    cleanup
    exit 1
fi

# Create builder image
docker build --build-arg JOVEO_ENV=$JOVEO_ENV -t apply-mobweb-builder -f .docker/Dockerfile-builder .
if [ $? -ne 0 ];then
    ## cleanup
    docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
    exit 1
fi

# Run the builder image
docker run -e JOVEO_ENV=$JOVEO_ENV --rm -v `pwd`:/src apply-mobweb-builder:latest
if [ $? -ne 0 ];then
    ## cleanup
    docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
    exit 2
fi

# Build the deployable image
docker build -t joveo/apply-mobweb -f .docker/Dockerfile .
if [ $? -ne 0 ];then
    ## cleanup
    docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
    exit 3
fi

# remove the builder image
docker rmi -f apply-mobweb-builder
if [ $? -ne 0 ];then
    ## cleanup
    docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
    exit 4
fi

## cleanup
docker run --privileged --rm -v `pwd`:/src alpine sh -c "rm -rf /src/node_modules /src/dist"
