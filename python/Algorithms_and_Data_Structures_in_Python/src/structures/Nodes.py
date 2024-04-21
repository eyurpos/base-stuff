# Base Node structure
class Node:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)
    
# Linked Node structure
class LinkedNode (Node):
    def __init__(self, data):
        super().__init__(data)
        self.next = None
    
# Doubly Linked Node structure
class DoublyLinkedNode (LinkedNode):
    def __init__(self, data):
        super().__init__(data)
        self.prev = None

# Binary Tree Node structure
class BinaryTreeNode (Node):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None
        self.left = None
        self.right = None
    
# AVL Tree Node structure
class AvlTreeNode (BinaryTreeNode):
    def __init__(self, data):
        super().__init__(data)
        self.height = 1