class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
# print w1 will get Traceback, global x is not defined
w1 = Weird(X,Y)
print w1.getX()
w2 = Wild(X,Y)
# 7
print w2.getX()
# 8
print w2.getY()
w3 = Wild(17, 18)
# 17
print w3.getX()
# 18
print w3.getY()
w4 = Wild(X, 18)
# 7
print w4.getX()
X = w4.getX() + w3.getX() + w2.getX()
# X = 7+17+7
print X
# still 7, because X only updated in the main frame
# but w4 instance stays untouched
print w4.getX()
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
# 44
print Y
# so does Y in w2 instance, 8
print w2.getY()