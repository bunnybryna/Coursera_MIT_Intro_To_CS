# p1 use interation function to calculate the exponential 
def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result * base
        exp -= 1
    return result
    
# p2 use recursive function to do the same thing
# note the base case is exp = 0 instead of exp = 1
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0: 
        return 1
    #no need elif exp == 1:
    #return base
    return base * recurPower(base,exp-1)
    
# p3 another version of recursive function, even and odd
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # you've got two recursive functions, you need two base cases
    # exp = 0, exp = 1
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp > 0 and exp % 2 == 0:
        return recurPowerNew(base*base,exp/2)
    if exp > 1 and exp % 2 != 0:
        return base * recurPowerNew(base,exp-1)
        
# p4 iterative function to get the greatest common divisor of two positive integers
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.'''
    divisor = min(a,b)
    while divisor >= 1:
        if a % divisor == 0 and b % divisor == 0:
            break 
        divisor -= 1
    return divisor 

 # p5 recursive funciton to get gcd   
 def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # gcd(6,3)=gcd(3,3)=gcd(3,0)=3
    # gcd(4,3)=gcd(3,1)=gcd(1,0)=1
    if b == 0:
        return a
    return gcdRecur(b,a%b)

