# Every procedure that has a yield statement is a generator
# a procedure has only one yield statement that will never be executed
# then the procedure is still a generator

def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

print type(g1)
print type(g2)
print g1.next()
print g2.next()