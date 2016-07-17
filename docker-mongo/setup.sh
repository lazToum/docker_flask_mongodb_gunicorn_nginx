#!/bin/bash

mongod --dbpath /data/db &

RET=1
while [[ RET -ne 0 ]]; do
    echo "=> Waiting for confirmation of MongoDB service startup"
    sleep 5
    mongo admin --eval "help" >/dev/null 2>&1
    RET=$?
done

ADMINUSER=rootUser
ADMINPASS=changeMe
DBNAME=flaskDb
DBUSER=flaskUser
DBPASSWORD=changeMe

mongo admin --eval "db.createUser({user: '$ADMINUSER', pwd: '$ADMINPASS', roles:[{role:'root',db:'admin'}]});"

mongo $DBNAME --eval "db.createUser({user: '$DBUSER', pwd: '$DBPASSWORD', roles:[{role:'dbAdmin',db:'$DBNAME'}, {role:'readWrite',db:'$DBNAME'}]});"

mongod --shutdown