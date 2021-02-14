from __future__ import print_function

'''
Joshua Wren
22 January 2021
Week Two Assignment 2 - File Hashing
'''

import os
import hashlib

directory = "."

fileList      = []
fileHashes    = {}
filepathList  = []

for root, dirs, files in os.walk(directory):

    # Walk the path from top to bottom.
    # For each file obtain the filename 
    
    for fileName in files:
        path = os.path.join(root, fileName)
        fullPath = os.path.abspath(path)
        
        # Add fileName to fileList && Add fullPath to filepathList
        fileList.append(fileName)
        filepathList.append(fullPath)

# Index for iterating through path list
index = 0

# Iterate through fileList
for eachFile in fileList:
    # Open each file (read binary - rb) as fileToHash
    with open(eachFile, 'rb') as fileToHash:
        # Contents of file
        fileContents = fileToHash.read()
        # Create a md5 hashing object of fileContents
        hashObj = hashlib.md5(fileContents)
        # Create digest - finished hashing
        digest = hashObj.hexdigest()
        # Add digest to dictionary as key; filepath as value
        fileHashes[digest] = filepathList[index]
    # Increase index to iterate through filepathList
    index += 1
    
for key, value in fileHashes.items():
    print('\nkey:   ', key)
    print('value: ', value)
