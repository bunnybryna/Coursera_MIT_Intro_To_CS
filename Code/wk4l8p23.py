def FancyDivide(numbers, index):
    try:
        try:
            denom = numbers[index]
            for i in range(len(numbers)):
                numbers[i] /= denom
        except IndexError, e:
            FancyDivide(numbers, len(numbers) - 1)
        else:
            print "1"
        finally:
            print "0"
    # index=0 will result the second try fail
    # and will fall in the second exception, print -2         
    except ZeroDivisionError, e:
        print "-2"
        
FancyDivide([0, 2, 4], 1)
print '-'*10
FancyDivide([0, 2, 4], 4)
print '-'*10
FancyDivide([0, 2, 4], 0)        