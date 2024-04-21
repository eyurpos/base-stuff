import DoublyLinkedList as list
from stest import expect_equal

test1 = '3 100 10 1000 Adam 7.5 '
test2 = '3 100 10 Adam 7.5 '
test3 = '3 67 100 10 68 Adam 7.5 '
test4 = '7.5 Adam 68 10 100 67 3 '

def init():
    doublyLinkedList = list.DoublyLinkedList()
    doublyLinkedList.push_back(10)
    doublyLinkedList.push_top(100)
    doublyLinkedList.insert(5,1000)
    doublyLinkedList.insert(0,3)
    doublyLinkedList.push_back('Adam')
    doublyLinkedList.push_back(7.5)

    return doublyLinkedList


doublyLinkedList = init()
expect_equal(doublyLinkedList.s_forward(), test1)
doublyLinkedList.remove(1000)
expect_equal(doublyLinkedList.s_forward(), test2)
doublyLinkedList.insert(1,67)
doublyLinkedList.insert(4,68)
expect_equal(doublyLinkedList.s_forward(), test3)
expect_equal(doublyLinkedList.s_backward(), test4)


