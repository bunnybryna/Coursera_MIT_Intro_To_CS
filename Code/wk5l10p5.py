def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        # difference is here, selSort updated minIndx and minVal
        # it finds the smallest value in unsorted part of the list with minVal and minIndx
        # then switch smallest and L[i]
        # only one swap at the end for each iteration of i
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
        print L     

def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        # difference is here, newSort updates L[i]
        # L[i] remains the smallest element between i and j position
        # and then j+1 moves to next interation 
        # runs more assignments, (n-1) times of swaps for each iteration of i 
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        print L 

#print newSort([1,2,3,4])
print selSort([4,3,2,1])
print newSort([4,3,2,1])
#print newSort([3,1,2,4])             
            