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
    # note that __str__ only takes one argument the intSet itself
    def __str__(self):
        # returns a string representation of self
        self.vals.sort()
        # separator.join(sequence) method returns a string, which is the concatenation of the strings in the sequence sequence
        # separator provided will separate each elements 
        # s = '-',seq = ('a','b','c'),print s.join(seq) will be a-b-c
        # [str(e) for e in ['a','b','c']] = ['a','b','c']
        return '{'+','.join([str(i) for i in self.vals])+'}'
            
    def member(self,e):
        # returns True if e is in self, and False otherwise
        return e in self.vals
    
    def remove(self,e):
        # removes e from self and raises valueError if e is not in self
        try:
            self.vals.remove(e)
        except:
            raise ValueError (str(e) + ' not found')
            
s = intSet()
print s
s.insert(3)
s.insert(4)
s.insert(3)
print s
print s.member(5)
print s.member(3)        
s.insert(6)
print s 
s.remove(3)
#print s
#s.remove(3) will raise an error
print s.__str__()