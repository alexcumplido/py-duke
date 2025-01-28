#!/bin/bash

### Reflections questions ###
# What real-world workflows could be automated with bash scripting ?
# How could functions make your scripts more reusable and readable ?
# When ight you use an array versus a dictionary data structure ?
# How can you debug and test scripts locally before production use ?

### Write a script to process a directory of CSV files 
# Create a function to common data tasks like stats or formats
# Build a CLI tool to generate formatted reports
# Use arrays to store command history across sessions
# Test scripts with different inputs and edge cass

### Building a bash script (core components)###
# Statement : ephemeral : interactiva
# Script : automate : run again
# Command Line Toold : Reuse : Input
# Shebang line + debug mdoes + statement and variables

#Strict mode exits shell when if a command fails
# set -e
# #Print shell input lines as they read
# set -v
# #Print command traces before executing it
# set -x

# Bash does not have a concept of return value, so we can capture the eccho

# add() {
#     num1=$1
#     num2=$2
#     result=$((num1 + num2))
#     echo "The result is" $result
#     echo $result
# }

# output=$(add 5 9)

# echo "Results is"
# add $output $output


# A Build function
# B parse input
# C Pass input to Function

# ./cli.sh --count 5 --phrase "hi"

# A Build function
phrase_generator() {
    for((i=0; i<$1; i++));
        do {
            echo "$2"
        }
    done
}

# B parse input
while [[ $# -gt 1 ]]
    do
        key="$1"

        case $key in
            -c|--count)
            COUNT="$2"
            shift
            ;;
            -p|--phrase)
            PHRASE="$2"
            shift
            ;;
        esac
        shift
    done

# C Pass input to Function
phrase_generator "${COUNT}" "${PHRASE}"


