def FancyDivide(numbers, index):
    try:
        # 1.index = 4 will fail
        # 3. index = 2,denom = 3 
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        # 2. FancyDivide([0,2,4],2)
        FancyDivide(numbers, len(numbers) - 1)
    except ZeroDivisionError, e:
        print "-2"
    # 4. this time try completes without exceptions
    # 5. so pribt else '1'
    else:
        print "1"
    # 6. finally 1st time when f([0,2,4],2) completes
    # 7. finally 2nd time when the real function completes
    finally:
        print "0"
        
#FancyDivide([0, 2, 4], 1)
print '-'*10
FancyDivide([0, 2, 4], 4)
print '-'*10
#FancyDivide([0, 2, 4], 0)