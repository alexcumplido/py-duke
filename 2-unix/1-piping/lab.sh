# Part 1: Count the lines in the file and inspect the contents
# Run wc -l nba_2017.csv
# How many lines are in the file?
# Run the head nba_2017.csv and inspect the first few rows of the file.

# Part 2: Truncate and shuffle the file
# Truncate and shuffle the file shuf -n 100 nba_2017.csv > small_nba_2017.csv
# Count the number of lines. How many are there?
# If you inspect the first few lines what do you see? head small_nba_2017.csv 

# Part 3: Remove Column Names Before Shuffle
# What happens when you run tail -n +2 nba_2017.csv | head?
# How could use this approach to remove the column heads before shuffling?
# Why would want to do this and how could you append them back on after you shuffle?

#!/bin/bash
file="$1"
truncate="$2"

if [[ $# -eq 0 ]]; then
    echo "Error: No arguments supplied"
fi

if [ ! -f $file ]; then
    echo -e "\nError: "$var" does not exist."
    echo "Error: File not found"
elif [ -f $file ]; then  
    wc -l $file
    head -n 10 $file
    shuf_file=small_nba_2017.csv
    echo -e "\nShuf file: $file"
    shuf -n $truncate $file > $shuf_file
    head $shuf_file
    wc -l $shuf_file
fi