class Queue(object):
    def __init__(self):
        # initializes one attribute: a list to keep track of queue's elements 
        self.vals = []
    
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    # removes the oldest(stay longest) element and returns it       
    def remove(self):
        if len(self.vals) > 0:
            return self.vals.pop(0)
        # if the queue is empty, raises a ValueError
        else:
            raise ValueError()
    
    def __str__(self):
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
            
queue = Queue()
queue.insert(5)
queue.insert(6)
queue.remove()
print queue
queue.insert(7)
queue.remove()
#print queue
queue.remove()
queue.remove()
print queue   