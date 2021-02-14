'''
Name: Joshua Wren
Date: January 11, 2020
Week One Assignment - Simple String Searching
'''

excerpt = " Another one got caught today, it's all over the papers. Teenager\
            Arrested in Computer Crime Scandal, Hacker Arrested after Bank Tampering\
            Damn kids.  They're all alike"

''' Your work starts here '''
def stringSearch(string):
	print(f"##### Starting string search... #####\n")
	
	# lowercase the string
	lowercasedStr = string.lower()
	print(f"String as Lowercase: {string}")
	
	# get length of string
	lengthOfString = len(lowercasedStr)
	print(f"Length of String: {lengthOfString}")
	
	# turn string into list of words
	stringList = lowercasedStr.split()
	print(f"String as List: {stringList}")
	
	# get length of list
	numOfStringWords = len(stringList)
	print(f"Length of String List: {numOfStringWords}")
	
	# sort list alphabetically
	stringList.sort()
	print(f"Sorted String List: {stringList}")
	
	# find specified strings in list and number of occurances of each
	scandalCount = 0
	arrestedCount = 0
	erCount = 0
	goodCount = 0
	tomorrowCount = 0
	for word in stringList:
		if "scandal" in word:
			scandalCount+=1
		elif "arrested" in word:
			arrestedCount+=1
		elif "er" in word:
			erCount+=1
		elif "good" in word:
			goodCount+=1
		elif "tomorrow" in word:
			tomorrowCount+=1	
	return print(f'\nThe following strings appear "x" number of times:\nscandal - {scandalCount}\narrested - {arrestedCount}\ner - {erCount}\ngood - {goodCount}\ntomorrow - {tomorrowCount}\n\n##### End Search #####')

stringSearch(excerpt)
