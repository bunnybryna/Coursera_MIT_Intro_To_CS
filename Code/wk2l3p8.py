#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0

# the problem is that after guess hits 5.0, it will not fit that if statement and will stay 5.0 
# 5.0 <25, will make the while loop go on forever
#while guess <= x:
    #if abs(guess**2 -x) >= epsilon:
        #guess += step
        #print guess

#if abs(guess**2 - x) >= epsilon:
    #print 'failed'
#else:
    #print 'succeeded: ' + str(guess)
    
# this program will succeed when x=25
# but when x=23, square root=4.7958,guess will never equal to 4.7958
# this program will fail
x = 23
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print 'failed'
else:
    print 'succeeded: ' + str(guess)