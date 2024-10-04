#Lab steps
# Handle the case when no file argument is passed
# Print the file size in a human-readable format
# Print the last modified timestamp of the file
# Update the script to allow viewing multiple files passed as arguments
# Ensure the script works properly with invalid files or paths

# Challenge exploration
# Explore how to view contents of a CSV file
# Research how to exclude specific files from being processed
# Investigate custom formatting options for file size and date
# Consider how to add interactivity with input prompts
# Think through integrating help documentation in the scrip

#Reflection Questions
# In what cases might the script fail if a file check isn't done first?
# Why is handling errors important when writing CLI programs?
# How could this script be extended to support more file types?
# What are some challenges in designing CLI tools?
# How could this viewer script assist in your workflow?

#!/bin/bash
#"cmd -option target"

if [[ $# -eq 0 ]]; then
    echo "Error: No arguments supplied"
fi

# Usage: viewer.sh <file>
for var in $@;
do
  if [ ! -f "$var" ]; then
    echo "Error: "$var" does not exist."
    echo "Error: File not found"
    exit 1
  fi
done

for var in $@;
do
  # last access
  echo -e "\nLast modification to the file:"
  stat -c %y "$var"

  # file contents
  echo "Contents of $var:"
  cat "$var"

  # file info
  echo -e "\nFile info:"
  ls -l "$var"
done
