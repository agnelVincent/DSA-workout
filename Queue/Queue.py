class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self , val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            print('queue is empty')
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            print('queue is empty')
            return None
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue)==0
    
    def size(self):
        return len(self.queue)
    
    def traverse(self):
        if self.is_empty():
            print('queue is empty')
            return None
        for i in self.queue:
            print(i , end = ' ')


