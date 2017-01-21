def linearSearch(L,x):
    for e in L:
        if e == x:
            return True
     return False
     
# 5n+2,when n gets large,2 becomes irrelavant 
     def fact(n):
    # 1 for assignment
    answer = 1
    # 1 for test, 2 for multiplication and assignment 
    # another 2 for substraction and assignment
    # each time go through the loop, we have 5 steps, so 5n
    while n>1:
        answer *= n
        n -= 1
    # 1 for return 
    return answer 

# if x=100,eps=0.0001, it will take one billion iterations of the loop
# 8 steps inside the loop, 8 times the number of times through the loop    
def sqrtExhaust(x,eps):
    step = eps ** 2
    ans = 0.0
    while abs(ans**2 - x)>= eps and ans <= max(x,1):
        ans += step
    return ans
    
# compared with bisection approach, it will only take 30 iterations of the loop
# 10 steps inside the loop
# 1 billion or 8 billion vs 30 or 300, it is the number of iterations (the growth in the size of problem)that matters     
def sqrtBi(x,eps):
    low = 0.0 
    high = max(1,x)
    ans = (high + low)/2.0 
    while abs(ans**2-x) >=epsilon:
        if ans ** 2 < x:
            low = ans 
        else:
            high = ans
        ans = (high + low)/2.0
    return answer    
# conclusion:multiplicative factor (number of steps within loop) irrelevant

# complexity is 1000+2x+2x2(if each line takes one step)
# if x is small, 1000 dominates,if x is large, x square dominates
def f(x):
    for i in range(1000):
        ans = i 
    for i in range(x):
        ans += 1 
    for i in range(x):
        for j in range(x):
            ans += 1
    
# logarithmic complexity
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    # 6 steps inside the loop,how many times through loop depends on 
    # how may times can i divided by 10,O(lg[i])
    while i > 0:
        result = digits[i%10] + result 
        i = i/10
    return result
    
# linear complexity,O(len(s))
def addDigits(s):
    val = 0
    for c in s:
        val += int(c)
    return val
    
# linear complexity, complexity can depend on number of recursive calls
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
        
# quadratic complexity O(len(L1)*len(L2))
# worst case when len(L1)=len(L2), none of L1 elements in L2,O(len(L1)^2)
def isSubset(L1,L2):
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
            if not matched:
                return False
        return True
        
# Quadratic complexity
def intersect(L1,L2):
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 = e2:
                tmp.append(e1)
    res = []
    # this step is to strip the duplicates
    for e in tmp:
        if not (e in res):
            res.append(2)
    return res
    
# exponential complexity
def genSubsets(L):
    # L = [a],smaller=genSubsets([])=[[]]
    # extra = [a],small+extra=[]+[a]=[a],new.append([a]),new=[a]
    # return [[],[a]]
    res = []
    if len(L) == 0:
        # return a list of empty list
        return [[]]
    # get all subsets without last element    
    smaller = genSubsets(L[:-1])
    # create a list of just last element
    extra = L[-1:]
    new = []
    # for all smaller solutions, add one with last element
    for small in smaller:
        new.append(small+extra)
    # return samller+new
    return smaller+new