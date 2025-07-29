class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
         self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end = True

    def autocomplete(self , prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        results = []

        def dfs(node , path):
            if node.is_end:
                results.append(''.join(path))
            for char , child in node.children.items():
                dfs(child , path + [char])
        
        dfs(node , list(prefix))
        for i in results:
            print(i)

trie = Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("can")
trie.insert("bat")

trie.autocomplete('ca')