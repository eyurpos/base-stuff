from Nodes import BinaryTreeNode

# Binary Tree structure
class BinaryTree:    
    def __init__(self):
        self.head = None

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
        
        childNum =  element.get_child_num()
        newChild = None
        parent = element.parent
        
        if childNum == 1:
            if element.right:
                newChild = element.right
            else:
                newChild = element.left
        elif childNum == 2:
            mostRightCihild = element.left.find_most_right_node()
            element.data = mostRightCihild.data
            self.__remove_node(mostRightCihild)
            return self

        if parent:
            parent.change_child(element, newChild)
        else:
            self.head = newChild

        if newChild:
            newChild.parent = parent

    def __traverse(self, element, result):
        if element:
            if element.left:
                self.__traverse(element.left, result)

            result.append(element.data)

            if element.right:
                self.__traverse(element.right, result)
    
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

    def print(self):
        result = []
        self.__traverse(self.head, result)
        print(result)


if __name__ == '__main__':
    binaryTree = BinaryTree()
    binaryTree.insert(10)
    binaryTree.insert(100)
    binaryTree.insert(1000)
    binaryTree.insert(3)
    binaryTree.insert(1)
    binaryTree.insert(7.5)
    binaryTree.print()
    print('-------')
    binaryTree.remove(10)
    binaryTree.print()
    print('-------')
    binaryTree.insert(67)
    binaryTree.print()
    print('-------')
    binaryTree.remove(67)
    binaryTree.print()
    

        


        

