def isPalindrome(aString):
    '''
    aString: a string
    a palindrome a word that reads the same forwards or reversed
    '''
    aStr = aString.lower()
    if len(aStr) <= 1:
        return True
    else:
        return aStr[0] == aStr[-1] and isPalindrome(aStr[1:-1])
        
print isPalindrome('e')
print isPalindrome('ame')
print isPalindrome('Parisirap')