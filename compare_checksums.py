#!/usr/bin/env python3
#Checksum verifier. Verifies that two copies of the same file have the same MD5 checksum. 
#Can be used to verify that a file has been accurately and completely copied to another location.
#Runs from terminal command line: python3 <script> <file> <file>

import hashlib
import os
import sys

def get_checksum(file):
    """function opens a file, generates the file's MD5 checksum, and prints the filepath/result"""
    print("File: ", file)
    file_info = open(file,'rb').read()
    checksum = hashlib.md5(file_info).hexdigest()
    print("MD5 checksum: ", checksum)
    print()

#Files, input into terminal
filepath1 = sys.argv[1]
filepath2 = sys.argv[2]


#Compare output for each file
if get_checksum(filepath1) == get_checksum(filepath2):
    print ("Your files have been verified. The MD5 checksums are the same.")
else:
    print("Your files have not been copied accurately. The MD5 checksums are different.")
