# 'bubble sort' as elements bubble (up or down) one element at a time
# The basic idea is that every time it finds two successive elements in the wrong order, it will swap them
# Because all lists can be sorted, it will eventually run out of things that are in the wrong order
# Another way of thinking is that in each iteration, if an element e is bigger than the one after it, e moves down one location
# Then, e is checked against the next element, and so on, until the algorithm finds an element bigger than e
# so that after n iterations, the list is sorted
def mySort(L):
    clear = False
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                print L  

#print mySort([1,2,3,4])
print mySort([2,2,1,1])
#print mySort([4,3,2,1])
#print mySort([3,1,2,4])     
                
# newSort is, loosely speaking, performing mySort in the opposite direction
# it is moving up the next smallest element to the beginning of the list
# newSort does not examine entries in positions before the ith on the ith iteration
# mySort, however, examines the entire list on each iteration.                
def newSort(L):
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                print L
            j += 1   

print newSort([2,2,1,1])    