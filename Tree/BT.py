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
        
        current = self.root

        while True:
            if current.left is None:
                current.left = Node(value)
                return
            elif current.right is None:
                current.right = Node(value)
                return
            else:
                current = current.left


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