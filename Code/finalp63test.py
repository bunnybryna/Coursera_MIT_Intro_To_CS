class Person(object):     
    def __init__(self, name):         
        self.name = name     
    def say(self, stuff):         
        return self.name + ' says: ' + stuff     
    def __str__(self):         
        return self.name  

class Lecturer(Person):     
    def lecture(self, stuff):         
        return 'I believe that ' + Person.say(self, stuff)  

class Professor(Lecturer):    
    def __init__(self, name):
        self.name = name 
    def say(self, stuff): 
        return str(self) + ' says: ' + self.lecture(stuff)
    def __str__(self):
        return 'Prof. ' + self.name
        

class ArrogantProfessor(Professor): 
    def lecture(self,stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
         
e = Person('eric') 
le = Lecturer('EEeric') 
pe = Professor('eric') 
ae = ArrogantProfessor('eric') 
#print pe.print_name()
#print pe.print_super_name()
#print ae.say
print e,le,pe,ae
print pe.say('the sky is blue')
# Prof. eric says: I believe that eric says: the sky is blue 
print ae.say('the sky is blue')
# Prof. eric says: It is obvious that I believe that eric says: the sky is blue         