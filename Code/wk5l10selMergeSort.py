def search(L,e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False
    
# selection sort 
# inner loop is O(len(L)),outer loop is O(len(L))    
# complexity is O(len(L)2) or quadratic
def selSort(L):
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        # while loop to find the smallest element in the right of i
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        # standard way to do a switch
        # eg, L=[2,3,1,4],temp=L[0],L[0]=L[2],L[2]=temp
        # L = [1,3,2,4]
        temp = L[i]
        L[i] = L[minIndx]
        L[minInd] = temp
        
# merge sort  
# complexity is O(len(L))
def merge(left,right,compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare(left[i],right[j]):
            result.append(left[i])
            i += 1
         else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

# complexity is number of calls to merge() * number of calls to merge()
# which is O(len(L))* log(len(L))    
import operator
def mergeSort(L,compare=operator.lt):
    if len(L)<2:
        returnL[:]
    else:
        middle = int(len(L)/2)
        left = mergeSort(L[:middle],compare)
        right = mergeSort(L[middle:],compare)
        return merge(left,right,compare)