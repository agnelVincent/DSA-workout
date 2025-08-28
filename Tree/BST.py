class Node:
    def __init__(self , value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self ,value):
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
                
    def inorder(self , node):
        
        if node:
            self.inorder(node.left)
            print(node.value , end = ' ')
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
            print(node.value ,end = ' ')
            
    def bfs(self):
        from collections import deque

        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            print(node.value , end = ' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def kth_largest(self , k):
        self.count = 0
        self.res = -1
        
        def dfs(node):
            if not node or self.count >= k:
                return
            dfs(node.right)
            self.count += 1
            if self.count == k:
                self.res = node.value
                return
            dfs(node.left)
            
        dfs(self.root)
        return self.res
            
    
bst = BST()
for i in [5,1,2,10,9,8,3,6,4,7]:
    bst.insert(i)

bst.inorder(bst.root)
print()
bst.preorder(bst.root)
print()
bst.postorder(bst.root)
print()
print(bst.kth_largest(5))
print()
bst.bfs()