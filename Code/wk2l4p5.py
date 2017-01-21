def clip(lo, x, hi):
    ans = -((max(lo,x,hi)+min(lo,x,hi))-lo-x-hi)
    return round(ans,2)

# 1st run,x<lo<h
clip(1,0,2)
# 2nd run,lo<hi<x
clip(0,2,1)
# 3rd run,low<x<hi 
clip(0,1,2)    
# return min(max(x,lo),hi)