# Coordinate creates a binding of 'obejct' in global environment to a new frame
# this frame contains attribute bindings, either variables or procedures
# in this case, the attribute is a binding of a name to a procedure
# Coordinate is a subclass of obejct, obejct is a superclass of Coordinate
# Coordinate inherits from the obejct class
class Coordinate(object):
    # we define an __init__ method to provide some initial values 
    # this method, or procedural attribute, belongs to this class, is a procedural attribute
    # self is always the first argument of methods and pointing to the instance
    # Coordinate.__init__ , we can access parts of a class
    def __init__(self,x,y):
        # . is used to access an attribute of an obejct
        self.x = x
        self.y = y
        
# creates a new frame(a instance) and bidings in the frame
# fianlly the result is returned and bound in the global environment
# c.x will return 3
# c.__init__(5,6) will change the bindings for x and y within c
c = Coordinate(3,4)
# will create new instance
origin = Coordinate(0,0)
print c.x, origin.x 
      
# conclusion: when I call a class, I instantiate it. 
# That class points to a frame, and that instantiation creates an instance.
# using that instance as an argument for self,I call any init mehtod
# creates instance variables or attributes. 
# when done, the instance itself is returned as a value 

import math

def sq(x):
    return x*x

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x 
        self.y = y 
    # __str__ method will return a str
    # __ and __ is for not overriding the other string method
    # it will convert any instance into a string
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
    # create method in a class that will apply to any instance
    def distance(self,other):
        return math.sqrt(sq(self.x - other.x)+sq(self.y-other.y))   
        
c = Coordinate(3,4)    
# without __str__ method, it will print out like <__main__.Coordinate instance at 0x0000000002632E08>
# now <3,4>    
print c
# <class '__main__.Coordinate'>
# means the name of class is Coordinate and c is an instance of class Coordinate
print type(c)
# <class '__main__.Coordinate'> <type 'type'>
# means that Coordinate is a class, type is a version of 'type'
print Coordinate, type(Coordinate)
# use isinstance() to check if an object is an instance of a particular type
# check if c is an instance of Coordinate
# print True
print isinstance(c, Coordinate)
     
     
class intSet(object):
    ''' An intSet is a set of integers 
    The value is represented by a list of ints, self.vals
    Each int in the set occurs in self.vals exactly once.'''
    def __init__(self):
        # create an empty set of integers
        self.vals = []
        
    def insert(self,e):
        # assumes e is an integer and inserts e into self
        if not e in self.vals:
            self.vals.append(e)
    
    def __str__(self):
        # returns a string representation of self
        self.vals.sort()
        # separator.join(sequence) method returns a string, which is the concatenation of the strings in the sequence sequence
        # separator provided will separate each elements 
        # s = '-',seq = ('a','b','c'),print s.join(seq) will be a-b-c
        # [str(e) for e in ['a','b','c']] = ['a','b','c']
        return '{'+','.join([str(e) for e in self.vals])+'}'
            
    def __member__(self):
        return (self.e in intList)
    
    def __remove__(self):
        if self.e in intList:   
            intList.remove(self.e)
        else:
            print 'error'
        
        
        
           
        