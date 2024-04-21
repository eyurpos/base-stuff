from Nodes import LinkedNode

# Stack structure
class Stack:        
    def __init__(self):
        self.head = None

    def push(self, data):
        newEl = LinkedNode(data)

        newEl.next = self.head
        self.head = newEl

    def pop(self):
        result = None

        if self.head:
            result = self.head.data
            self.head =  self.head.next

        return result   
  