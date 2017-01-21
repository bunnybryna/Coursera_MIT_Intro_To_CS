def iterMul(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result

# reduce this problem to a smaller version of the same problem 
# with a case I can solve directly
# recursive step and base case  
def recurMul(a,b):
    if b == 1:
        return a 
    else:
        return a + recurMul(a,b-1)

# factorial n! = n*(n-1)*...*1        
def factI(n):
    res = 1
    while n > 1:
        res = res * n
        n -= 1
    return res 

def factR(n):
    if n == 1:
        return n
    return n * factR(n-1)
    
 # Towers of hanoi
 # think recursively, if I want to move stack of size n, I need to move stack of size n-1 to the spare
 # and then move the bottom one to the target place and then move n-1 to target place
 # smaller problem + base case
def printMove(fr,to):
    print'move from' + str(fr) + 'to' +str(to)
def towers(n,fro,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
    # there are only three spikes 
    # note that the 2nd argument is the spike called from, 3nd is the spike called to, 4th is the spare one 
    # 1st step: towers(n-1,fr,spare,to) means, move n-1, from 'fr' spike to 'spare' spike, and leave 'to' spike spared
    # 2nd step: 1 means the bottom one from 'fr' to 'to' and leave 'spare'
    # 3rd step: towers(n-1,spare,to,fr) means move n-1, from 'spare' to 'to' and leave 'fr'
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)

# fibonacci numbers        
def fib(x):
# assert is to check if that statement true
    assert type(x)== int and x>=0
    if x == 0 or x == 1:
        return 1
    else:
        return fb(x-1)+fib(x-2)
        
# recursion on strings: palindrome
def is Palindrome(s):
# internal procedures
# first to strip out all the spaces and the punctuation
    def toChars(s):
        s = s.lower()
        ans = ''
        for c  in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
    
# global variables
def fibMetered(x):
    global numCalls
    # everytime we call fibMetered, numCalls increase by one
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fibMetered(x-1) + fibMetered(x-2)
def testFib(n):
    for i in range(n+1):
        #  global means numCalls will be bound at the top
        # at the highest level environment
        global numCalls
        # each time through the loop, we reset numCalls to zero
        numCalls = 0
        print 'fib of ' + str(i) + ' = ' + str(fibMetered(i))
        print 'fib called ' + str(numCalls) + ' times'
# fibMetered(0,1)=1,1
# numCalls =1,1       
print testFib(1)
# 012=1,1,2
# 1,1,3
print testFib(2)
# 012345=1,1,2,3,5,8
# 1,1,3,5,9,15
print testFib(5)