class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
        
    def __eq__(self,other):
        # return True if coordinates refer to same point in the plane
        # first make sure 'other' is of the same type
        assert type(other) == type(self)
        # better to use getX() than just self.x, protect access to the attributes
        return self.getX() == other.getX() and self.getY() == other.getY()
    
    def __repr__(self):
        #  repr() built-in function to compute the “official” string representation of an object
        # a special method that returns a string that looks like a valid Python expression
        # that could be used to recreate an object with the same value
        return 'Coordinate(' + str(self.getX()) + ', '+ str(self.getY())+ ')'
        
t = Coordinate(10,10)
s = Coordinate(1,1)
q = Coordinate(1,1)
print s == t
print s.__init__(1,1)
print s.getX()
print s == q      