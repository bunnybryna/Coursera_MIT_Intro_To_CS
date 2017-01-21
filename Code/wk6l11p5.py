class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self,other):
        newList = []
        for e in self.vals:
            if e in other.vals:
                newList.append(e)
        return '{' + ','.join([str(e) for e in newList]) + '}'
        
        # another way initialize a new intSet
        commonSet = intSet()
        for val in self.vals:
        # use two pre-defined attributes member() and insert()
        # make sure member is used on other and insert is used on commonSet
            if other.member(val):
                commonSet.insert(val)
            return commonSet
            
    # need double underscore to differentiate from len() method
    def __len__(self):
            count = 0
        for e in self.vals:
            count += 1
        return count
        # or just return len(self.vals)

setA = intSet({-20,-19,-6,-5,0,3,10,11,14,16})        
setB = intSet({-19,-15,-13,6,7,10,12,15,16,20})
print setA.intersect(setB)        