#trying to build a prime number finder
#only designed to work on positive numbers
#I want users to eventually be able to input top and bottom numbers to search
#1 is being defined as non-prime for this 

#variables
prime = True #assigning this variable a value to start with

aNumber = input("What's the smallest number that you'd like me to test?") #The number being tested, starts at the bottom and increments throughout the program
maxSize = input("what's the largest number that you'd like me to test?") #largest number to be tested

#test that entries are numbers
try:
    divisor = int(aNumber)-1 #dividing by a number less than the tested number, this decriments through the program
except:
    print("Python thinks you didn't enter a smaller number. Let's just call it 2.")
    aNumber = 2
    divisor = int(aNumber)-1
else:
    aNumber = int(aNumber)
    divisor = int(aNumber)-1

try:
    maxSize = int(maxSize)
except:
    print("Python thinks that you didn't enter a larger number. Let's call it ",aNumber)
    maxSize = int(aNumber)
else:
    maxSize = int(maxSize)

#test the aNumber is a postive number
if aNumber < 1: 
    print("You entered 0 or a negative number, I'm bumping you up to 1 to start")
    aNumber = 1
if maxSize < 1: 
    print("You entered 0 or a negative number, I'm bumping you up to 2 to start")
    maxSize = 2

#quick test for starting numbers larger than ending number
if aNumber > maxSize: 
    print("your smallest number (",aNumber,") is larger than your largest number)",maxSize,") so I'm going to swap them")
    foo = aNumber
    aNumber = maxSize
    maxSize = foo

while (aNumber <= maxSize):
    if divisor < 1: prime =  False #tests that we're not using
    while (divisor > 1 and prime == True):
        if aNumber % divisor == 0:prime = False
        divisor -= 1
    if prime == True:    print ("Prime number found: ", aNumber)
    prime = True
    divisor = aNumber
    aNumber +=1
   