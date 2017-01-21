def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            newTup = newTup + (aTup[i],)
    return newTup
    
# another way, smarter way
def oddTuples2(aTup):
    return aTup[::2]