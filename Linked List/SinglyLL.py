class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self , value):
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self , value):

        if self.head is None:
            return self.insert_at_beginning(value)
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = Node(value)
    
    def insert_at_position(self , value , position):
        if position == 1:
            return self.insert_at_beginning(value)
        
        if self.is_empty():
            return False
        
        current = self.head
        i = 1

        while current.next and i < position-1:
            current = current.next
            i += 1
        
        if not current:
            print('index out of range')
            return
        
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return False
        
        self.head = self.head.next

    def delete_at_end(self):
        if self.is_empty():
            return False
        
        current = self.head
        while current.next.next:
            current = current.next
        
        current.next = None

    def delete_at_position(self , position):
        if self.is_empty():
            return False
        
        if position == 1:
            return self.delete_at_beginning(position)
        
        i = 1
        current = self.head

        while current.next and i < position - 1:
            current = current.next
            i += 1
        
        if not current:
            print('index not found')
            return

        if current.next.next:
            current.next = current.next.next
            return
        
        current.next = None

    def reverse(self):

        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value , end= ' ')
            current = current.next
        print()

    def is_empty(self):
        return self.head is None
    
    def middle(self):
        if self.is_empty():
            return False
        
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value

ll = SinglyLL()

for i in [3,5,7,9]:
    ll.insert_at_end(i)

ll.insert_at_position(2,1)

ll.insert_at_beginning(1)

ll.insert_at_position(4,4)

ll.insert_at_position(6,6)

ll.insert_at_position(8,8)

ll.insert_at_end(10)

ll.traverse()

ll.delete_at_beginning()

ll.delete_at_position(3)

ll.delete_at_end()

ll.traverse()

ll.reverse()

ll.traverse()

print(ll.middle())