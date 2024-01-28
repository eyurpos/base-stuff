#!/bin/bash

# Exercise 1
#
# Create a startup script for an application called sleep­-walking­-server, 
# which is provided below. The script should be named sleep­walking and 
# accept "start" and "stop" as arguments. If anything other than 
# "start" or "stop" is provided as an argument, display a usage statement: 
# "Usage sleep­walking start|stop" and terminate the script with an exit status of 1.

START=start
STOP=stop

case "$1" in
    $START)
        /tmp/sleep­-walking­-server &
        ;;
    $STOP)
        kill $(cat /tmp/sleep-walking-server.pid)
        ;;
    *)
        echo "Wrong usage. Suported options $START|$STOP"
        exit 1
esac
