def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
#print search([], 4)   
#print search([1,2,3,4,5],5)    
    
# same result    
def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False    

# same result too    
def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False    

# correct only when L is non-empty and e is in L   
def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    # when L=[],L[1:] is always[]
    else:
        return search3(L[1:], e)    

#search3([], 4)    

def newsearch(L, e):
    length = len(L)
    for i in range(length):
        if L[length-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False    
print newsearch([], 4)   
print newsearch([0,2],0)     