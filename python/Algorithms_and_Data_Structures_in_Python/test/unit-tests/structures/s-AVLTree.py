import AVLTree as avl
from stest import expect_equal

test1 = '[1, 3, 7.5, 10, 100, 1000]'
test2 = '[1, 3, 7.5, 100, 1000]'
test3 = '[1, 3, 7.5, 67, 100, 1000]'
test4 = '[1, 3, 7.5, 100, 1000]'

def init():
    avlTree = avl.AvlTree()
    avlTree.insert(10)
    avlTree.insert(100)
    avlTree.insert(1000)
    avlTree.insert(3)
    avlTree.insert(1)
    avlTree.insert(7.5)

    return avlTree

avlTree = init()
expect_equal(str(avlTree), test1)

avlTree.remove(10)
expect_equal(str(avlTree), test2)

avlTree.insert(67)
expect_equal(str(avlTree), test3)

avlTree.remove(67)
expect_equal(str(avlTree), test4)
    

        


        

