def polysum(n,s):
    # import math to use pi and tan
    import math
    p = math.pi
    tan = math.tan
    # sum the area and square of the perimeter of the regular polygon
    area = (0.25*n*s*s)/(tan(p/n))
    squareP = (s*n)**2
    #  the function returns the sum, rounded to 4 decimal places
    sum = round(area+squareP,4)
    return sum

#try it out, print polysum(3,1)