x = 3
# 1.need to set iteration variables outside the loop
ans = 0
itersLeft = x
# 2.need to test that variable to determine when done
while(itersLeft != 0):
    # ans is incremented,0,3,6,9
	ans = ans + x
	# 3. need to change the variable within the loop
	# itersLeft is decremented,3,2,1,0 stop
	itersLeft = itersLeft - 1
print (str(x) + '*' + str(x) + '=' + str(ans))

# cube root 
x = int(raw_input('Enter an integer:'))
ans = 0
while ans ** 3 < x:
    ans = ans + 1
if ans ** 3 != x:
    print str(x) + ' is not a perfect cube'
else:
    print 'Cube root of ' + str(x) + ' is ' + str(ans)
	
# negative version
x = int(raw_input('Enter an integer:'))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
if ans ** 3 != abs(x):
    print str(x) + ' is not a perfect cube'
else:
	if x < 0:
		ans = - ans
	print 'Cube root of ' + str(x) + ' is ' + str(ans)
	
# cleaned version using range()
x = int(raw_input('Enter an integer:'))
for ans in range(0,abs(x)+1):
    if ans ** 3 == abs(x):
	    break
if ans ** 3 != abs(x):
	print str(x) + ' is not a perfect cube'
else:
	if x < 0:
		ans = - ans
	print 'Cube root of ' + str(x) + ' is ' + str(ans)

# converting decimal integer to binary     
if num < 0:
    isNeg = True
    num = abs(num)
# True or False is to keep track of negative number 
# so as to put the nagative sign back when it's done
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
# code corrected, should be num>0 instead of num>2 
# 19=1*2**4+0*2**3+0*2**3+1*2**1+1*2**0
#! first take remainder relative to 2,and divide 19 by 
# shifting to the right, and get 10011
while num > 0:
    # str(),concatenation of the string,to avoid numbers 0 and 1 adding up 
    # str(num%2)is to get the next bit, num/2 is to shift right
    result = str(num%2) + result
    num = num / 2
if isNeg:
    result = '-' + result
print result


# converting fractions to binary,commments are on the separate program
x = float(raw_input('Enter a decimal number between 0 and 1:'))

p = 0
while((2**p)*x)%1 != 0:
    print 'Remainder = ' + str((2**p)*x-int((2**p)*x)))
    p += 1

num = int(x*(2**p))

result = ''
if num == 0:
    result = '0'
while num >0:
    result = str(num%2) + result
    num = num /2

for i in range(p-len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print 'The binary representation of the decimal ' + str(x) + ' is ' + str(result)

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2-x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1 
print 'numGuesses = ' + str(numGuesses)
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print str(ans) + ' is close to the square root of ' + str(x)
    
#bisection search
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0 
high = x 
ans = (high + low)/2.0 
while abs(ans**2-x) >=epsilon:
    print 'low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans)
    numGuesses += 1 
    if ans ** 2 < x:
        low = ans 
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuesses = ' + str(numGuesses)
print str(ans) + ' is close to square root of ' + str(x)    

# computing powers
x = float(raw_input('Enter a number:'))
p = innt(raw_input('Enter an integer power:'))

result = 1
for turn in range(p):
    print 'iteration:' + str(turn) + current result: ' + str(result)
    result = result * x 
    
# use a function to do it
def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print 'iteration:' + str(turn) + 'current result: ' + str(result)
        result = result * x 
    return result

# twoPower(2,8)=256
# n=8,4,2,x=4,16,256    
def square(x):
    return x*x
def twoPower(x,n):
    while n > 1:
        x = square(x)
        n = n/2
    return x 

def findRoot1(x,power,epsilon):
    low = 0 
    high = x 
    ans = (high+low)/2.0 
    while abs(ans**power -x) > epsilon:
        if ans**ans <x:
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
   