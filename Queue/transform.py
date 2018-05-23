import Stack.arraystack
import Queue.linkedqueue
import Stack.linkedstack
import Queue.arrayqueue


def queue2stack(my_queue):
    """Return new stack, which is transformed queue with the same order"""
    if not (isinstance(my_queue, Queue.linkedqueue.LinkedQueue) or isinstance(my_queue, Queue.arrayqueue.ArrayQueue)):
        raise TypeError
    temp_stack = Stack.linkedstack.LinkedStack()
    my_stack = Stack.linkedstack.LinkedStack()

    try:
        while True:
            temp_stack.push(my_queue.pop())
    except KeyError:
        pass

    try:
        while True:
            my_stack.push(temp_stack.pop())
    except KeyError:
        pass
    return my_stack