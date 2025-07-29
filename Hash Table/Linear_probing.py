
class HashTable:
    def __init__(self , size = 10):
        self.size = size
        self.table = [None] * self.size

    def _hash(self , key):
        return hash(key) % self.size
    
    def insertion(self , key , value):
        index = self._hash(key)

        original_index = index

        while self.table[index] != None:

            if self.table[index] != 'Deleted' and self.table[index][0] == key:
                self.table[index] = (key , value)
                return
            
            index = (index+1) % self.size

            if index == original_index:
                print('hash table full')
                return
        self.table[index] = (key ,value)

    def remove(self , key):
        index = self._hash(key)

        original_index = index

        while self.table[index] != None:
            if self.table[index] != 'Deleted' and self.table[index][0] == key:
                self.table[index] = 'Deleted'
                return
            index = (index + 1) % self.size
            if index == original_index:
                print('hash table full')
                return
        print('key not found')

    def searching(self , key):
        index = self._hash(key)
        original_index = index
        while self.table[index] != None:
            if self.table[index] != 'Deleted' and self.table[index][0] == key:
                print(self.table[index][1])
                return
            index = (index + 1) % self.size
            if original_index == index:
                break
        print('no match found')
    
    def traverse(self):
        for i in self.table:
            if i == 'Deleted' or i == None:
                print(0 , end=' , ')
            else:
                print(f'{i[0]} : {i[1]}' , end=' , ')
        print()
            

ht = HashTable()

ht.insertion("apple", 100)
ht.insertion("banana", 200)
ht.insertion("orange", 300)
ht.traverse()

ht.remove("banana")
ht.traverse()

ht.searching("apple")
ht.searching("banana")