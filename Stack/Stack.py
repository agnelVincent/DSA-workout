class Stack:
    def __init__(self):
        self.stack = []

    def push(self , val):
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            print('stack is empty')
            return 
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print('stack is empty')
            return
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def traverse(self):
        if self.is_empty():
            print('stack is empty')
            return
        for i in range(len(self.stack)-1,-1,-1):
            print(self.stack[i] , end=' ')

    def size(self):
        return len(self.stack)

