#x = 25
x = 12345
epsilon = 0.01
step = epsilon**2
#step = 0.5,2 will skip over answers
numGuesses = 0
ans = 0.0
# ans <=x will tell me when I'm done
while abs(ans**2-x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1 
print 'numGuesses = ' + str(numGuesses)
if abs(ans**2-x) >= epsilon:
    print('Failed on square root of ' + str(x))
else:
    print str(ans) + ' is close to the square root of ' + str(x)
    