from Nodes import LinkedNode

# Linked List structure
class LinkedList:    
    def __init__(self):
        self.head = None
        self.size = 0

    def push_back(self, data):
        newEl = LinkedNode(data)

        if not self.head:
            self.head = newEl
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = newEl
        self.size += 1

    def push_top(self, data):
        newEl = LinkedNode(data)

        newEl.next = self.head
        self.head = newEl
        self.size += 1

    def insert(self, position, data):
        newEl = LinkedNode(data)

        if self.size <= position:
            self.push_back(data)
            return
        
        if position == 0:
            self.push_top(data)
            return
        
        tmp = self.head
        while position > 1:
            tmp = tmp.next
            position -= 1

        newEl.next = tmp.next
        tmp.next = newEl
        self.size += 1

    def remove(self, data):
        if self.head.data == data:
            self.head = self.head.next
        else:
            tmp = self.head
            while tmp.next:
                if tmp.next.data == data:
                    tmp.next = tmp.next.next
                    break
                else:
                    tmp = tmp.next

        self.size -= 1


    def size(self):
        return self.size
    
    def __repr__(self):
        result = ""
        tmp = self.head

        while tmp is not None:
            result += "{} ".format(str(tmp)) 
            tmp = tmp.next
        return result
