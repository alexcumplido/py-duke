# grep
# cut
# uniq
uniq file.txt
uniq -c file.txt
# sort
sort file.txt
# awkgrep

# get a random sample of 10 line from a thousand l
shuf -n 10 amazon_reviews.txt > 10lines.txt

# SED: search and replace
echo "MIXED" | sed 's/MIXED/NEGATIVE/'
shuf -n 200 amazon_reviews.txt | sed 's/NEGATIVE/NEGATIVE/' | awk 'NF>10'

## Reflections questions
# What are some real-word use cases where you might use text processing commands like grep and cut?
# How could piping commands together enable more complex text precssing workflows ?
# What scenarios might awk be more useful for text processing than Bash builtin tools ?
# When would you want to remove duplicate lines ina  file with uniq ?
# What other text processing commands seem useful to learn ?

## Challenge Exercise
# Use grep, cut, and awk to parse a CSV file and extract fields
# Take a log file, extract relevant lines with grep, sort entries chronologically, and remove duplicates
# Write a script that searches a folder of text files to find ones containing a specific keywoard
# Process a large text corpus to tally the frequency of all words used
# Parse text from a webpage by scaping it and extracting relevant contant

