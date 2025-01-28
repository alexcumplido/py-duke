#!/usr/bin/env bash

# Lab Steps
# Examine the provided Bash script and run it with different input options
# Add a new option "--concatenate" that will combine all repeated output into a single string
# Add a new option "--capitalize" to convert phrase to uppercase on each repeat
# Add a new option "--delimiter" to customize the character between repeated phrases

# Reflection Questions

# What does the shift command do when parsing script options?
# Why is echoing the phrase done inside a for loop?
# What operator is used to reverse the phrase string?
# How are options parsed from command arguments?
# Where could additional functionality be added?

# Challenge Exploration

# Explore extending functionality with questions like:
# Can you randomly vary capitalization across repeats?
# How would you save phrase repeats to a new file?
# Can you embed repeat counts into the output phrases?
# What would adding support for multiple phrases require?
# How might this be extended if integrated into a shell environment startup script?

# Counts - Number of times to print phrase
count=5

# Phrase - Message to print 
phrase="hello world"

# Reverse - Whether to reverse string
reverse=0

# Parse options
while [[ $# -gt 0 ]]; do
   key="$1"
   case $key in
     -c|--count)
        count="$2"
        shift   
        ;;
     -p|--phrase)
        phrase="$2"
        shift
        ;;
     -r|--reverse)
        reverse=1
        shift
        ;;
    esac
    shift
done

# Generate phrase 
for ((i=0; i<$count; i++)); do

  # Reverse phrase if reverse flag set
  if [ $reverse -eq 1 ]; then
    rev_phrase=$(echo $phrase | rev)
    echo $rev_phrase 
  else
    echo $phrase
  fi

done

