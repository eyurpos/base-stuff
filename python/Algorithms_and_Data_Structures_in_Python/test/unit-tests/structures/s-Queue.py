import Queue as queue
from stest import expect_equal

def init():
    queue_test = queue.Queue()
    queue_test.push(10)
    queue_test.push(100)
    queue_test.push('Adam')
    queue_test.push(7.5)

    return queue_test

queue_test = init()
expect_equal(queue_test.pop(), 10)
queue_test.push(1000)
expect_equal(queue_test.pop(), 100)
expect_equal(queue_test.pop(), 'Adam')
expect_equal(queue_test.pop(), 7.5)
expect_equal(queue_test.pop(), 1000)
expect_equal(queue_test.pop(), None)
    