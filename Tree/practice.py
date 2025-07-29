class Tree:
    def __init__(self , val):
        self.value = val
        self.left = None
        self.right = None

    def traverse(self , root):
        if root.left is None:
            return 
        print(root.value)
        return self.traverse(root.left)
        
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.traverse(root)

