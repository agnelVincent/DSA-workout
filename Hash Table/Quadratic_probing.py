class HashTable:
    def __init__(self , size):
        self.size = size
        self.table = [None] * self.size

    def _hash(self , key):
        return hash(key) % self.size
    
    def insert(self , key , value):

        index = self._hash(key)

        for i in range(self.size):
            idx = (index + i**2) % self.size
            entry = self.table[idx]

            if entry == None or entry == 'DELETED':
                self.table[idx] = (key , value)
                return
            
            if entry[0] == key:
                self.table[idx] = (key , value)
                return
            
        print('hash table is full')

    def search(self , key):

        index = self._hash(key)

        for i in range(self.size):
            idx = (index + i**2) % self.size
            entry = self.table[idx]

            if entry == None:
                break

            if entry != 'DELETED' and entry[0] == key:
                print(self.table[idx][1])
                return
            
        print('no match found')
    
    def remove(self , key):

        index = self._hash(key)

        for i in range(self.size):

            idx = (index + i**2) % self.size
            entry = self.table[idx]

            if entry == None:
                break

            if entry != 'DELETED' and entry[0] == key:
                self.table[idx] = 'DELETED'
                return

        print('key not found')

    def traverse(self):
        for i in self.table:
            if i is None or i == 'DELETED':
                print(0, end=' , ')
            else:
                print(f'{i[0]} : {i[1]}', end=' , ') 



ht = HashTable(10)
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("apple", 30)  
ht.search("apple")      
ht.search("berry")      
ht.remove("banana")
ht.search("banana")     
ht.traverse()

print(ht) 