from __future__ import print_function

'''
Joshua Wren
22 January 2021
Week Two Assignment 1 - File Processing
'''

import os

print("\n\n##### Script Start #####\n")

# Create empty set for found worms
uniqueWorms = set()

# Open the file, give file variable name
with open("redhat.txt", 'r') as logFile:
    # Iterate through lines of file
    for eachLine in logFile:
        # Split-up strings in each line
        fieldList = eachLine.split()
        # Iterate through each field of current split-up line
        for eachField in fieldList:
            # Check for `worm` in current string field
            if 'worm' in eachField.lower():
                # Add worm to uniqueWorms (sets will not add duplicate values, perfect!)
                uniqueWorms.add(eachField)

# Sort set then print each unique worm name
uniqueWorms = sorted(uniqueWorms)
for eachWorm in uniqueWorms:
    print(eachWorm)
    
print("\n##### Script End #####")