def a(x,y,z):
    if x:
        return y
    else:
        return z 
def b(q,r):
    return a(q>r,q,r)
 
print a(False,2,3)
print b(3,2)
# it will return function
print a(3>2,a,b)
# it will return function too
print b(a,b)
