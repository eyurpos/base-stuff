#!/bin/bash

# Exercise 2: 
#
# Write a script that renames files based on the file extension. 
# The script should prompt the user for a file extension. 
# Next, it should ask the user what prefix to prepend to the file name(s). 
# By default the prefix should be the current date in YYYY­MM­DD format. 
# So, if the user simply presses enter the date will be used. 
# Otherwise, whatever the user entered will be used as the prefix. 
# Next, it should display the original file name and the new name of the file. 
# Finally, it should rename the file. 

OPTION="C"
sh ./files_op.sh $OPTION

read -p "Enter the file extencion: " EXTENCION
if [ -z "$EXTENCION" ]; then
  sh ./files_op.sh D
  exit 1
fi

read -p "Enter the file extencion: " PREFIX
if [ -z "$PREFIX"]; then
  PREFIX=$(date +%F)
fi

cd tmp
for FILE in *.$EXTENCION
do
  NEW_NAME=${PREFIX}-${FILE}
  echo $FILE $NEW_NAME
  mv $FILE $NEW_NAME
done

cd ..
sh ./files_op.sh D

