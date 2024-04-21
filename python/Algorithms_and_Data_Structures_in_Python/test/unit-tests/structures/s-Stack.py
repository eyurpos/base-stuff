import Stack as stack
from stest import expect_equal

def init():
    stack_test = stack.Stack()
    stack_test.push(10)
    stack_test.push(100)
    stack_test.push('Adam')
    stack_test.push(7.5)

    return stack_test


stack_test = init()

expect_equal(stack_test.pop(), 7.5)
stack_test.push(1000)
expect_equal(stack_test.pop(), 1000)
expect_equal(stack_test.pop(), 'Adam')
expect_equal(stack_test.pop(), 100)
expect_equal(stack_test.pop(), 10)
expect_equal(stack_test.pop(), None)
    