def foo(L):
    val = L[0]
    while (True):
        val = L[val]
        
num = ???
#L = [5, 0, 2, 4, 6, 3, 1]
L = [2, 0, 1, 5, 3, 4]
val = 0
for i in range(0, num):
    val = L[L[val]]

print val

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

# ordered list
# improve average complexity but worst case still need to look at every element
def search(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        # once got to a point where the element was bigger than e
        # it can't be in the rest of list
        if L[i] > e:
            return False
    return False        
    
# binary search
def search(L,e):
    def bSearch(L,e,low,high):
        if high == low:
            return L[low] == e
        mid = low + int(high-low)/2
        if L[mid] == e:
            return True
        if L[mid] > e:
            return bSearch(L,e,low,mid)
        else:
            return bSearch(L,e,mid+1,high)
    if len(L) == 0:
        return False
    else:
        return bSearch(L,e,0,len(L)-1)