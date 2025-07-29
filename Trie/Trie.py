class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self , word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def search(self , word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_end 
    
    def starts_with(self , prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True
    
    def delete(self , word):
        def _delete(node ,word, depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            
            char = word[depth]

            

    
    def traverse(self):
        def dfs(node , path):
            if node.is_end:
                print(''.join(path))
            for char , child in node.children.items():
                dfs(child , path + [char])
        dfs(self.root , [])
    
    
    
trie = Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("can")
trie.insert("bat")

print(trie.search("cat"))     
print(trie.search("cab"))     
print(trie.starts_with("ca")) 
print(trie.starts_with("ba")) 
print(trie.starts_with("da")) 

trie.traverse()

