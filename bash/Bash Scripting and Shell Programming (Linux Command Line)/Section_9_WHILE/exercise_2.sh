#!/bin/bash

# Exercise 2:
# 
# Write a shell script that asks the user for the number of lines 
# they would like to display from the /etc/passwd file and display those lines.

read -p "Enter number of lines to read: " NUM_TO_READ

if [ -z "$NUM_TO_READ" ]; then
  exit 1
fi

LINE_NUM=1

while read LINE
do
  echo "${LINE_NUM}: ${LINE}"
  ((LINE_NUM++))

  if [ "$LINE_NUM" -gt "$NUM_TO_READ" ]; then
    break
  fi
done < /etc/passwd
