class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion_at_end(self , value):
        if self.head is None:
            self.head = Node(value)
            return self.head
        
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(value)

    def insertion_at_beginning(self , value):
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insertion_at_position(self , value , position):
        if position == 0:
            self.insertion_at_beginning(value)
            return
        current = self.head
        i = 0
        while i < position-1 and current.next is not None:
            current = current.next
            i += 1
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self , position):
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        i = 0
        while i < position - 1 and current.next is not None:
            current = current.next
            i += 1
        current.next = current.next.next

    def delete_at_end(self):
        current = self.head

        while current.next.next:
            current = current.next
        current.next = None

    
    def traverse(self):

        if self.head is None:
            print('empty linked list')
            return
        
        current = self.head

        while current:
            print(current.value , end=' --> ')
            current = current.next
    
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow:
            print(f'middle : {slow.value}')
        else:
            print('List is empty')
        
    

linkedlist = LinkedList()

for i in [1,2,3,4,5,6,7,8]:
    linkedlist.insertion_at_end(i)

linkedlist.insertion_at_position(100,4)

linkedlist.traverse()
print()
linkedlist.insertion_at_beginning(100)

linkedlist.delete_at_position(4)

linkedlist.delete_at_end()

linkedlist.traverse()

linkedlist.find_middle()