"""
Implement Queue using Stacks
"""
class Node:
    """A singly linked list node."""
    def __init__(self, val, next_=None):
        """Initializes the node."""
        self.val = val
        self.next = next_

class Stack:
    """A LIFO stack implementation using a linked list."""
    def __init__(self):
        """Initializes an empty stack."""
        self.head = None

    def push(self, x: int) -> None:
        """Pushes an element onto the top of the stack."""
        self.head = Node(x, self.head)

    def pop(self) -> int:
        """Removes and returns the top element of the stack."""
        if self.head is None:
            return None
        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self) -> int:
        """Returns the top element without removing it."""
        if self.head is None:
            return None
        return self.head.val

    def empty(self) -> bool:
        """Checks if the stack is empty."""
        return self.head is None

class MyQueue:
    """A FIFO queue implemented using two stacks."""
    def __init__(self):
        """Initializes the queue with input and output stacks."""
        self.stack_in = Stack()
        self.stack_out = Stack()

    def create_stack_out(self):
        """Transfers elements from input to output stack if needed."""
        if self.stack_out.empty():
            while not self.stack_in.empty():
                self.stack_out.push(self.stack_in.pop())

    def push(self, x: int) -> None:
        """Pushes an element to the back of the queue."""
        self.stack_in.push(x)

    def pop(self) -> int:
        """Removes and returns the element at the front of the queue."""
        self.create_stack_out()
        return self.stack_out.pop()

    def peek(self) -> int:
        """Returns the element at the front of the queue without removing it."""
        self.create_stack_out()
        return self.stack_out.peek()

    def empty(self) -> bool:
        """Checks if the queue is empty."""
        return self.stack_in.empty() and self.stack_out.empty()
