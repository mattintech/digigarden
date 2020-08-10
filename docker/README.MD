# DigiGarden Docker CheatSheet
This folder is used to create the docker containers to run the digiGarden reporting Service.

## Starting or Adding a new docker image
```
docker-compose build
docker-compose up -d
```

## Updating Docker Config
```
docker-compose up -d
```

## stoping all containers 
```
docker-compose stop
```


## Utils

Get an IPAddress of a container.
```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <containerId or containerName>
```