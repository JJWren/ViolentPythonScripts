# Python Standard Library
import os
import sys
import re

# Import Python 3rd Party Libraries
from prettytable import PrettyTable

# Pseudo Constants
AUTHOR = "Joshua Wren"
CREATION_DATE = "16 February 2021"
TITLE = "Week Five - Assignment 7 - Regex Extractor"

CHUNK_SIZE = 1024

print(AUTHOR)
print(CREATION_DATE)
print(TITLE)

def main():
    # regex for email pattern
    ePatt = re.compile(b'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}')
    # regex for url pattern
    uPatt = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w.\.?=%&=\-@$,]*')
    
    '''Getting unique emails and urls, and their occurances through use of dictionaries'''
    emailDict = {}
    urlDict = {}
    tblEmails = PrettyTable(['Emails', 'Occurances'])
    tblURLs = PrettyTable(['URLs', 'Occurances'])
    
    targetFile = input("Please input a filepath: ")
    
    if os.path.exists(targetFile):
        if os.path.isfile(targetFile):
            try:
                with open(targetFile, 'rb') as binaryFile:
                    while True:
                        chunk = binaryFile.read(CHUNK_SIZE)
                        if chunk:
                            emails = ePatt.findall(chunk)
                            urls = uPatt.findall(chunk)
                
                            for eachEmail in emails:
                                lowercaseEmail = eachEmail.lower()
                                lowercaseEmail = lowercaseEmail.decode("utf-8")
                                
                                try:
                                    occurances = emailDict[lowercaseEmail]
                                    occurances += 1
                                    emailDict[lowercaseEmail] = occurances
                                except:
                                    emailDict[lowercaseEmail] = 1
                                    
                            for eachURL in urls:
                                lowercaseURL = eachURL.lower()
                                lowercaseURL = lowercaseURL.decode("utf-8")
                                
                                try:
                                    occurances = urlDict[lowercaseURL]
                                    occurances += 1
                                    urlDict[lowercaseURL] = occurances
                                except:
                                    urlDict[lowercaseURL] = 1
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
        
    # format tables and print them
    tblEmails.align["Emails"] = "l"
    tblURLs.align["URLs"] = "l"
    tblEmails.reversesort = False
    tblURLs.reversesort = False
    tblEmails.sortby = "Emails"
    tblURLs.sortby = "URLs"
    
    for key, value in emailDict.items():
        tblEmails.add_row([key, value])
    for key, value in urlDict.items():
        tblURLs.add_row([key, value])
    print(tblEmails)
    print(tblURLs)
    
    
if __name__ == '__main__':
    main()    
    print("\nScript End")