'''
Joshua Wren
09 February 2021
Week Four - Assignment 5 - Image Finder
'''

# Python Standard Library
import os
import sys

# 3rd Party Modules
from PIL import Image
from prettytable import PrettyTable

''' Determine which version of Python '''
if sys.version_info[0] < 3:
    PYTHON_2 = True
else:
    PYTHON_2 = False

def ImageAnalyzer(file):
    fileName = os.path.basename(file)
    absPath = os.path.abspath(file)
    ext = os.path.splitext(absPath)[1]
    fileSize = int('{:}'.format(os.path.getsize(absPath)))
    
    imStatus = ''
    imFormat = ''
    imMode   = ''
    imWidth  = ''
    imHeight = ''
    
    try:
        # Try to open as an image
        with Image.open(absPath) as im:
            # if success, get the details
            imStatus = 'YES'
            imFormat = im.format
            imMode   = im.mode
            imWidth  = im.width
            imWidth  = int(imWidth)
            imHeight = im.height
            imHeight = int(imHeight)
            
            return [imStatus, fileName, fileSize, ext, imFormat, imWidth, imHeight, imMode]
    except:
        imStatus = 'NO'
        
        return [imStatus, fileName, fileSize, ext, 'N/A', 'N/A', 'N/A', 'N/A']

def ImageFinder():
    print("\n***** Image Finder *****\n\n")
    
    if PYTHON_2:
        directory = raw_input("Enter directory to find images in: ")
    else:
        directory = input("Enter directory to find images in: ")
    
    tbl = PrettyTable(['Image?','File Name', 'File Size', 'Ext', 'Format', 'Width', 'Height', 'Type'])
    
    if os.path.isdir(directory):
        dirs = os.listdir(directory)
        
        for eachFile in dirs:
            ''' Set file path '''
            file = os.path.join(directory, eachFile)
            
            imDataList = ImageAnalyzer(file)
            tbl.add_row(imDataList)
    else:
        print(f"'{directory}' is an invalid directory\n")
    
    ''' Print Images Data Table '''
    tbl.align = 'l'
    tbl.hrules = 1
    
    print("\nImages Table as processed:")
    print(tbl.get_string())
    
    print("\nImages Table sorted by File Size Ascending:")
    reversedTbl = tbl.get_string(sortby='File Size', reversesort=True)
    print(reversedTbl)

    print("\nImages Table sorted by File Width Descending:")
    widthTbl = tbl.get_string(sortby='Width', reversesort=False)
    print(widthTbl)

    print("\nScript End")

ImageFinder()
