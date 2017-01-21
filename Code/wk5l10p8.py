def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False    
     

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False 
print search([], 4)  
print newsearch([], 4)  
print search([1,2,3], 2)  
print newsearch([1,2,3], 2) 
print search([0,2,4,6],6)
print newsearch([0,2,4,6],6)
     