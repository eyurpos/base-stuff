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
            print("{} bigger actual size {}".format(position, self.size))
            self.push_back(data)
            return
        
        if position == 0:
            self.push_top(data)
            return
        
        tmp = None
        if position < self.size//2:
            print(1)
            tmp = self.__find_forward_el(position)
        else:
            print(2)
            tmp = self.__find_backward_el(position)

        if not tmp:
            print ("Error")
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
    
    def print_forward(self):

        print('List size {}:\n'.format(self.size))
        tmp = self.head

        while tmp is not None:
            print(tmp)
            tmp = tmp.next

    def print_backward(self):

        print('List size {}:\n'.format(self.size))
        tmp = self.tail

        while tmp is not None:
            print(tmp)
            tmp = tmp.prev

if __name__ == '__main__':
    doublyLinkedList = DoublyLinkedList()
    doublyLinkedList.push_back(10)
    doublyLinkedList.push_top(100)
    doublyLinkedList.insert(5,1000)
    doublyLinkedList.insert(0,3)
    doublyLinkedList.push_back('Adam')
    doublyLinkedList.push_back(7.5)
    doublyLinkedList.print_forward()
    print('-------')
    doublyLinkedList.remove(1000)
    doublyLinkedList.print_forward()
    print('-------')
    doublyLinkedList.insert(1,67)
    doublyLinkedList.insert(4,68)
    doublyLinkedList.print_forward()
    print('-------')
    doublyLinkedList.print_backward()
    print('-------')
    