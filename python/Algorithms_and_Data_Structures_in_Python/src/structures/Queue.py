from Nodes import LinkedNode
        
# Queue structure
class Queue:    
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        newEl = LinkedNode(data)

        if self.tail:
            self.tail.next = newEl

        self.tail = newEl

        if not self.head:
            self.head = self.tail

    def pop(self):
        result = None

        if self.head:
            result = self.head.data

            self.head = self.head.next

            if self.tail.next == self.head:
                self.tail = self.head

        return result       

if __name__ == '__main__':
    queue = Queue()
    queue.push(10)
    queue.push(100)
    queue.push('Adam')
    queue.push(7.5)
    print(queue.pop())
    print('-------')
    queue.push(1000)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    if queue.pop():
        print("error")
    print('-------')
    