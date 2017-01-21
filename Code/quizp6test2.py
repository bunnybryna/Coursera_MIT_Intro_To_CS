def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    bList = []
    for item in aList:
        # bList.extend(aList)=>bList = bList + aList
        if type(item) == list:
            bList.extend(flatten(item)) 
        else:
            bList.append(item)       
    return bList
        
flatten([[1,'a',['cat']],[4,5]]) 