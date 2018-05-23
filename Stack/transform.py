import Stack.arraystack
import Queue.linkedqueue
import Stack.linkedstack
import Queue.arrayqueue


def stack2queue(my_stack):
    """Return new queue, which is transformed stack with the same order"""
    if not (isinstance(my_stack, Stack.linkedstack.LinkedStack) or isinstance(my_stack, Stack.arraystack.ArrayStack)):
        raise TypeError
    temp_stack = Stack.linkedstack.LinkedStack()
    my_queue = Queue.linkedqueue.LinkedQueue()

    try:
        while True:
            temp_stack.push(my_stack.pop())
    except KeyError:
        pass

    try:
        while True:
            my_queue.add(temp_stack.pop())
    except KeyError:
        pass
    return my_queue
