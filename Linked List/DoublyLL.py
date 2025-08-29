class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self , value):
        if self.head is None:
            self.head = Node(value)
            return
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    
    def insert_at_position(self , value , position):
        if position == 1:
            return self.insert_at_beginning(value)
        current = self.head
        i = 1
        while current.next and i < position-1:
            current = current.next
            i += 1
        if not current:
            print('index not available')
            return
        if not current.next:
            self.insert_at_end(value)  
        new_node = Node(value)
        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        current.next.prev = new_node

    def insert_at_end(self , value):
        if self.head is None:
            return self.insert_at_beginning(value)
        
        current = self.head
        
        while current.next:
            current = current.next
        
        new_node = Node(value)
        current.next = new_node
        new_node.prev = current

    def delete_at_beginning(self):
        if self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
                return
            self.head = None

    def delete_at_end(self):
        
        current = self.head

        while current.next.next:
            current = current.next
        
        current.next.prev = None
        current.next = None

    def delete_at_position(self , position):

        i = 1
        current = self.head

        while current.next and i < position:
            temp = current
            current = current.next
            i += 1

        if not current:
            print('index error')
            return
        
        temp.next = current.next
        if current.next:
            current.next.prev = temp

    def reverse(self):
        current = self.head

        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            
            prev_node = current
            current = current.prev

        self.head = prev_node
         
    def traverse(self):
        current = self.head
        while current:
            print(current.value ,end=' ')
            current = current.next
        print()


ll = DoublyLL()
for i in [2,3,4,5,7]:
    ll.insert_at_end(i)

ll.insert_at_position(6,5)

ll.insert_at_position(1,1)

ll.traverse()

ll.delete_at_position(4)

ll.traverse()

ll.reverse()

ll.traverse()