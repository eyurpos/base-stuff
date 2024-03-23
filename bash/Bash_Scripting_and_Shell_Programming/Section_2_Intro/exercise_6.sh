#!/bin/bash

# Exercise 6:
#
# Write a shell script that prompts the user for a name of a file or directory 
# and reports if it is a regular file, a directory, or other type of file. 
# Also perform an ls command against the file or directory with the long listing option.

read -p "Enter the path to a file or a directory: " FILE

if [ -f $FILE ]; then
    echo "$FILE is a regular file."
elif [ -d $FILE ]; then
    echo "$FILE is a directory." 
else
    echo "$FILE something else."
fi

ls $FILE
