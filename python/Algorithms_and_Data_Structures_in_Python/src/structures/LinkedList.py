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
            print("{} bigger actual size {}".format(position, self.size))
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
    
    def print(self):

        print('List size {}:\n'.format(self.size))
        tmp = self.head

        while tmp is not None:
            print(tmp)
            tmp = tmp.next

if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.push_back(10)
    linkedList.push_top(100)
    linkedList.insert(5,1000)
    linkedList.insert(0,3)
    linkedList.push_back('Adam')
    linkedList.push_back(7.5)
    linkedList.print()
    print('-------')
    linkedList.remove(1000)
    linkedList.print()
    print('-------')
    linkedList.insert(2,67)
    linkedList.print()
    print('-------')
    