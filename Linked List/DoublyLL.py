class Node:
    def __init__(self , value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert(self , value):
        if not self.head:
            