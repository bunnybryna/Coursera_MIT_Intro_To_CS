# 5:30 will print out 
# we print self.time not time
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print self.time

clock = Clock('5:30')
clock.print_time()

# 10:30 will print out
# clock in line 9 is not the same thing of clock in line 9
# better to give parameters, local variables and attributes different names
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print time

clock = Clock('5:30')
clock.print_time('10:30')

# 10:30 will print out
# boston_clock and paris_clock are two names for the same object
# aliasing
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	print self.time

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()