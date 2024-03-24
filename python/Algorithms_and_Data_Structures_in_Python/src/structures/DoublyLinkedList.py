from Nodes import DoublyLinkedNode

# Doubly Linked List structure
class DoublyLinkedList:    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __find_forward_el(self, position):
        tmp = self.head
        while position > 0:
            tmp = tmp.next
            position -= 1

        return tmp

    def __find_backward_el(self, position):
        tmp = self.tail
        number = self.size-1
        while number > position:
            tmp = tmp.prev
            number -= 1

        return tmp
    
    def push_back(self, data):
        newEl = DoublyLinkedNode(data)

        if not self.tail:
            self.tail = newEl
            self.head = self.tail
        else:
            self.tail.next = newEl
            newEl.prev = self.tail
            self.tail = newEl
        self.size += 1

    def push_top(self, data):
        newEl = DoublyLinkedNode(data)

        if not self.head:
            self.head = newEl
            self.tail = newEl
        else:
            newEl.next = self.head
            self.head.prev = newEl
            self.head = newEl

        self.size += 1

    def insert(self, position, data):
        newEl = DoublyLinkedNode(data)

        if self.size <= position:
            self.push_back(data)
            return
        
        if position == 0:
            self.push_top(data)
            return
        
        tmp = None
        if position < self.size//2:
            tmp = self.__find_forward_el(position)
        else:
            tmp = self.__find_backward_el(position)

        if not tmp:
            return
        
        newEl.next = tmp
        newEl.prev = tmp.prev
        newEl.next.prev = newEl
        newEl.prev.next = newEl

        self.size += 1

    def remove(self, data):
        if self.head == self.tail:
            if self.head == data:
                self.head = None
                self.tail = None
        elif self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            tmp = self.head
            while tmp.next:
                if tmp.next.data == data:
                    tmp.next = tmp.next.next
                    tmp.next.prev = tmp
                    break
                else:
                    tmp = tmp.next

        self.size -= 1


    def size(self):
        return self.size
    
    def s_forward(self):
        result = ""
        tmp = self.head

        while tmp is not None:
            result += "{} ".format(str(tmp)) 
            tmp = tmp.next

        return result

    def s_backward(self):
        result = ""
        tmp = self.tail

        while tmp is not None:
            result += "{} ".format(str(tmp)) 
            tmp = tmp.prev

        return result
