class Node:
    """Represents a single node in the stack linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """A Linked List-based Stack implementation."""
    def __init__(self):
        self.top = None

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return self.top is None

    def push(self, data) -> None:
        """Adds an element to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        """Removes and returns the top element of the stack."""
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data

    def peek(self):
        """Returns the top element without removing it."""
        if self.is_empty():
            return None
        return self.top.data

    def to_list(self) -> list:
        """Returns all elements as a Python list from top to bottom."""
        elements = []
        current = self.top
        while current:
            elements.append(current.data)
            current = current.next
        return elements
