#!/bin/bash

# Exercise 3:
#
# Store the output of the command "hostname" in a variable. Display "This script is running on _______." 
# where "_______" is the output of the "hostname" command.

HOST_NAME=$(hostname)
echo "This script is running on $HOST_NAME."