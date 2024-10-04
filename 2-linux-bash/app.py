import subprocess

# Call Bash pipeline and store result
result = subprocess.run("ls -l | wc -l", shell=True, text=True, capture_output=True)  

print(result.stdout)