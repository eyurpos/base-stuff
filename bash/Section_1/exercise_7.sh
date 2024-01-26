#!/bin/bash

# Exercise 7:
# 
# Modify the previous script so that it accepts the file or directory 
# name as an argument instead of prompting the user to enter it.

FILE=$1

if [ -f $FILE ]
then
    echo "$FILE is a regular file."
elif [ -d $FILE ]
then
    echo "$FILE is a directory." 
else
    echo "$FILE something else."
fi

ls $FILE