def nfruits(aDict,string):
    '''aDict is a non-empty dictionary containing type of fruit and its quantity initially (len(aDict) < 10)
    string is a string pattern of the fruits eaten by Python
    nfruits returns the max quantity of fruits left when Python reached campus
    '''
    ls = len(string)
    # use nested loop to compare the elements in a dictionary and a string 
    # ls-1 is to save the special case(the last one)for later
    for i in range(ls-1):
        letter = string[i]
        for key in aDict:
            # each time he consumes a fruit of one type
            if  key == letter:
                aDict[key] -= 1
            # after that he buys a fruit of each other type
            elif key != letter: 
                aDict[key] += 1    
                
    # special case: only consumption and no ore purchase
    lastLetter = string[ls-1]
    aDict[lastLetter] -= 1
    
    #  use .items() to find the max value
    #  bigFruit is the key,bigCount is the value
    # the other way: 
    # lst = aDict.values()
    # lst.sort(reverse=True)
    # print lst[0]
    # or just max(aDict.values())
    bigFruit = None
    bigCount = None
    for fruit,count in aDict.items():
        if bigCount is None or count > bigCount:
            bigFruit = fruit
            bigCount = count
    return bigCount

#checkcase:
#print nfruits({'A': 1, 'B': 2, 'C': 3}, 'AC')
#print nfruits({'X': 10, 'B': 6, 'U': 7, 'O': 9, 'H': 10}, 'H')
#print nfruits({'P': 6, 'K': 7, 'R': 10, 'S': 6, 'G': 5}, 'SGSS')
#print nfruits({'J': 7, 'U': 8, 'T': 7, 'O': 7}, 'UOUJU')

# another version
def nfruits(fruit, pattern):
    '''
    Takes a dictionary containing fruits as key and
    their amount.
    Returns the maximum quantity of fruits.
    '''
    # Two loops are used, one to substract the fruit eaten
    # and the other to add the fruit bought:
    
    for fruit_eaten in pattern[:-1]:
        fruit[fruit_eaten] -= 1 
        
        for fruit_bought in fruit.keys():
            if fruit_bought != fruit_eaten:
                fruit[fruit_bought] += 1
                
    # The last fruit is eaten but Python does not buy more:  
    
    fruit[pattern[-1]] -= 1 
   
    return max(fruit.values())