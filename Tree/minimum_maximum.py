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
    
    def minimum_node(self):
        node = self.root
        while node.left:
            node = node.left
        return node.value
    
    def maximum_node(self):
        node = self.root
        while node.right:
            node = node.right
        return node.value
    
tree = BST()
for i in [5,1,9,10,4,20,23,2]:
    tree.insert(i)

print(tree.minimum_node())
print(tree.maximum_node())