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
# It's the same thing with lists. If you have a list, list_a and you do this:
#list_a = [1,2,3]
#list_b = list_a
#list_b[0] = 'x'
#print list_a
#You get:['x', 2, 3]