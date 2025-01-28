#!/bin/bash
# Visual:  hierarchical logical structure 

# Index database base search by metadata
# Locate only knows about updated files on the database
sudo apt install locate
sudo updatedb

#count files
locate -c 

#case insensitive search
locate -i 

# Real Time live search of
# Search the file system for matching files given a criteria.
find . -name reciptes.txt
time find / -name reciptes.txt
find /tmp/ -name foo* -type f -print
find /tmp/ -name foo* -type f -print | xargs /bin/rm -f


# Reader Reflections questions
# When would you choose a live find search over a database search with locate ?
# How could updating locate's database on a schelude improve search relevancy ?
# In what cases would piping find into xarfs be useful for acting on results ?
# If Linux lacks features, what metadata search does MacOS provide ?
# How do conventions in folder structures assist visual search ?

# Reader Challenge Exercises
# Search for files over 1GB on your sisteym using find and xargs
# Setup a cron job or scheluded task to update the locate database weekly
# Find the 3 largest files then archive them with tar via xargs
# Implement a Python script to search files modified in the last day
# Compate locate and finds speeds with time on a few sample queries.


