# Reflection Questions
#In what cases might you want to pipe commands rather than run them sequentially?
#When would redirecting output be useful in a script?
#How could chaining commands with conditionals affect script logic flow?
#Why append files instead of overwriting them?
#Which control characters do you find most useful for command editing

# Challenge Exercises
# Pipe the output of ls to wc -l to count files in the home directory.
# Redirect the output of pwd to a file called location.txt.
# Echo a message only if a certain file exists using conditional execution.
# Append a list of running processes to an existing processes.txt log file.
# Use control characters to edit a long running command more easily.

#!/bin/bash
ls | wc -l
pwd > location.txt

[ -f location.txt ] && echo "location.txt exist"
# ls -l /usr/bin | wc -l > out.txt
# date >> out.txt
# ls out.txt && echo "out.txt exist"
# pwd > location.txt
# cat out.txt && cat location.txt
# rm out.txt && rm location.txt