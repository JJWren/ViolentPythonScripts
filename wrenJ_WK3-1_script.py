'''
Joshua Wren
28 January 2021
Week Three - Assignment 4 - File Processing Object
'''
from __future__ import print_function
import os
import sys
import time
from binascii import hexlify

''' Determine which version of Python '''
if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False

class FileProcessor:
    
    def __init__(self):
        self.filePath = ''
        self.fileSize = ''
        self.mode = ''
        self.modifiedTime = ''
        self.createTime = ''
        self.header = ''
        self.lastErr = ''
        
    def SetFilePath(self, filePath):
        ''' Set the file path if valid 
            Obtain file size and timestamps
            return True if valid and set the self.filePath object variable
        '''
        if os.path.isfile(filePath):
            if os.access(filePath, os.R_OK):
                self.filePath = filePath
                stats = os.stat(self.filePath)
                self.fileSize = stats.st_size
                self.mode = stats.st_mode
                self.modifiedTime = time.ctime(stats.st_mtime)
                self.createTime = time.ctime(stats.st_atime)
                self.lastErr = ''
                return True
            else:
                self.filePath = ''
                self.lastErr = 'Invalid File Path'
            
    def GetFileHeader(self):
        with open(self.filePath, 'rb') as binFile:
            firstTwenty = binFile.read(20)
            hexStr = hexlify(firstTwenty)
            self.header = hexStr
            
    def PrintFileDetails(self):
        print("Path:               ", self.filePath)
        print("File Size:          ", '{:,}'.format(self.fileSize), "Bytes")
        print("File Mode:          ", self.mode)
        print("File Modified Time: ", self.modifiedTime)
        print("File Created Time:  ", self.createTime)
        print("File Header:        ", self.header)
        
        
print("File Processor Demonstration")

if PYTHON_2:
    directory = raw_input("Enter directory to process files from: ")
else:
    directory = input("Enter directory to process files from: ")


if os.path.isdir(directory):
    dirs = os.listdir(directory)
    
    for eachFile in dirs:
        ''' Set file path '''
        file = os.path.join(directory, eachFile)
        ''' Instantiate instance of the class: FileProcessor '''
        obj = FileProcessor()
        
        print(f"\nProcessing File {file}...\n")
        
        if obj.SetFilePath(file):
            if obj.SetFilePath(file):
                obj.GetFileHeader()
                obj.PrintFileDetails()
            else:
                print("Processing Failed: ", obj.lastErr)
        else:
            print("File Name Err: ", obj.lastErr)
else:
    print(f"'{directory}' is an invalid directory")
    
print("\nScript End")

