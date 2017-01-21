 # Towers of hanoi
 # think recursively, if I want to move stack of size n, I need to move stack of size n-1 to the spare
 # and then move the bottom one to the target place and then move n-1 to target place
 # smaller problem + base case
def printMove(fr,to):
    print'move from' + str(fr) + 'to' +str(to)
def towers(n,fro,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
    # there are only three spikes 
    # note that the 2nd argument is the spike called from, 3nd is the spike called to, 4th is the spare one 
    # 1st step: towers(n-1,fr,spare,to) means, move n-1, from 'fr' spike to 'spare' spike, and leave 'to' spike spared
    # 2nd step: 1 means the bottom one from 'fr' to 'to' and leave 'spare'
    # 3rd step: towers(n-1,spare,to,fr) means move n-1, from 'spare' to 'to' and leave 'fr'
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)