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

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(100)
    stack.push('Adam')
    stack.push(7.5)
    print(stack.pop())
    print('-------')
    stack.push(1000)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    if stack.pop():
        print("error")
    print('-------')
    