class MinHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self , value):
        self.heap.append(value)
        return self._heapify_up(len(self.heap)-1)
        
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value
        
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
        
    def _heapify_up(self , index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index] , self.heap[parent] = self.heap[parent] , self.heap[index]
            else:
                break
            
    def _heapify_down(self , index):
        n = len(self.heap)
        
        while index < n:
            left = (2 * index) + 1
            right = (2 * index) + 2
            smallest = index
            
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
                
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
                
            if smallest != index:
                self.heap[smallest] , self.heap[index] = self.heap[index] , self.heap[smallest]
                index = smallest
            
            else:
                break


heap = MinHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(2)

print(heap.extract_min())  
print(heap.extract_min())  
print(heap.peek())         

