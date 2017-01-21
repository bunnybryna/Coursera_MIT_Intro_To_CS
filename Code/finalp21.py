class A(object):
    def foo(self):
        print 'hi'
class B(A):
    def foo(self):
        print 'bye'
        
a = A()
#print a.foo()

def f(n):
    def g(m):
        m = 0
        for i in range(m):
            print m
    for i in range(n):
        g(n)
        print i
        
#print f(1)
#print f(10)
#print f(0)      
  
def foo_one(n):
    """ Assume n is an int >= 0 """
    answer = 1.0
    while n > 1:
        answer *= n
        n -= 1
        print 1
    return answer
    
print foo_one(10)
def foo_two(n):
    """ Assume n is an int >= 0 """
    if n <= 1: 
        return 1.0
    else: 
        print 1
        return n*foo_two(n-1)
        
print foo_two(10)        