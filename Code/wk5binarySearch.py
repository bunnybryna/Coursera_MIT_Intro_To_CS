def search(L,e):
    def bSearch(L,e,low,high):
        # note that L[low] == e is not an assignment, it returns a bool
        # when high=low it's the last step 
        # only need to check if L[low]orL[high] = e or not
        # and the answer is the answer for the whole function
        if high == low:
            return (L[low] == e)
        # low+int(high-low)=(high+low)/2
        # this way mid is always a positive int
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
        
print search(['c','t','u','z'],'z')