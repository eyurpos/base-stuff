#!/bin/bash

# Exercise 1: 
#
# Write a shell script that renames all files in the current directory that end in ".txt" 
# to begin with today's date in the following format: YYYY­MM­DD. For example, 
# if a picture of my cat was in the current directory and today was October 31, 
# 2016 it would change name from "mycat.txt" to "2016­10­31­mycat.txt". 

sh ./files_op.sh "C"

cd tmp

DATE=$(date +%F)

for FILE in *.txt
do
  mv $FILE ${DATE}-${FILE}
done

cd ..
sh ./files_op.sh D
