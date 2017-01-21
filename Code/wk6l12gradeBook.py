import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name
        
class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum

class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)        
        
class Grades(object):
    ''' A mapping from students to a list of grades'''
    def __init__(self):
        # create empty grade book
        # list of student objects
        self.students = []
        # maps idNum -> list of grades
        self.grades = {}
        # true if self.students is sorted
        self.isSorted = True
    def addStudent(self,student):
        '''Assumes: student is of type Student
           Add student to the grade book'''
        # self.students is a list of student instance
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self,student,grade):
        '''Assumes: grade is a float
        Add grade to the list of grades for student'''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError('Student not in the grade book')
            
    def getGrades(self,student):
        '''Return a list of grades for student'''
        # return copy of student's grade
        # self.grades is a dictionary, but self.grades[key=ID] will return a list for a particular student
        try:
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError('Student not in the grade book')
    def allStudents(self):
        '''Return a list of the students in the grade book'''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        # another way to do this 
        # for s in self.students:
            #print s
        
        
def gradeReport(course):
    '''Assumes: course is of type Grades'''
    report = []
    # for each student in the studentlist
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        # for every grade in the set of grades, adding them up 
        # using getGrades method, use the IDnum as index into the dictionary of grades for this course
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s)+ '\s mean grade is '+str(average))
        except ZeroDivisionError:
            report.append(str(s)+ 'has no grades')
    return '\n'.join(report)
    
ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('John Henry')
g2 = Grad('George Steinbrenner')
six00 = Grades()
six00.addStudent(g1)
six00.addStudent(ug2)
six00.addStudent(ug1)
six00.addStudent(g2)
for s in six00.allStudents():
    six00.addGrade(s, 75)
six00.addGrade(g1, 100)
six00.addGrade(g2, 25)
six00.addStudent(ug3)    
print gradeReport(six00)
# Jane Doe\s mean grade is 75.0
# John Doe\s mean grade is 75.0
# David Henryhas no grades
# John Henry\s mean grade is 87.5
# George Steinbrenner\s mean grade is 50.0