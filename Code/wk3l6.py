def findDivisors(n1,n2):
    # empty tuple
    divisors = ()
    for i in range(1,min(n1,n2)+1):
        if n1%i == 0 and n2 % i == 0:
        # "," in (i,) means it is a tuple, not number i
            divisors = divisors + (i,)
    return divisors

divs = findDivisors(20,100)
total = 0
for d in divs:
    totoal += d
print total

Techs = ['MIT','Cal Tech']
Ivys = ['Harvard','Yale','Brown']
Univs = [Techs,Ivys]
Univs1 = [['MIT','Cal Tech'],['Harvard','Yale','Brown']]
# Univs and Univs1 are not the same
Techs.append('RPI')
# Univs' elements are pointers to other lists
Univs = [['MIT','Cal Tech','RPI'],['Harvard','Yale','Brown']]
Univs1 = [['MIT','Cal Tech'],['Harvard','Yale','Brown']]

# iteration on lists,double iteration
for e in Univs:
    print 'Univs contains '
    print e 
    print ' which contains '
    for u in e:
        print '    ' + u 
        
# append vs flatten
Techs.append(Ivy)
# Techs returns ['MIT','Cal Tech','RPI',['Harvard','Yale','Brown']]
flat = Techs + Ivys
# returns ['MIT','Cal Tech','RPI','Harvard','Yale','Brown']

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

# higher order programming, use functions as arguments 
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
