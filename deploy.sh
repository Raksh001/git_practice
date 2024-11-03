#!/bin/sh
echo $JOVEO_ENV
awsTag="$1"
image="$2"
env="$3"

containerName=$(echo "$image" | sed 's/^.*\///' | sed 's/:.*$//')

filter1="Name=tag-key,Values=$awsTag"
filter2="Name=instance-state-name,Values=running"

describeInstancesCmd="aws ec2 describe-instances --region us-east-1 --filter $filter1 $filter2"

if [ "$env" = "prod" ]; then
    instanceIPs=$(${describeInstancesCmd} | egrep -i 'privateipaddress"' | sed 's/^.*://' | sed 's/\"//g' | sed 's/,//' | uniq)
else
    instanceIPs=$(${describeInstancesCmd} --profile joveo-dev | egrep -i 'privateipaddress"' | sed 's/^.*://' | sed 's/\"//g' | sed 's/,//' | uniq)
fi

echo $instanceIPs

for ip in $instanceIPs
do
    docker -H $ip:5555 pull "$image:$env"

    containerId=`docker -H $ip:5555 ps -qa --filter "name=$containerName"`
    if [ -n "$containerId" ]
    then
        echo "Stopping and removing existing container"
        docker -H $ip:5555 stop $containerName
        docker -H $ip:5555 rm $containerName
    fi

    docker -H $ip:5555 run -d -e JOVEO_ENV=$env --name $containerName --net "host" --restart=always "$image:$env"
done
