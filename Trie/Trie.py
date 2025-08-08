class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self , word):
        current = self.root

        for i in word:
            if i not in current.children:
                current.children[i] = TrieNode()
            current = current.children[i]
        current.is_end = True

    def search(self , word):
        current = self.root
        
        for i in word:
            if i not in current.children:
                return False
            current = current.children[i]
        return current.is_end
    
    def starts_with(self , prefix):
        current = self.root

        for i in prefix:
            if i not in current.children:
                return False
            current = current.children[i]
        
        return True
    
    def traverse(self):
        words = []

        def dfs(node , path):
            if node.is_end:
                words.append(path)
            for char , child in node.children.items():
                dfs(child , path + char)
            
        dfs(self.root , "")

        return words

    
    def delete(self , word):

        def _delete(node , word , depth):
            if depth == len(word):
                if not node.is_end:
                    return False
                node.is_end = False
                return len(node.children) == 0
            
            char = word[depth]
            
            if char not in node.children:
                return False
            
            should_delete = _delete(node.children[char] , word , depth+1)

            if should_delete:
                del node.children[char]
                return not node.is_end and len(node.children) == 0
            
            return False


        _delete(self.root , word , 0)

    
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


print(trie.traverse())
trie.delete('cat')
print(trie.traverse())

