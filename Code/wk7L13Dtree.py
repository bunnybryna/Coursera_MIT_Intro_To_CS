class binaryTree(object):
    def __init__(self,value):
        self.value = value
        self.leftBranch = None
        self.rightBranch = None
        self.parent = None
    def setLeftBranch(self,node):
        self.leftBranch = node
    def setRightBranch(self,node):
        self.rightBranch = node
    def setParent(self,parent):
        self.parent = parent
    def getValue(self):
        return self.value
    def getLeftBranch(self):
        return self.leftBranch
    def getRightBranch(self):
        return self.rightBranch
    def getParent(self):
        return self.parent
    def __str__(self):
        return self.value
       
    
def buildDTree(sofar,todo):
# sofar is the list of things we decide to include, todo is the list of things we haven't decide
    if len(todo) == 0:
        return binaryTree(sofar)
    else:
        withelt = buildDTree(sofar+[todo[0]],todo[1:])
        withoutelt = buildDTree(sofar,todo[1:])
        here = binaryTree(sofar)
        here.setLeftBranch(withelt)
        here.setRightBranch(withoutelt)
        return here
    '''power set
         []
    [a]      []
[a,b] [a]  [b] []'''

def DFSDTree(root,valueFcn,constraintFcn):
    stack = [root]
    # save my best solution so far
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        # constraintFcn is to check if still I have room, can I add it in?
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
                print best.getValue()
            elif valueFcn(stack[0].getValue())>valueFcn(best.getValue()):
                best = stack[0]
                print best.getValue()
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
         # if there is no room for this value, just chop it off and move on       
        else:
            stack.pop(0)
    print 'visited', visited
    return best
    
def BFSDTree(root,valueFcn,constraintFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print best.getValue()
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print best.getValue
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited',visited
    return best
#[value,weight]    
a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]
treeTest = buildDTree([],[a,b,c,d])

def sumValues(lst):
    vals = [e[0] for e in lst]
    return sum(vals)
        
def WeightsBelow10(lst):
    wts = [e[1] for e in lst]
    return sum(wts)<= 10
        
foo = DFSDTree(treeTest,sumValues,WeightsBelow10) 
print foo.getValue()       
BFSDTree(treeTest,sumValues,WeightsBelow10)  

def DFSDTreeGoodEnougth(root,valueFcn,constraintFcn,stop):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
                print best.getValue()
            if stop(best.getValue()):
                print 'visited',visited
                return best
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
        else:
            stack.pop(0)
    print 'visited',visited
    return best
    
def atLest15(lst):
    return sumValues(lst) >= 15
    
depth = DFSDTreeGoodEnougth(treeTest,sumValues,WeightsBelow10,atLest15)
print depth.getValue()

# only build the tree as I need it
def DTImplicit(toConsider,avail):
# return value of a solution and solution itself
    # if there is nothing left to consider or no more room 
    if toConsider == [] or avail == 0:
        result = (0,())
    # if the first element' weight is bigger than avail
    # result will not include the first element
    elif toConsider[0][1] > avail:
        result = DTImplicit(toConsider[1:],avail)
    else:
        # nextItem = [value,weight]
        nextItem = toConsider[0]
        # a solution with the element
        withVal,withToTake = DTImplicit(toConsider[1:],avail-nextItem[1])
        # adding the element in
        withVal += nextItem[0]
        # a solution without the element
        withoutVal,withoutToTake = DTImplicit(toConsider[1:],avail)
        if withVal > withoutVal:
            # withToTake+(nextItem,) 
            # for example, ([2,3],)+([4,5],) just like(2,)+(3,)=(2,3) 
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result
    
stuff = [a,b,c,d]

val, taken = DTImplicit(stuff, 10)

print ''
print 'implicit decision search'
print 'value of stuff'
print val
print 'actual stuff'
print taken


def DFSBinaryNoLoop(root,fcn):
    stack = [root]
    # add a list to keep track what node that has been checked
    seen = []
    while len(stack) > 0:
        print 'at node' + str(queue[0].getValue())
        if fcn(stack[0]):
            return True
        else:
            temp = stack.pop(0)
            seen.append(temp)
            if temp.getRightBranch():
                if not temp.getRightBranch() in seen:
                    stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                if not temp.getLeftBranch() in seen:
                    stack.insert(0,temp.getLeftBranch())
                    
    return False     

n3.setLeftBranch(n5)
n5.setParent(n3)
# will end up with an infinite loop
DFSBinary(n5, find6)   
DFSBinaryNoLoop(n5,find6)
 