#!/bin/bash

cd ./opencve

docker-compose build

docker-compose up -d  postgres redis webserver celery_worker

docker exec -it webserver opencve upgrade-db

docker exec -it webserver opencve import-data

docker-compose up -d celery_beat

cd ..

docker compose up -d mongo redis mysql misp misp-modules elastcsearch kibana squid 














