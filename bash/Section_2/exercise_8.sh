#!/bin/bash

# Exercise 8:
# 
# Modify the previous script to accept an unlimited number of files 
# and directories as arguments. Hint: You'll want to use a special variable. 

for FILE in $@
do
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
done

