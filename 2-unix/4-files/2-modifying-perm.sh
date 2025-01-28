# mkdir : makes a new directory
# touch : cretes a new empty file 
# mv: moves a file or directory
# cp : copies a file or directory
# rsync : synchronizes files between directories
# chmod : changes file permissions
# zip archives files into a zipped folder

# CRUD



# Database (records) -- CRUD (operations) -- Filesystem


# Crud relations
# Create: touch, mkdir
# Read: cat, less, grep
# Update: mv, tar, zip, chmod
# Delete: rm, rmir


# Synchronize directories
rsync -av /source/dir /dest/dir

# Set permissions to read/write for owner only 
chmod 600 file.txt

# Create a zip archive

#Archiving
zip -r archive.zip file_to_comrpess
cd files
unzip file_to_decompress

# Tar
# archive
tar -zcvf archives/file.tgz source_file

#unarchive
tar -zxvf target_file.tgz

# Archive directory
zip -r test.zip test

# Copy archive to backup location
cp test.zip /backup/

# Synchronize backup  
rsync -av /backup /offsite-backup

## Reflection questions
# What permission settings would you use for a script you want to share on your team ?
# When would you use rsync over cp for copying files ?
# What is the difference between archiving with zip vs tar ?
# How can you recursively create a directory structure ?
# How do permissions affect who can access and execute files ?

## Challenges
# Create a script that touches files for a directory structure
# Write a script to recursively copy a directory with permissions
# Create a cron job that runs a backup script to archive important files
# Restrict permissions on a file and get errors trying to access it
# Use rsync to synchronize two directories in a scriptecho 41-444-5599 | grep '
