#!/usr/bin/env python3.7

import os

# Get the current working directory
directory = os.getcwd()

# Create an empty list to store file information
files_list = []

# Loop through each file in the directory and create a dictionary with the file information
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    file_size = os.path.getsize(file_path)
    last_modified = os.path.getmtime(file_path)
    
    file_info = {
        "File name": file_name,
        "Path": file_path,
        "File size": file_size,
        "Last Modified": last_modified
    }

# Add the dictionary to the list
    files_list.append(file_info)
    
# Print the list of files
print(*files_list, sep="\n")