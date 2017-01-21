def program1(x):
    # 1 step
    total = 0
    # 3 steps inside the loop, 1000 times of iteration,3000
    # i=0, assignment;total + i, addition and total = ,assignment) 
    for i in range(1000):
        total += i
    # best case 1 step, while x <= 0, still gets 1 step of comparison
    # worst case 5n+1, 5 steps inside loop, but still need 1 more step to check if x>0
    while x > 0:
        x -= 1
        total += x
    # last step
    return total,count
 
# best case, 2003
# worst case, log2(n)*5+2008 
def program2(x):
    total = 0
    # 2 steps inside loop, 1000 times of iteration
    for i in range(1000):
        total = i
    # best case 1 step for comparison
    # worst case (log2(n)+1)*5+1,5 steps inside loop, log2(n)+1 times of iteration 
    # plus one more step for comparison
    while x > 0:
        x /= 2
        total += x
    # last step
    return total 

# best case 3 steps, L is empty list
# worst case 7n+2, L is a list with it elements sorted in increasing order, [1,3,5,7,...]   
# 2+3n+4n-1+1=7n+2
def program3(L):
    # 2 steps
    totalSum = 0
    highestFound = None
    # 3n,3 steps inside loop, n times interation
    for x in L:
        totalSum += x
    # first time, 3 steps(1 for assignment, run if and assignment)
    # nest (n-1) times, 4 steps(1 for assignment, run if no assignment and run elif and assignment)
    # 3 + 4(n-1) = 4n-1
    for x in L:
        if highestFound == None:
            highestFound = x
        elif x > highestFound:
            highestFound = x
    # last step
    return (totalSum, highestFound)    