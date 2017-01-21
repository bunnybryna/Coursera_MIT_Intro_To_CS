# better to create a superclass to cover all students
# captures common behaviors of subclasses allow us to concentrate methods in a single place
class Student(MITPerson)
    pass

class UG(Student):
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
        
    def getClass(self):
        return self.year
class Grad(Student):
    pass

class TransferStudent(Student):
    pass
    
def isStudent(obj):
    return isinstance(obj,Student)