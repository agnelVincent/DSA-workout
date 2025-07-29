from collections import deque

class Stack:
    def __init__(self):
        self.q = deque()

    def push(self , val):
        self.q.append(val)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None
        return self.q.popleft()
    
    def top(self):
        if self.is_empty():
            print('Stack is empty')
            return 
        
        return self.q[0]
    
    def is_empty(self):
        return len(self.q) == 0
    
    def size(self):
        return len(self.q)
    

