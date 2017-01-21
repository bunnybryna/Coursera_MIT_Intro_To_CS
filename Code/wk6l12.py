import datetime
class Person(object):
    def __init__(self,name):
        # create a person called name
        self.name = name
        self.birthday = None
        # take that string and split it everywhere I find a space' '
        self.lastName = name.split(' ')[-1]
    def getLastName(self):
        # return self's last name
        return self.lastName
    def __str__(self):
        # return self's name
        return self.name
    def setBirthday(self,month,day,year):
        # set self's birthday to birthdate
        self.birthday = datetime.date(year,month,day)
    def getAge(self):
        # return self's current age in days
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days  
    def __lt__(self,other):
        # return True if self's name is lexigoraphically less than other's name
        if self.lastName == other.lastName:
            # if they have same last name, check first name using string comparison
            return self.name < other.name
        return self.lastName < other.lastName

me = Person('Bryna Zhao')
me 
print me
print me.getLastName()
print me.setBirthday(7,25,1987)
print me.getAge()
her = Person('Cher')
print her
print her.getLastName()
pList = [me,her]
print pList
for p in pList: print p
pList.sort()

# MITPerson is a subclass of Person, a specialization of Person
# MITPerson has access to all of the characters of a Person
class MITPerson(Person):
    # nextIdNum is a class attribute, a attribute belongs to the class not to instance of class
    # init is a attribute that belongs to the instance of class 
    nextIdNum = 0
    def __init__(self,name):
        # initialize Person attributes, inheriting __init__ method from Person
        Person.__init__(self,name)
        # new MITPerson attributes: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1 
    def getIdNum(self):
        return self.idNum
        # init and lt two methods shadow the Person methods
        # they are creating an instance of MIT Person using Person attritbutes to set up bindings
    
    def __lt__(self,other):
        return self.idNum < other.idNum
        
p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')  
# because I update ID number everytime inside the class
# when  call the init method, it's creating a new unique binding for each values

print p1,p2,p3,p4
print p1.getIdNum()
print p2.getIdNum()
print p1<p2
print p2<p3
# False, p4<p1 => p4.__lt__(p1),we use lt method associated with p4, a Person
# so we compare them based on name
print p4<p1
# it will get a Traceback
# p1<p4 => p1.__lt__(p4), use lt method associated with p1, a MITPerson
# compare with IDNum, but p4 doesn't have an ID
# shadowing overrides other methods
# print p1<p4

class UG(MITPerson):    
    def __init__(self,name,classYear):
        MITPerson.__init__(self,name)
        self.year = classYear
    def getClass(self):
        return self.year
# Grad will inherit from MITPerson, 
# pass means it doesn't have any unusual methods of its own        
class Grad(MITPerson):
    pass
    
class TransferStudent(MITPerson)
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)

s1 = UG('Fred',2016)
s2 = Grad('Angela')
print isStudent(s1)
print isStudent(s2)    
me = MITPerson('Eric')
print isStudent(me)