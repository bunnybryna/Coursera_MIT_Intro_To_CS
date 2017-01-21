def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    # wrong code! See test2.py
    bList = []
    for item in aList:
        if type(item) != list:
            bList.append(item)
            print bList
        else:
            flatten(item)       
        
flatten([[1,'a',['cat']],[[3],4,5]])        