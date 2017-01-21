try:
    f = open('grades.txt')
except IOError,e:
    print "Can't open grades file:" + str(e)
    sys.exit(0)
except ArithmeticError,e:
    raise ValueError('Bug in grades calculation ' + str(e))
    
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError,e:
        print 'division by zero!' + str(e)
    except TypeError:
        divide(int(x),int(y))
    # else is executed when try completes with no exceptions
    else:
        print 'result is',result
    # finally is always executed after try,else and except 
    # even if break,continue or return
    finally:
        print 'executing finally clause'
        
        
def getSubjectStats(subject,weights):
    return [[elt[0],elt[1],avg(elt[1],weights)]
        for elt in subject]
        
def dotProduct(a,b):
    result = 0.0
    for i in range(len(a)):
        result += a[i]*b[i]
    return result

def avg(grades,weights):
# if no grades for a student, we won't get an error
    try:
        return dotProduct(grades,weights)/len(grades)
    except ZeroDivisionError:
        print 'no grades data'
        # or we could decide a student without grades will get a zero
        return 0.0
    # suppose some grades are letter grades    
    except TypeError:
        newgr = [convertLetterGrade(elt) for elt in grades]
        return dotProduct(newgr,weights)/len(newgr)
        
def convertLetterGrade(grade):
    if type(grade) == int:
        return grade
    elif grade == 'A':
        return 90.0
    elif grade == 'B':
        return 80.0
    elif grade == 'C':
        return 70.0
    elif grade == 'D':
        return 60.0
    else:
        return 50.0

def getRatios(v1,v2):
    '''Assumes: v1 and v2 are lists of equal length of numbers 
    ReturnsL a list containing the meaningful values of v1[i]/v2[2]'''
    ratios = []
    for index in range(len(v1)):
        try:
            ratios.append(v1[index]/float(v2[index]))
        except ZeroDivisionError:
            # 'NaN' is short for no a number
            ratios.append(float('NaN')) 
        except:
            raise ValueError('GetRatios called with bad arg')
    return ratios
    
try:
    print getRatios([1.0,2.0,7.0,6.0],[1.0,2.0,0.0,3.0])
    print getRatios([],[])
    print getRatios([1.0,2.0], [3.0])
except ValueError, msg:
    print msg
    
# assertions & defensive programming   
def avg(grades,weights):
# an empty list for grades will raise an AssertionError
# assert means as long as it's true, carry on
# the following message will print out
    assert not len(grades) == 0,'no grades data'
    assert len(grades) == len(weights),'wrong number grades'
    newgr = [convertLetterGrade(elt) for elt in grades]
    result = dotProduct(newgr,weights)/len(newgr)
    assert 0.0 <= result <= 100.0
    return result