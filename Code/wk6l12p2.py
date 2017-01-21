class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print "A.x"
    def y(self):
        print "A.y"
    def z(self):
        print "A.z"

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print "B.y"
    def z(self):
        print "B.z"

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print "C.y"
    def z(self):
        print "C.z"
# When resolving a reference to an attribute of an object that's an instance of class D, Python first searches the object's instance variables then uses a simple left-to-right, depth first search through the class hierarchy.
# In this case that would mean searching the class C, followed the class B and its superclasses (ie, class A, and then any superclasses it may have, et cetera).
class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print "D.z"
        
obj = D()
# compare obj.a and obj.y()
# obj.a => D.__init__=> C.__init then B.__init 
# => self.a = 4 then A.__init__ and self.a = 2
# => self.a = 4 then self.a = 1 then self.a = 2
# so finally self.a = 2,obj.a = 2
# conclusion: B.__init__ redefines (or overwrites) the mapping for the variable name   
# note just the mapping gets redefined, B and C instances are still there
print obj.a     
print obj.b
print obj.c
print obj.d  
obj.x()
# however obj.y() => D.y() => C.y() => print 'C.y'(if no c.y(),keep searching in B.y and A.y)
# .y() keep seeking the name until finds it, left-to-right, depth first rule applied
# conclusion: difference is obj.a looking for instance variable while obj.y() looking for method
obj.y()
obj.z()