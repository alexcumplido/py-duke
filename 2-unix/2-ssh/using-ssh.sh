
# Securely connecting to a Linux instance using SSH

# Reflection Questions
# Why is SSH more secure than telnet?
# When would you use key-based over password authentication with SSH?
# What commands allow SSH to copy files or execute scripts on a remote system?
# How does port forwarding enable accessing services only available internally on remote networks?
# What troubleshooting steps would you take if failing to connect to an instance with SSH?

# SSH Key Generation
ssh-keygen -t rsa -b 4096 -C "myemail@example.com"  

# Basic SSH Connection
ssh -i /path/to/private_key.pem username@server_ip_or_dns

# File Transfer with SCP 
scp -i /path/to/private_key.pem /local/file.txt username@server:/remote/destination  

# Local Port Forwarding 
ssh -L 8888:remote_server:80 username@server_ip_or_dns

# Secure remote development with ssh and Visual Studio Code

# Reflection Questions
# What are the benefits of using VSCode Remote SSH versus a local text editor or IDE for remote development?
# How does the SSH extension simplify extension management when working on remote hosts?
# When would you use SSH port forwarding to access services on a remote host?
# What are some good ways to work with source code from a remote SSH host on your local machine?
# If building an application for deployment on a Linux server, how could Remote SSH aid in development?

# Challenges
# Connect to a remote SSH server from VSCode
# Install a Python extension on the remote host
# Forward a web server port from the remote host to local port 8888
# Open a terminal on the remote host and run some Linux commands
# Debug a Node.js application running on the remote host

# Generate SSH Key Pair
ssh-keygen -t rsa -b 4096

# SSH Remote Connection
ssh username@remote_host 

# Port Forwarding
ssh -L 8888:remote_host:80 username@remote_host

# Lesson reflection

# Reflection Questions
# What are the security advantages of SSH over unencrypted protocols like telnet or FTP?
# In what scenarios would SSH keys be preferred over password-based authentication?
# How could port forwarding be useful for web development or testing code destined for production servers?
# What SSH client and server components need to be installed before you can connect to a Linux instance?
# What troubleshooting steps would you take if failing to connect to an instance via SSH?

# Challenges
# Generate an SSH keypair on your local system for authentication
# Use SSH to execute the uptime command on a remote server
# Transfer a local file to your home directory on a cloud Linux instance
# Forward a web server from an instance to your local port 8888
# Debug an SSH connection failure by checking security groups, networking, keys etc.

#!/bin/bash

# Function to generate SSH key pair
generate_ssh_keys() {
    ssh-keygen -t rsa -b 4096 -C "your_email@domain.com"  
}

# Function to connect to instance and run command  
ssh_remote_command() {
    ssh -i /path/to/private_key.pem username@server_ip_or_dns uptime
}

# Function to securely copy file to instance
scp_file() {
    scp -i /path/to/private_key.pem /local/file.txt username@server:/remote/destination
}

# Function to forward remote port to local port
ssh_port_forward() {
    ssh -L 8888:remote_server:80 username@server_ip_or_dns
}

# Function to check SSH connection issues
debug_ssh() {
    # Check security group rules, NACLs, keys etc  
}