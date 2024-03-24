import LinkedList as list
from stest import expect_equal

test1 = '3 100 10 1000 Adam 7.5 '
test2 = '3 100 10 Adam 7.5 '
test3 = '3 100 67 10 Adam 7.5 '

def init():
    linkedList = list.LinkedList()
    linkedList.push_back(10)
    linkedList.push_top(100)
    linkedList.insert(5,1000)
    linkedList.insert(0,3)
    linkedList.push_back('Adam')
    linkedList.push_back(7.5)

    return linkedList

linkedList = init()
expect_equal(str(linkedList), test1)
linkedList.remove(1000)
expect_equal(str(linkedList), test2)
linkedList.insert(2,67)
expect_equal(str(linkedList), test3)
    