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
        
n5 = binaryTree(5)
n2 = binaryTree(2)
n1 = binaryTree(1)        
n4 = binaryTree(4)
n8 = binaryTree(8)
n6 = binaryTree(6)
n7 = binaryTree(7)

n5.setLeftBranch(n2)
n2.setParent(n5)
n5.setRightBranch(n8)
n8.setParent(n5)
n2.setLeftBranch(n1)
n1.setParent(n2)
n2.setRightBranch(n4)
n4.setParent(n2)
n8.setLeftBranch(n6)
n6.setParent(n8)
n6.setRightBranch(n7)
n7.setParent(n6)
# depth first search
def DFSBinary(root,fcn):
    stack = [root]
    while len(stack)>0:
        if fcn(stack[0]):
            return True
        else:
            # stack is a list, .pop takes the zeroth element
            temp = stack.pop(0)
            if temp.getRightBranch():
                # put the element at the beginning at the stack
                # stack is a last-in, first-out data structure
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
    return False
    
    
def find6(node):
    rerturn node.getValue() == 6
    
def lt6(node):
    return node.getValue()>6
DFSBinary(n5,find6)
DFSBinary(n5,find10) 
# look at any subtrees
DFSBinary(n2,find6)


# breadth first seach
def BFSBinary(root,fcn):
    queue = [root]
    while len(queue) >0:
        if fcn(queue[0]):
            return True
        else:
            temp = queue.pop(0)
            # difference is put the element at the end
            # queue is a first-in, first-out structure, FIFO
            if temp.getLeftBranch():
                queue.append(temp,getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp,getRightBranch())
    return False

# keep track of the path 
def DFSBinaryPath(root,fcn):
    stack = [root]
    while len(stack)>0:
        if fcn(stack[0]):
            return TrackPath(stack[0])
        else:
            # stack is a list, .pop takes the zeroth element
            temp = stack.pop(0)
            if temp.getRightBranch():
                # put the element at the beginning at the stack
                # stack is a last-in, first-out data structure
                stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0,temp.getLeftBranch())
    return False    
    
def TracePath(node):
    if not node.getParent():
        return [node]
    else:
        return [node]+TracePath(node.getParent)
        
foo = DFSBinaryPath(n5,find6)
print [e.getValue()] for e in foo:
# [6,8,5], from bottom to top

# left<node<right
def DFSBinaryOrdered(root,fcn,ltFcn):
    stack=[root]
    while len(stack)>0:
        if fcn(stack[0]):
            return True
        elif ltFcn(stack[0]):
            temp = stack.pop(0)
            if temp.getLeftBranch():
                # only look for the value in leftside child
                stack.insert(0,temp.getLeftBranch())
        else:
            if temp.getRightBranch():
                # only look in the rightside
                stack.insert(0,temp.getRightBranch())
    return False
    
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
            elif valueFcn(stack[0].getValue())>valueFcn(best.getValue()):
                best = stack[0]
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
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited',visited
    return best
    
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
        
DFSDTree(treeTest,sumValues,WeightsBelow10)        
BFSDTree(treeTest,sumValues,WeightsBelow10)  