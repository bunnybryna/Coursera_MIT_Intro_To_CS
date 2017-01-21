# write a procedure which returns the sum of the number of values associated with a dictionary
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for keys in aDict:
        length = len(aDict[keys])
        count = count + length
    return count 

# another way to do this using values
def howMany(aDict):
    result = 0
    # aDict.values() is a list of lists
    for value in aDict.values():
        result += len(value)
    return result
    
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxLength = 0
    for value in aDict.values():
        length = len(value)
        maxLength = max(length,maxLength)
        
    for key,value in aDict.items():
        if len(value) == maxLength: 
            return key
    
# cleaner code using one loop
    maxKey = None
    maxLength = 0
    for key,value in aDict.items():
        if len(value) >= maxLength:
            maxLength = len(value)
            maxKey = key
    return maxKey    