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