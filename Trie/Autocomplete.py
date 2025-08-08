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

    def autocomplete(self , prefix):
        
        current = self.root
        for i in prefix:
            if i not in current.children:
                print('not found')
                return
            current = current.children[i]

        word = []
        def dfs(node , path):
            if node.is_end:
                word.append(path)
            for char , child in node.children.items():
                dfs(child , path + char)

        dfs(current , prefix)
        return word

trie = Trie()
for i in ["cat" , "cab" , "camel" , "cannon" , "catch"]:
    trie.insert(i)

print(trie.autocomplete('cat'))