import BinaryTree as binary
from stest import expect_equal

test1 = '[1, 3, 7.5, 10, 100, 1000]'
test2 = '[1, 3, 7.5, 100, 1000]'
test3 = '[1, 3, 7.5, 67, 100, 1000]'
test4 = '[1, 3, 7.5, 100, 1000]'

def init():
    binaryTree = binary.BinaryTree()
    binaryTree.insert(10)
    binaryTree.insert(100)
    binaryTree.insert(1000)
    binaryTree.insert(3)
    binaryTree.insert(1)
    binaryTree.insert(7.5)

    return binaryTree

binaryTree = init()
expect_equal(str(binaryTree), test1)

binaryTree.remove(10)
expect_equal(str(binaryTree), test2)

binaryTree.insert(67)
expect_equal(str(binaryTree), test3)

binaryTree.remove(67)
expect_equal(str(binaryTree), test4)
    

        


        

