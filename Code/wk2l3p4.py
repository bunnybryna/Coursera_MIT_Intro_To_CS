num = 10
for num in range(5):
    print num
# it will print 0,1,2,3,4,4
# because now num=4
print num

for var in range(20):
    if var % 4 == 0:
        print var
    if var % 16 == 0:
        print 'Foo!'
# it will print out 0,'Foo!',4,8,12,16,'Foo!'
# don't forget 0%int == 0
# every var goes to 1st if and test and then 2nd if
# and move to the next var,so 0 fits both if, and printed as 0,'Foo!'