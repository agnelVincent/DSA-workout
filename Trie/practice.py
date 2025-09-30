class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self , word):
        
        current = self.root

        for i in word:
            if i not in current.children:
                current.children[i] = Node()
            current = current.children[i]

        current.is_end = True

    def startwith(self , prefix):
        current = self.root
        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        return True
    
    def autocomplete(self , prefix):
        current = self.root

        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        
        def dfs(node , path):
            if node.is_end:
                res.append(path)
            for char , children in node.children.items():
                dfs(children , path + char)

        res = []
        dfs(current , prefix)
        return res

    def traverse(self):
        
        def dfs(node , path):

            if node.is_end:
                result.append(path)
                
            for char , child in node.children.items():
                dfs(child , path + char)
        
        result = []

        dfs(self.root , '')
        return result

trie = Trie()

trie.insert('cat')
trie.insert('can')
trie.insert('camel')
trie.insert('cannoy')

print(trie.traverse())

print(trie.autocomplete('can'))
