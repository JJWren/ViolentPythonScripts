'''
A password hash value has been intercepted during an investigation.
The hash value is of type md5 and is associated with a password
that is used by the suspect.

Your job is to brute force the password by generating all 
possible password combinations until you identify a matching
password.

A couple of additional details have been discovered.

1) A salt value is prepending to the password when hashing occurs
   and that have value is   &654P
   
2) The suspect is known to use 7 or 8 character passwords

3) The suspect is has a dog named boo

4) His favorite number is 11

5) and his hometown is rome

GIVEN: KNOWN HASH VAUE:  'e182221f74dbce5af2d6b3535cadb39e'
       PASSWORD LEN:  7 OR 8 characters
       SALT: &654P
       Dog: boo
       Favorite Number: 11
       HomeTown: rome
'''

# import standard libraries

import hashlib              # Hashing the results
import time                 # Timing the operation
import itertools            # Creating controled combinations

# Pseudo Constants
AUTHOR = "Joshua Wren"
CREATION_DATE = "02 March 2021"
TITLE = "Week Seven - Assignment 10 - Rainbow Table Generator and Password Cracker"

print(AUTHOR)
print(CREATION_DATE)
print(TITLE, "\n")

#
# Create a list of lower case, upper case, numbers
# and special characters to include in the password table
#

'''Get a yes or no input, recursive'''
def askAgain():
    yesNo = input("Any others? (y/n): ")
    if (yesNo == 'y'):
        return True
    elif (yesNo == 'n'):
        return False
    else:
        askAgain()

bruteForceCharacters = set()
print("Example Characters to Brute Force: 'romeb1'")
tryAgain = True
while (tryAgain):
    string = input("Please input the characters to brute force with no separation between characters: ")
    chars = set(string)
    for char in chars:
        bruteForceCharacters.add(char)
    tryAgain = askAgain()

# Define a hypothetical SALT value
print("\nExample Salt: &654P\nExample Hash: e182221f74dbce5af2d6b3535cadb39e\n")
SALT = input("Please input the known salt: ")
KNOWN_HASH = input("Please input the known hash: ")

# Define the allowable range of password length
PW_LOW  = int(input("Please enter minimum password length (such as '7'): "))
PW_HIGH = int(input("Please enter maximum password length (such as '8'): "))

# Mark the start time
startTime = time.time()

# Create an empty list to hold the final passwords
pwSet = set()

# create a loop to include all passwords
# within the allowable range

print("\nGenerating Passwords ... Please Wait")
pwCnt = 0
for r in range(PW_LOW, PW_HIGH+1):
    
    #Apply the standard library interator
    for s in itertools.product(bruteForceCharacters, repeat=r):
        # append each generated password to the 
        # final list
        pwSet.add(''.join(s))
        pwCnt += 1

# For each password in the list generate
# a hash value by concatenating 
# the salt + password
# then report the resulting password 

print("Possible Passwords Generated: ", pwCnt)
print("Searching for matching HASH: ", KNOWN_HASH)


try:
    passwordFound = False
    for pw in pwSet:
        # Perform hashing of the password
        md5Hash = hashlib.md5()
        pwStr = (SALT+pw)
        pwStr = pwStr.encode('ascii')
        md5Hash.update(pwStr)
        md5Digest = md5Hash.hexdigest()
        if md5Digest == KNOWN_HASH:
            print("\nSUSPECT PASSWORD = ", pw, '\n')
            passwordFound = True
            break
    
    if not passwordFound:
        print("\nPASSWORD NOT FOUND\n")
        
except Exception as err:
    print('File Processing Error', err)

print("\nSCRIPT END")