from enum import Enum
from Nodes import AvlTreeNode
from BinaryTree import BinaryTree

class AvlTree (BinaryTree):
    class Heavy(Enum):
        RIGHT_HEAVY = -1
        BALANCED = 0
        LEFT_HEAVY = 1

    def __init__(self):
        super().__init__()

    def __getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
    

    def __getMaxHeight(self, root): 
        if not root:
            return 0
  
        return 1 + max(self.__getHeight(root.left), self.__getHeight(root.right)) 


    def __getBalance(self, root): 
        if not root: 
            return self.Heavy.BALANCED

        balance = self.__getHeight(root.left) - self.__getHeight(root.right)
        if balance < -1:
            return self.Heavy.RIGHT_HEAVY
        elif balance > 1:
            return self.Heavy.LEFT_HEAVY
        return self.Heavy.BALANCED
    
  
    def __leftRotate(self, root): 

        new_root = root.right 
        new_right = new_root.left 
  
        new_root.left = root 
        root.right = new_right 
  
        root.height = self.__getMaxHeight(root)
        new_root.height = self.__getMaxHeight(new_root)
  
        return new_root 
  

    def __rightRotate(self, root): 
    
        new_root = root.left 
        new_left = new_root.right 
  
        new_root.right = root 
        root.left = new_left
  
        root.height = self.__getMaxHeight(root)
        new_root.height = self.__getMaxHeight(new_root)
  
        return new_root
    

    def __balance(self, parent, data):        

        balance = self.__getBalance(parent)

        if balance == self.Heavy.LEFT_HEAVY and data < parent.left.data:
            return self.__rightRotate(parent)
        if balance == self.Heavy.RIGHT_HEAVY and data > parent.right.data:
            return self.__leftRotate(parent)
        if balance == self.Heavy.LEFT_HEAVY and data > parent.left.data:
            parent.left = self.__leftRotate(parent.left)
            return self.__rightRotate(parent)
        if balance == self.Heavy.RIGHT_HEAVY and data < parent.right.data:
            parent.right = self.__rightRotate(parent.right)
            return self.__leftRotate(parent)
        
        return parent
    

    def __insert_node(self, parent, data):
        if not parent:
            return AvlTreeNode(data)
        elif data > parent.data:
            parent.right = self.__insert_node(parent.right, data)
        elif data < parent.data:
            parent.left = self.__insert_node(parent.left, data)
        else:
            print("{} already available".format(data))
            return
 
        parent.height = self.__getMaxHeight(parent)
        
        return self.__balance(parent, data)


    def __remove_node(self, parent, data):
 
        if not parent:
            return None
        elif data < parent.data:
            parent.left = self.__remove_node(parent.left, data)
        elif data > parent.data:
            parent.right = self.__remove_node(parent.right, data)
        else:
            if parent.left is None:
                temp = parent.right
                parent = None
                return temp
            elif parent.right is None:
                temp = parent.left
                parent = None
                return temp
 
            temp = self._find_most_left_child(parent.right)
            parent.data = temp.data
            parent.right = self.__remove_node(parent.right, temp.data)
 
        if parent is None:
            return parent
 
        parent.height = self.__getMaxHeight(parent)
 
        return self.__balance(parent, data)


    def insert(self, data):
        self.head = self.__insert_node(self.head, data)


    def remove(self, data):
        self.head = self.__remove_node(self.head, data)


def init():
    avlTree = AvlTree()
    avlTree.insert(10)
    avlTree.insert(100)
    avlTree.insert(1000)
    avlTree.insert(3)
    avlTree.insert(1)
    avlTree.insert(7.5)

    return avlTree