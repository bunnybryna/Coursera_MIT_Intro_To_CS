def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # wrong code, TypeError: 'NoneType' object is not iterable
    bList = []
    for item in aList:
        if type(item) != list:
            bList.append(item)
        else:    
            # .extend() is better 
            bList.extend(flatten(item)) 
    print bList
        
flatten([[1,'a',['cat']],[4,5]]) 