varA = raw_input('Give me A:')
varB = raw_input('Give me B:')
# use try and except to test 
# if raw inputs can be converted to integers
# multiple lines under try
# it will runs until one dies
try:
	intA = int(varA)
	print intA
	intB = int(varB)
	print intB
# if string(s) is found
# the program will stop before doing comparisons
except:
	print 'string involved'
	exit()
	
if intA > intB:
    print 'bigger'
elif intA == intB:
    print 'equal'
else:
    print 'smaller'
print 'done'

# the real code submitted
# put all the conditional statements under try
try:
    intA = int(varA)
    intB = int(varB)
    if intA > intB:
        print 'bigger'
    elif intA == intB:
        print 'equal'
    else:
        print 'smaller'
# if string(s) is found
# the program will stop before doing comparisons
except:
    print 'string involved'
