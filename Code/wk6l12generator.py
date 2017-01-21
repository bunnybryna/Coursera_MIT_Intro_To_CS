def genTest():   
    yield 1
    yield 2
    
foo = genTest()
print foo.next()    
print foo.next()
# StopIteration execption
# print foo.next()
# we can use a generator inside a loop
# it will continue until gets the StopIteration
for n in genTest():
    print n
    
def genFib():
    fibn1 = 0
    fibn2 = 1
    # fib(n)= fib(n-1)+fib(n-2)
    while True:
        next = fibn1+fibn2
        yield next
        fibn1 = fibn2
        fibn2 = next
        
ha = genFib()
print ha.next()
print ha.next()    
print ha.next()
print ha.next()  
for n in genFib():
    print n