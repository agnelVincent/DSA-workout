from collections import deque

class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self , value):
        if self.root is None:
            self.root = Node(value)
            return 
        
        current = self.root
        
        while True:
            if value <= current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
                
    def search(self , value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value <= node.value:
                node = node.left
            else:
                node = node.right
        return False
                
    def inorder(self , node):
        if node.left:
            self.inorder(node.left)
        print(node.value , end = ' ')
        if node.right:
            self.inorder(node.right)
            
    def preorder(self , node):
        if node:
            print(node.value , end = ' ')
            self.preorder(node.left)
            self.preorder(node.right)
            
    def postorder(self , node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value , end = ' ')
            
    def bfs(self , node):
        queue = deque()
        queue.append(node)
        while queue:
            current = queue.popleft()
            print(current.value , end = ' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
            
            
tree = BST()
for i in [5,1,9,10,4,20,23,2]:
    tree.insert(i)
    
tree.inorder(tree.root)
print()
tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()
tree.bfs(tree.root)
print()
print(tree.search(9))

                
                
                
                
                
                
                
                
                
                
                
                
                