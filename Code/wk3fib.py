# fibonacci numbers        
def fib(x):
# assert is to check if that statement true
    assert type(x)== int and x>=0
    if x == 0 or x == 1:
        return 1
    else:
        return fb(x-1)+fib(x-2)
        
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