def findRoot1(x,power,epsilon):
    low = 0 
    high = x 
    ans = (high+low)/2.0 
    while abs(ans**power -x) > epsilon:
        print ans
        if ans**power <x:
            low = ans 
        else:
            high = ans
        ans = (high+low)/2.0
    return ans

def findRoot2(x,power,epsilon):
    # don't do even powered roots for negative number
    if x<0 and power%2 ==0:
        return None
    # if x<0,low=x,high=0, and high will stay 0
    # do the search in the negative range
    # findRoot1,high=x, will lead ans further away 
    low = min(0,x)
    high = max(0,x)
    ans = (high+low)/2.0
    while abs(ans**power -x) > epsilon:
        print ans
        if ans**power <x:
            low = ans 
        else:
            high = ans
        ans = (high+low)/2.0
    return ans


def findRoot3(x,power,epsilon):
    """ x and epsilon int or float,power an int
        epsilon>0 & power>=1
        return a float y s.t. y**power is within epsilon of x.
        if such a float does not exist, returns None"""
    if x<0 and power%2 ==0:
        return None
    # when x is fractional,root is between 0 and 1
    low = min(-1,x)
    high = max(1,x)
    ans = (high+low)/2.0
    while abs(ans**power -x) > epsilon:
        print ans
        if ans**power <x:
            low = ans 
        else:
            high = ans
        ans = (high+low)/2.0
    return ans
    
#print findRoot1(25.0,2,0.001)
#print findRoot1(27.0,3,0.001)
#print findRoot2(-27.0,3,0.001)
print findRoot3(0.25,2,0.001)
