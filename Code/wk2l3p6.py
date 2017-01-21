iteration = 0
count = 0
while iteration < 5:
    for letter in 'hello, world':
        count += 1
    print 'Iteration ' + str(iteration) + ': count is: ' + str(count)
    iteration += 1
# it will print out iteration 0,1,2,3,4: count is 12,24,36,48,60
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in 'hello, world':
        count += 1
    print 'Iteration ' + str(iteration) + ': count is: ' + str(count)
    iteration += 1
# it will print out iteration 0,1,2,3,4: count is 12,12,12,12,12
# because in while loop, everytime count starts as 0 and for loop increments count to 12 
# and move to the next iteration  
    
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + ": count is: " + str(count)
    iteration += 1 
# it will print out iteration 0,1,2,3,4: count is 1,12,1,12,1
# because when iteration=0,2,4, for loop will stop right after count increments to 1
# but when iteration=,1,3, for loop will run to the end when count hits 12