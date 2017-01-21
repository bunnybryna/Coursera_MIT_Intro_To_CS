#def dict_interdiff(d1, d2):
def dict_interdiff():
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    # remember to remove d1 and d2
    d1 = {1:30, 2:20, 3:30, 5:80}
    d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
    dictInter = dict()
    dictDiff = dict()
    # dictInter: key=common key in d1 & d2
    # the list of keys in dictInter
    interKey = []
    for key in d1.keys():
        if key in d2.keys():
            interKey.append(key)
    # dictInter: value = f(v1,v2),v1=d1[common],v2=d2[common]
    value1 = []
    value2 = []
    for key in interKey:
        value = d1[key]
        value1.append(value)
    for key in interKey:
        value = d2[key]
        value2.append(value)
    # remeber to change min to f
    # the list of values in dictInter
    interValue = map(min,value1,value2)
    for i in range(len(interKey)):
        dictInter[(interKey[i])]=interValue[i]
    # dictDiff: key only in d1 or d2
    # dictDiff: value = d1[onlykey],d2[onlykey]
    for key,value in d1.items():
        if key not in d2:
            dictDiff[key]=value
    for key,value in d2.items():
        if key not in d1:
            dictDiff[key]=value
    tupleDI = (dictInter, dictDiff)
    return tupleDI


print dict_interdiff()    