def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    dotProduct returns  sum of the pairwise products of two lists
    '''
    # map() will apply function to every item of iterable and return a list of results
    # listMulti=[listA[0]*listB[0],listA[1]*listB[1],...]
    listMulti = map(multi,listA,listB)
    # calculate the sum 
    total = 0
    for item in listMulti:
        total += item
    return total
    
def multi(a,b):
    return a * b
    
print dotProduct([1,2,3], [4,5,6])    