# 2.6
x = int(raw_input('Enter an integer:))
if x % 2 == 0:
    print ''
	print 'Even'
else:
    print''
	print 'Odd'
print 'Done with conditional'

if x % 2 == 0:
	if x % 3 == 0:
		print 'Divisible by 2 and 3'
	else:
		print 'Divisible by 2 and not by 3'
elif x % 3 == 0:
	print 'Divisible by 3 and not by 2'
else:
	print 'Not divisible by 2 or 3'

if x < y and x < z:
	print 'x is leaset'
elif y < z:
	print 'y is least'
else:
	print 'z is least'
	
