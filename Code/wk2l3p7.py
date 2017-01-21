iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1 

# test 1, infinite loop
#for iteration in range(5):
    #count = 0
    #while True:
        #for letter in "hello, world":
            #count += 1
        #print "Iteration " + str(iteration) + "; count is: " + str(count)
        
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print "Iteration " + str(iteration) + "; count is: " + str(count)
        break
        
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)

count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print "Iteration " + str(iteration) + "; count is: " + str(count)