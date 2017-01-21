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

