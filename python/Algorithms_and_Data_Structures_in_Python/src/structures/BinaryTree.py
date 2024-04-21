from Nodes import BinaryTreeNode

# Binary Tree structure
class BinaryTree:    
    def __init__(self):
        self.head = None

    def __repr__(self):
        result = []
        self._traverse(self.head, result)
        return str(result)
    
    def __insert_node(self, parent, newEl):
        if newEl.data > parent.data:
            if parent.right:
                self.__insert_node(parent.right, newEl)
            else:
                parent.right = newEl
                newEl.parent = parent
        elif newEl.data < parent.data:
            if parent.left:
                self.__insert_node(parent.left, newEl)
            else:
                parent.left = newEl
                newEl.parent = parent
        else:
            print("{} already available".format(newEl.data))

    def __find_node(self, element, data):
        if not element:
            return None

        if element.data == data:
            return element
        
        if data > element.data:
            return self.__find_node(element.right, data)
        elif data < element.data:
            return self.__find_node(element.left, data)

        return None
    
    def __remove_node(self, element):
        if not element:
            return None
        
        childNum =  self.__get_child_num(element)
        newChild = None
        parent = element.parent
        
        if childNum == 1:
            if element.right:
                newChild = element.right
            else:
                newChild = element.left
        elif childNum == 2:
            mostRightCihild = self._find_most_right_child(element.left)
            element.data = mostRightCihild.data
            self.__remove_node(mostRightCihild)
            return self

        if parent:
            self.__change_child(parent, element, newChild)
        else:
            self.head = newChild

        if newChild:
            newChild.parent = parent

    def _traverse(self, element, result):
        if element:
            if element.left:
                self._traverse(element.left, result)

            result.append(element.data)

            if element.right:
                self._traverse(element.right, result)

    def __get_child_num(self, element):
        if not element:
            raise ValueError
        
        if (element.right is not None) and (element.left is not None):
            return 2
        elif (element.right is not None) | (element.left is not None):
            return 1
        else:
            return 0

    def __change_child(self, parent, oldChild, newChild):
        if not parent:
            raise ValueError
        
        if parent.left == oldChild:
            parent.left = newChild
        elif parent.right ==  oldChild:
            parent.right = newChild
        else:
            raise ValueError

    def _find_most_right_child(self, root):
        if not root:
            raise ValueError
        
        if root.right:
            return self._find_most_right_child(root.right)
        
        return root

    def _find_most_left_child(self, root):
        if root is None or root.left is None:
            return root
 
        return self._find_most_left_child(root.left)
       
    def insert(self, data):
        newEl = BinaryTreeNode(data)

        if not self.head:
            self.head = newEl
        else:
            self.__insert_node(self.head, newEl)

    def find(self, data):
        return self.__find_node(self.head, data)
    
    def remove(self, data):
        element = self.find(data)
        self.__remove_node(element)
