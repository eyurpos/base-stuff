from Nodes import RedBlackNode
from BinaryTree import BinaryTree

class RedBlackTree (BinaryTree):
    def __init__(self):
            super().__init__()
            self.__left_left_rotate_flag = False 
            self.__right_right_rotate_flag = False
            self.__left_right_rotate_flag = False
            self.__right_left_rotate_flag = False


    def __rotate_left(self, root):
        new_root = root.right
        new_right = new_root.left
        new_root.left = root
        root.right = new_right
        root.parent = new_root
        if new_right is not None:
            new_right.parent = root
        return new_root
 

    def __rotate_right(self, root):
        new_root = root.left
        new_left = new_root.right
        new_root.right = root
        root.left = new_left
        root.parent = new_root
        if new_left is not None:
            new_left.parent = root
        return new_root
    

    def __handle_rotations(self, root):
        if self.__left_left_rotate_flag:
            root = self.__rotate_left(root)
            root.colour = RedBlackNode.Color.BLACK
            root.left.colour = RedBlackNode.Color.RED
            self.__left_left_rotate_flag= False
        elif self.__right_right_rotate_flag:
            root = self.__rotate_right(root)
            root.colour = RedBlackNode.Color.BLACK
            root.right.colour = RedBlackNode.Color.RED
            self.__right_right_rotate_flag = False
        elif self.__right_left_rotate_flag:
            root.right = self.__rotate_right(root.right)
            root.right.parent = root
            root = self.__rotate_left(root)
            root.colour = RedBlackNode.Color.BLACK
            root.left.colour = RedBlackNode.Color.RED
            self.__right_left_rotate_flag = False
        elif self.__left_right_rotate_flag:
            root.left = self.__rotate_left(root.left)
            root.left.parent = root
            root = self.__rotate_right(root)
            root.colour = RedBlackNode.Color.BLACK
            root.right.colour = RedBlackNode.Color.RED
            self.__left_right_rotate_flag = False

        return root
    

    def __handle_red_red_conflicts(self, root):
        if root.parent.right == root:
            if root.parent.left is None or\
               root.parent.left.colour == RedBlackNode.Color.BLACK:
                if root.left is not None and\
                   root.left.colour == RedBlackNode.Color.RED:
                    self.__right_left_rotate_flag = True
                elif root.right is not None and\
                     root.right.colour == RedBlackNode.Color.RED:
                    self.__left_left_rotate_flag = True
            else:
                root.parent.left.colour = RedBlackNode.Color.BLACK
                root.colour = RedBlackNode.Color.BLACK
                if root.parent != self.head:
                    root.parent.colour = RedBlackNode.Color.RED
        else:
            if root.parent.right is None or\
               root.parent.right.colour == RedBlackNode.Color.BLACK:
                if root.left is not None and\
                   root.left.colour == RedBlackNode.Color.RED:
                    self.__right_right_rotate_flag = True
                elif root.right is not None and\
                     root.right.colour == RedBlackNode.Color.RED:
                    self.__left_right_rotate_flag = True
            else:
                root.parent.right.colour = RedBlackNode.Color.BLACK
                root.colour = RedBlackNode.Color.BLACK
                if root.parent != self.head:
                    root.parent.colour = RedBlackNode.Color.BLACK


    def __node_insert(self, root, data):
        conflict_flag = False   
        if root is None:
            return RedBlackNode(data)
        elif data < root.data:
            root.left = self.__node_insert(root.left, data)
            root.left.parent = root
            if root != self.head:
                if root.colour == RedBlackNode.Color.RED and\
                   root.left.colour == RedBlackNode.Color.RED:
                    conflict_flag = True
        elif data > root.data:
            root.right = self.__node_insert(root.right, data)
            root.right.parent = root
            if root != self.head:
                if root.colour == RedBlackNode.Color.RED and\
                   root.right.colour == RedBlackNode.Color.RED:
                    conflict_flag = True
        else:
            return root
 
        root = self.__handle_rotations(root)
 
        if conflict_flag:
            self.__handle_red_red_conflicts(root)
        return root
 

    def insert(self, data):
        if self.head is None:
            self.head = RedBlackNode(data)
            self.head.colour = RedBlackNode.Color.BLACK
        else:
            self.head = self.__node_insert(self.head, data)













avlTree = RedBlackTree()
avlTree.insert(10)
avlTree.insert(100)
avlTree.insert(1000)
avlTree.insert(3)
avlTree.insert(1)
avlTree.insert(7.5)

print(avlTree)