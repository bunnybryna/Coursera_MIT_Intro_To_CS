def isPal(x):
    assert type(x) == list
    # 8. temp = x will change x's value when temp is changed 
    temp = x[:]
    # 5. put in another immediately above the reverse
    # 6. temp.reverse doesn't function, it loses ()
    # print temp,x
    temp.reverse()
    # 7. aliasing bug, after the reverse(), temp is reversed but so is x
    # print temp,x = [b,a],[b,a]
    # 4. realize there is a bug in isPal
    # pick a point halfway through isPal and put in print statement
    # print temp,x
    if temp == x:
        return True
    else:
        return False
        
# 9. after the test, go back and check silly on earlier things
def silly(n):
    result = []
    for i in range(n):
        # 3. spot a bug: doing an initialization of result everytime through the loop
        # need to move it outside the loop
        # result = []
        elem = raw_input('Enter element: ')
        result.append(elem)
        # 2. move the printing inside the loop print result
    # 1. pick a spot about halfway through the code,binary idea
    # and put in a print statement,print(result)
    if isPal(result):
        print 'Yes'
    else:
        print 'No'