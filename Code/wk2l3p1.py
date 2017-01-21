num = 10
while num > 3:
	num -= 1
	print num
	
num = 10
while True:
	if num < 7:
		print 'Breaking out of loop'
		# break means stop and get out of the loop
		# so when num=6, num<7, printing num will be skipped 
		# there is no printing 6
		# just 'Breaking out of loop','Outside of loop'
		break
	print num
	num -= 1
print 'Outside of loop'
	