def ndigits(x):
    '''
    ndigits: a function takes one argument,
    an integer x, x > 0 or x < 0
    return: the number of digits in x
    '''
    # to deal with negative x, use abs(x)
    if x < 0:
        x = abs(x)
    # x < 10 is the base case 
    if x < 10:
        return 1
    # recursive step
    else:
        return 1+ndigits(x/10)
