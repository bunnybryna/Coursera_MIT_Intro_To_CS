
def removeDups(L1,L2):
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
            
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1,L2)
# it will return L1 = [2,3,4],why?
# when we mutate a list, we change its length

# better version is to clone, we will get Li = [3,4]
# loop over a copy of L1, but mutate the real L1
# L1Start = L1 will not work
def removeDumBetter(L1,L2):
    Li1Start = Li1[:]
    for e1 in L1Start:
        if e1 in L2:
            L1.remove(e1)