#!/usr/bin/env python3
#Program generates a MD5 checksum for a single file or a directory of files
#Runs from terminal command line: python3 <script> <file or directory>

import hashlib
import os
import sys

def get_checksum(file):
    """function opens a file and generates the file's MD5 checksum"""
    print("Filepath: ", file) #print filename for reference
    file_info = open(file,'rb').read() #read file
    checksum = hashlib.md5(file_info).hexdigest() #get checksum
    print("MD5 checksum: ", checksum)
    print()

#user input from terminal
user_input = sys.argv[1]

#if user_input is a directory
if os.path.isdir(user_input):
    for f in os.listdir(user_input):
        filepath = user_input+"/"+f #Pass each filename from directory into script
        get_checksum(filepath)

#if user_input is for a single file
else:
    get_checksum(user_input)
