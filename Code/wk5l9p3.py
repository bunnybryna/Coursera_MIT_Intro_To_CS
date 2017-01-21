# best case 2 steps, L is empty
# worst case 1+n(1+3n)+1=3n2+n+2
# n2
def program1(L):
    # 1 step
    multiples = []
    # n times of iteration
    # within each outer loop, one step( assignment to x) plus inner loop 3n
    # n(1+3n)
    for x in L:
        # n times of iteration, 3n
        # within each inner loop, 3 steps(assignment to y,multiplication,and appending)
        for y in L:
            multiples.append(x*y)
    # 1 step
    return multiples
    
# best case 2 steps, L is empty
# worst case 1+n(1+4n)+1=4n2+n+2, L = [2,2,2,...]   
# n2
def program2(L):
    squares = []
    # n times of iteration and within outer loop, one step plus inner loop 4n
    for x in L:
        # n times of iteration, within inner loop
        # 4 steps(assignment to y,conditional check,mulplication and appending)
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares    

# best case 2 steps
# worst case  ,L1 = [2,2,2,...],L2 = [0,1,3,4,5,...,2] 
# 1+n(1+n+1)+1=n2+2n+2  
# n2
def program3(L1, L2):
    intersection = []
    # n times of iteration, within outer loop 1 assignment and 1 conditional check
    # in the worst case, elt is the last element of L2, the check takes n step 
    # and add one append operation, n*(1+n+1)
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection    
    
# big O notation gives an upper bound on asymptotic growth of a function
# generally, a nested loop structure has O(n**2) complexity
'''If running time is a sum of multiple terms, keep one with the largest growth rate (so n**3 + 100n**2 + 500,000 is O(n**3)).
If the remaining term is a product (eg 3n**2), drop any multiplicative constants (so 3n**2 is O(n**2))
if you have a function that takes a constant number of steps - regardless of the size of the input
the function is O(1), even if it takes 3,000,000 steps every time! 
because the function does not take any additional time as the input grows large.'''
    