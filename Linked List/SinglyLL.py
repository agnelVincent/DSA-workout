class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert(self , value):
        if self.is_empty():
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = Node(value)
        current.next = new_node

    def delete_at_start(self):
        if self.is_empty():
            print('linked list empty')
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            print('linked list empty')
            return
        
    def delete_by_value(self , value):
        if self.is_empty():
            print('linked list empty')
            return
        if self.head.value == value:
            return self.delete_at_start()
        current = self.head
        while current.next:
            prev = current
            current = current.next
            if current.value == value:
                prev.next = current.next
                current.next = None
                return

    def traverse(self):
        if self.is_empty():
            print('linked list empty')
            return
        current = self.head
        while current.next:
            print(current.value , end=' ')
            current = current.next
        print(current.value)

    
linkedlist = SinglyLL()

for i in [2,4,8,10,15]:
    linkedlist.insert(i)

linkedlist.traverse()

linkedlist.delete_by_value(8)
linkedlist.traverse()
linkedlist.delete_at_start()
linkedlist.traverse()
linkedlist.delete_at_end()
linkedlist.traverse()
linkedlist.delete_by_value(10)
linkedlist.traverse()