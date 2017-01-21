def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]


def SimpleDivide(item, denom):
   return item / denom

# rewrite SimpleDivide
# when dividing by 0,FancyDivide returns a list with all 0 elements   
def SimpleDivide(item, denom):
    try:
        return item / denom
    except  ZeroDivisionError:
        return 0