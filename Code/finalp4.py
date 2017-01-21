def getSublists(L, n):
    '''This function returns a list of all possible sublists in L of length n without skipping elements in L.
    The sublists in the returned list should be ordered in the way they appear in L, 
    with those sublists starting from a smaller index being at the front of the list.
    L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] and n = 4 then your function should return the list
    [[10, 4, 6, 8], [4, 6, 8, 3], [6, 8, 3, 4], [8, 3, 4, 5], [3, 4, 5, 7], [4, 5, 7, 7], [5, 7, 7, 2]]'''
    subList = []
    # outer loop to create L-n+1 times of sublist 
    for i in range(len(L)-n+1):
        nList = []
        # inner loop is to create a sublist with n elements
        for t in range(n):
            nList.append(L[i])
            i += 1
        subList.append(nList)
    return subList

print getSublists([1, 1, 1, 1, 4],2)  
print getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],4)  

def longestRun(L):
    '''This function returns the length of the longest run of monotonically increasing numbers occurring in L. 
    if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5 
    because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7]'''
    if len(L) == 1:
        return 1
    else:    
        maxL = 0
        maxIndStart = 0
        maxIndEnd = 0
        for i in range(len(L)-1):
            length = 0
            indStart = 0
            indEnd = 0
            if L[i] <= L[i+1]:
                indStart = i 
                i += 1
                try:
                    while L[i] <= L[i+1]:
                        indEnd = i+1
                        i += 1
                except:
                    indEnd = i 
                #print indStart,indEnd
                length = indEnd - indStart + 1
            if length > maxL:
                maxL = length
                maxIndStart = indStart
        #print 'final', maxL,maxIndStart  
        return maxL
    
#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])  
#print longestRun([0]) 
#print longestRun([1, 1, 1, 1, 1])      
#print longestRun([10, 4, 6, 8, 3, 4, 5, 7, 7, 2])
#print longestRun([1, 2, 3, -1, -2, -3, -4, -5, -6])          
#print longestRun([-1, -2, -3, -4, -5, -6, -7, 2, 3])    
#print longestRun([1, 3, 5, -1, -3, -5, -7, 1, 3, 5])   
print longestRun([7, 4, 1, -7, -11])
#print longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9])
#print longestRun([1, 0, 0, 0, 4, 5, 1, 2, 9, 4, -1, 0])