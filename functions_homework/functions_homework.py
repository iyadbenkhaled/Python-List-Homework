# Checking whether a given is a palindrome or not
def isPalindrome(word):
    originalWord = word.upper() # Saving it for printing
    word = ''.join(word.split(' ')).upper() # Removing spaces from the string, joining it again and uppercasing it. I tried not to use regex.
   
    for index in range(0, len(word)):
        if not (word[index] == word[-1-index]):
            return originalWord + " is not a palindrome."
    return originalWord + " is a palindrome."

# Checking if a number is prime
def isPrime(n):
    if n == 1:
        return "1 is not a prime."
    else:
        sqrt_n = n ** (1/2)
        for i in range(2, int(sqrt_n)+1):
            if n%i == 0:
                return str(n) + " is not a prime."
        return str(n) + " is a prime."

# Check whether a number is in a given range
# The range is given just like in mathematics, [1,2] or ]1,2], in the form of a string with not spaces
# Call: isInRange(2, "[1,2[") -> return false
def isInRange(n, range):
    rangeElements = range.split(',')
    inf = float(rangeElements[0][1:])
    sup = float(rangeElements[1][0:-1])
    
    if range[0] == "[":
        if range[-1] == "]":
            return inf <= n and sup >= n
        elif range[-1] == "[":
            return inf <= n and sup > n
        
    elif range[0] == "]":
        if range[-1] == "]":
            return inf < n and sup >= n
        elif range[-1] == "[":
            return inf < n and sup > n
        
# Factorial
def factiorial(n):
    if n == 1:
        return 1
    else:
        return n*factiorial(n-1)

# Reversing String
def reverseString(myString):
    myReversedString = ""
    for i in range(0, len(myString)):
        myReversedString += myString[-1-i]
    return myReversedString

# Sum
def sum(myList):
    mySum = 0
    for i in myList:
        mySum += i
    return mySum

# Max of three number
def maxOfThree(a, b, c):
    return max( max(a, b) , c)