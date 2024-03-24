# Node structure
class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)
    
# Node structure
class DoublyLinkedNode (LinkedNode):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Node structure
class BinaryTreeNode (LinkedNode):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def get_child_num(self):
        if (self.right is not None) and (self.left is not None):
            return 2
        elif (self.right is not None) | (self.left is not None):
            return 1
        else:
            return 0
        
    def change_child(self, oldChild, newChild):
        if self.left == oldChild:
            self.left = newChild
        elif self.right ==  oldChild:
            self.right = newChild
        else:
            return

    def find_most_right_node(self):
        if self.right:
            return self.right.find_most_right_node()
        
        return self
    
    def __repr__(self):
        return str(self.data)