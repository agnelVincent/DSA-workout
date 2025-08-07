from collections import deque

class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self , value):
        if self.root is None:
            self.root = Node(value)
            return
        new_node = Node(value)
        queue = deque()
        queue.append(self.root)
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                return

            queue.append(current.left)
            
            if current.right is None:
                current.right = new_node
                return
            
            queue.append(current.right)
            

    def contains(self , value):
        current = self.root
        
        while current:
            if current.left == value:
                return True
            elif current.right == value:
                return True
            else:
                current = current.left
        return False
    
    
tree = BinaryTree()
tree.insert(6)
tree.insert(7)
print(tree.root.value)
