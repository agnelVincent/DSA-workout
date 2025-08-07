class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self , value):
        self.heap.append(value)
        return self._heapify_up(len(self.heap)-1)
    
    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return max_value
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def _heapify_up(self , index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[parent] < self.heap[index]:
                self.heap[parent] , self.heap[index] = self.heap[index] , self.heap[parent]
                index = parent
            else:
                break

    def _heapify_down(self , index):
        n = len(self.heap)
        while index < n:
            left = (2 * index) + 1
            right = (2 * index) + 2
            largest = index
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right

            if largest != index:
                self.heap[largest] , self.heap[index] = self.heap[index] , self.heap[largest]
                index = largest
            else:
                break

heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(20)
heap.insert(2)

print(heap.extract_max())  
print(heap.extract_max())  
print(heap.peek())         
