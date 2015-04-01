#!/bin/bash

echo Starting Receive Script
sudo python XBeeControl_receive.py &

echo Starting Server
sudo python Map/server.py &

xdg-open http://127.0.0.1:8080/

read userInput

echo killing scripts
sudo pkill -1 -f server.py
sudo pkill -1 -f XBeeControl_receive.py
    #ps -ef | grep "server.py" | awk '{print $2}' | xargs kill
    #ps -ef | grep "XBee" | awk '{print $2}' | xargs kill
exit 1
