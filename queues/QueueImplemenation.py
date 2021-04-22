class Queue : 
    def __init__(self):
        self.queue = []
        
    #Returns size of Queue
    def size(self):
        return len(self.queue)
    
    # Adds an item in the Queue
    def enqueue(self , item):
        self.queue.append(item)
        
    #Removes item from the Queue 
    def dequeue(self):
        if(len(self.queue) < 1):
            return None
        else:
            return self.queue.pop()
        
    #Display the Queue
    def display(self):
        print(self.queue)
    
    
q = Queue()
q.enqueue(12)
q.enqueue(13)
q.enqueue(33)
q.enqueue(124)
q.enqueue(71)

q.display()
q.dequeue()

q.display()