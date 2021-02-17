# Python Standard Library
import os
import sys
import re

# Import Python 3rd Party Libraries
from prettytable import PrettyTable

# PSEUDO_CONSTANTS
AUTHOR = "Joshua Wren"
CREATION_DATE = "16 February 2021"
TITLE = "Week Five - Assignment 7 - Regex Extractor"

CHUNK_SIZE = 16384

print(AUTHOR)
print(CREATION_DATE)
print(TITLE)

def main():
    wPatt = re.compile(b'[a-zA-Z]{5,15}')
    
    wordDict = {}
    fileWords = PrettyTable(["Word", "Occurances"])
    
    fileName = input("Please input a filepath: ")
    
    if os.path.exists(fileName):
        if os.path.isfile(fileName):
            try:    
                # Begin file parsing; add unique words to dictionary along with occurance values
                with open(fileName, "rb") as binFile:
                    while True:
                        chunk = binFile.read(CHUNK_SIZE)
                        if chunk:
                            words = wPatt.findall(chunk)
                            for eachWord in words:
                                lWord = eachWord.lower()
                                lWord = lWord.decode("utf-8")
                                try:
                                    occurances = wordDict[lWord]
                                    occurances += 1
                                    wordDict[lWord] = occurances
                                except:
                                    wordDict[lWord] = 1
                                    
                        else:
                            break
            except Exception as err:
                errStr = str(err)
                errMsgEnd = errStr.find(":")
                errMsg = errStr[:errMsgEnd]
                print(errMsg)
        else:
            if not os.path.isfile(absPath):
                reason = "Not a File"
            else:
                reason = "Access Rights"
            print(reason)
    else:
        print("Something went wrong:")            
                
    # Load dictionary elements into PrettyTable
    for key, value in wordDict.items():
        fileWords.add_row([key,value])
    
    # Format and print pretty table
    fileWords.reversesort = True
    fileWords.align["Word"] = "l"
    fileWords.align["Occurances"] = "c"
    print("Results:\n")
    print(fileWords.get_string(sortby="Occurances"))
    
if __name__ == '__main__':
    main()    
    print("\nScript End")