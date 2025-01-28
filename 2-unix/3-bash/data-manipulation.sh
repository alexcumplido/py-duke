#!bin/bash

## Reflection Questions ##
# When would you use head vs tail when working with a large log file?
# How could grep help search medical records for certain health conditions?
# What are the tradeoffs between find and locate for searching files?
# When is piping output preferable to redirection to a file?
# How could you select a random subset of lines from a large data file?

## Challenges ##
# Use head, tail and redirection to print the first and last 5 lines of a text file
# Employ grep with flags like -c and -v to count and exclude lines in a file
# Utilize find to locate files modified within the last day
# Chain together grep, wc, and sort using pipes to analyze a log file
# Leverage shuf to extract a random sampling of lines from a large CSV

## Bash Shell techniques for Data
# Truncate - Reduce the size of a file using commands like head and tail
# head -n 5 file.txt
# tail -n 1 file.txt
# Extract columns from a file
# cut -f2 file.csv

#Filter: Search  Search for patterns in a file using grep
# grep "error" file.log

# Find - Search for files/directories recursively
# find . -name "data.csv"

# Locate - Quickly search an index of files rather than the actual filesystem
# locate "*stats"


# Populate a file

# echo "How many lines do you want ? "
# read LINES
# COUNT=1
# while [ $COUNT -le $LINES ]
# do 
#     echo "$COUNT $RANDOM" >> file.txt
#     ((COUNT++))
# done

# Populate a filter
echo "How many line do you want? "
read LINES

declare -a array=("apple" "pear" "cherry")

COUNT=1
while [ $COUNT -le $LINES ]
do
    rand=$[$RANDOM % 3]
    echo "$COUNT ${array[$rand]}" >> filter-file.txt
    ((COUNT++))
done

# Finding a pattern
# Piping grep
# grep apple filter-file.txt | wc -l
# # Using grep flag
# grep -c apple filter-file.txt 

# # Find either pattern
# grep -e apple -e pear filter-file.txt

# grep -e apple -e pear filter-file.txt | wc -l

# grep -c -e apple -e pear filter-file.txt | wc -l

# # Show all lines that DO NOT contain pattern
# grep -v apple filter-file.txt


# Searching data in Bash

find . -name "*.sh"

#Find all executable non visible files
find . -perm /+x ! -name '*' -type f
# command  + pattern of execution + pattern of exclusion + type of search


