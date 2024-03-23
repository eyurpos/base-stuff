#!/bin/bash

# Exercise 5:
# 
# Write a shell script that displays "man", "bear", "pig", "dog", "cat", 
# and "sheep" to the screen with each appearing on a separate line. 
# Try to do this in as few lines as possible.

LIST=( "man" "bear" "pig" "dog" "cat" "sheep" );

for BEAST in ${LIST[@]}
do
    echo "$BEAST"
done
