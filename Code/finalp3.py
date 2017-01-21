def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''
    # d.values => invDict.keys
    invDict = {}
    # [True,True,True]
    dValList = d.values()
    # [4,2,0]
    dKeyList = d.keys()
    for invKey in dValList:
        # get number of invValues in a list
        invValueLen = dValList.count(invKey)
        invValueList = []
        for i in range(invValueLen):
            # get the invDict.values by indexNum(when i=0,indexNum=0 )
            indexNum = dValList.index(invKey)
            # each invDict.value = dKeyList[indexNum](i=0,invValList=[4])
            invValueList.append(dKeyList[indexNum])
            # chop off the first 'True',dValList=[True,True],dKeyList = [2,0]
            dValList = dValList[indexNum+1:]
            dKeyList = dKeyList[indexNum+1:]
            # sort the list
            invValueList.sort()
        # only add one key-value pair when there is none    
        if invDict.get(invKey) == None:
            invDict[invKey] = invValueList
    return invDict    
    
d = {1:10, 2:20, 3:30} 
print dict_invert(d)
d = {1:10, 2:20, 3:30, 4:30} 
print dict_invert(d) 
d = {4:True, 2:True, 0:True}
print dict_invert(d) 
d={8: 6, 2: 6, 4: 6, 6: 6}
print dict_invert(d)