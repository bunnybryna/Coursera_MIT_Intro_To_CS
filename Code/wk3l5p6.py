# p6 iterative function to compute the length of an input argument
def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for i in aStr:
        count += 1
    return count
      
# p7 recursive function to do the same thing
def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # base case
    if aStr == '':
        return 0
    # recursive step
    else:
    
# p8 use the idea of bisection search to determine if a character is in a string
def isIn(char,aStr):
    length = len(aStr)
    # two base cases, length = 0 or 1
    # if only length = 0, last digit will form an infinite loop
    if length == 0:
        return False
    elif length == 1:
        return False
    #  or don't have to clarity if length is odd/even
    # just use midIndex = len(aStr)/2
    elif length % 2 != 0:
        midInd = (length-1)/2
    elif length % 2 == 0:
        midInd = (length/2)
    midChar = aStr[midInd]
    if char == midChar:
        return True
    if char > midChar:
        return isIn(char,aStr[midInd:])
    if char < midChar:
        return isIn(char,aStr[:midInd])
# p9 check semordnilap
# the wrapper function provided already
def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
# def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string
    
    returns: True if str1 and str2 are semordnilap;
             False otherwise.
    '''
    if len(str1)!= len(str2):
        return False
    elif len(str1) == 1 and len(str2) == 1:
        if str1[0] == str2[0]
            return True
    else:
        if str1[0] == str2[-1]:
            return semordnilap(str1[1:],str2[:-1])
 