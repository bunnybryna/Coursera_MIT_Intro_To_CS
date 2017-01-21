
def removeDups(L1,L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
            
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1,L2)
# it will return L1 = [2,3,4],why?
# when we mutate a list, we change its length

# better version is to clone, we will get Li = [3,4]
# loop over a copy of L1, but mutate the real L1
# L1Start = L1 will not work
def removeDumBetter(L1,L2):
    Li1Start = Li1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)
            
 higher order programming, use functions as arguments 
# L is a list, f a function, mutates L by replacing each element
# L = [1,-2,3.4]
# applyToEach(L,abs),applyToEach(L,int),applyToEach(L,fact),applyToEach(L,fib)
def applyToEach(L,f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
# instead of applying a function to a list of numbers
# here we apply a list of functions to a number  
# applyFuns([abs,int,fact,fib],4)     
def applyFuns(L,x):
    for f in L:
        print(f(x))
# simple form, a unary function 
map(abs,[1,-2,3,-4])
# general form an n-ary function, respectively applies min to each pair
# 1 and 2,28 and 57,36 and 9
L1 = [1,28,36]
L2 = [2,57,9]
map(min,L1,L2)
# print [1,28,9]

# dictionaries
# cann't index by number, have to index by key
monthNumbers = {1:'Jan',2:'Feb','Mar':3,'Feb':2,'Apr':4,'Jan':1,3:'Mar'}
# insertion
monthNumbers['Apr'] = 4
collect = []
for e in monthNumbers:
    collect.append(e)
# same with monthNumbers.keys()

# keys can be complex,keys must be immutable, tuple is fine but not a list
myDict = {(1,2):'twelve',(1,3):'thirteen'}
            