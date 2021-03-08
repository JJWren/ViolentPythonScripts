# Python Standard Library
import requests
import os
import re   # regex

# Import Python 3rd Party Libraries
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# Pseudo Constants
AUTHOR = "Joshua Wren"
CREATION_DATE = "16 February 2021"
TITLE = "Week Six - Assignment 9 - Web Scraper, Find the Bad Stuff"
IMG_SAVE = "./SCRAPED_IMAGES/"  # Directory to store images

# Create the directory if necessary
if not os.path.exists(IMG_SAVE):
    os.makedirs(IMG_SAVE)

print(AUTHOR)
print(CREATION_DATE)
print(TITLE, "\n")

def main():
    '''This could be re-used for scraping through a list of websites'''
    table = PrettyTable(['Link','Title', 'Page Links', 'Image Links'])
    table.title = 'Webpage Information'
    webInfoList = []
    
    print("Example Website:\nhttps://casl.website")
    target = input("Please input a website: ")
    '''Link Column'''
    webInfoList.append(str(target))
    
    page = requests.get(target)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    '''Gets title from page'''
    print("\nExtracting Title from: ", target)
    print("Please Wait\n")
    
    pageTitle = soup.find('title')
    print(f"Page Title: {pageTitle.string}")
    '''Title Column'''
    webInfoList.append(str(pageTitle.string))
    
    
    '''Gets all links from page'''
    print("\nExtracting Links from: ", target)
    print("Please Wait\n")
    
    pageLinks = soup.findAll('a', href=True)  # Find the link (a) tags with reference (href)
    linkUrlList = []
    for link in pageLinks:      # Process and display each link
        try:
            linkURL = link['href']
            print("Processing Link:", linkURL, end="")
            if linkURL[0:4] != 'http':       # If URL path is relative
                linkURL = target+linkURL         # try prepending the base url
    
            response = requests.get(linkURL)                 # Get the link from the URL
            linkName = os.path.basename(linkURL)
            
            print(f"  >> Link: {linkURL}")
        except Exception as err:
            print(linkURL, err)
            continue
        linkUrlList.append(linkURL)
    '''Concatenate all the linkURLs into a string to display in PrettyTable col'''
    s1 = '\n'    # separator
    s1 = s1.join(linkUrlList)     # join by separator
    '''Page Links Column'''
    webInfoList.append(str(s1))
        
    
    '''Gets all images from page'''
    print("\nExtracting Images from: ", target)
    print("Please Wait\n")
    
    pageImages = soup.findAll('img')  # Find the image tags
    imgUrlList = []
    for image in pageImages:      # Process and display each image
        try:
            imgURL = image['src']
            print("Processing Image:", imgURL, end="")
            if imgURL[0:4] != 'http':       # If URL path is relative
                imgURL = target+imgURL         # try prepending the base url
    
            response = requests.get(imgURL)                 # Get the image from the URL
            imageName = os.path.basename(imgURL)            
            
            imgOutputPath = IMG_SAVE+imageName
            
            with open(imgOutputPath, 'wb') as outFile:
                outFile.write(response.content)
                
            # Save the image
            print(f"  >> Saved Image: {imgOutputPath}")
        except Exception as err:
            print(imgURL, err)
            continue
        imgUrlList.append(imgURL)
    '''Concatenate all the imgURLs into a string to display in PrettyTable col'''
    s2 = '\n'    # separator
    s2 = s2.join(imgUrlList)     # join by separator
    '''Image Links Column'''
    webInfoList.append(str(s2))
    
    
    '''PrettyTable Stuff'''
    table.add_row(webInfoList)
    table.align = 'l'
    print('\n')
    print(table)
    '''Output table to txt file'''
    table_txt = table.get_string()
    with open('wrenJ_WK6-1_PrettyTableOutput.txt','w') as file:
        file.write(table_txt)
        
if __name__ == '__main__':
    main()    
    print("\nScrape Script Complete")