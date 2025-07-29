class HashTable:

    def __init__(self , size = 10):
        self.size = size
        self.table = [[] for i in range(self.size)]

    def _hash(self , key):
        return hash(key) % self.size
    
    def inserting(self , key , value):
        index = self._hash(key)

        for i in self.table[index]:
            if i[0] == key:
                i[1] = value
                return
        
        self.table[index].append([key , value])

    def remove(self , key):
        index = self._hash(key)
        for i , item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        print('key value pair not found')

    def search(self , key):
        index = self._hash(key)
        for i in self.table[index]:
            if i[0] == key:
                print(i[1])
                return
        print('match not found')

    def traverse(self):
        for i in self.table:
            for j in i:
                print(f'{j[0]} : {j[1]}' , end=' , ')


ht = HashTable()
ht.inserting("apple", 10)
ht.inserting("banana", 20)
ht.inserting("apple", 30)  
ht.search("apple")      
ht.search("berry")      
ht.remove("banana")
ht.search("banana")     
ht.traverse()

print(ht) 
