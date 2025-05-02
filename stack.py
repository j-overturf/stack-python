class Stack:
    """
    Python implementation of a Stack data structure.
    It uses LIFO (Last-in First Out) semantics to store data.
    The internal state of the Stack is a list.
    """
    # Class internal state
    stack = []

    def __init__(self):
        """
        Instantiates a new Stack object
        """
        self.stack = []

    def empty(self):
        """
        Checks if the Stack is empty.
        :return: True if the Stack is empty.
        """
        empty = False

        # If the length of the stack array is 0, then it is empty
        if len(self.stack) == 0:
            empty = True

        return empty

    def size(self):
        """
        Checks the size of the Stack.
        :return: The length of the Stack.
        """
        return len(self.stack)

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        :return: The top element of the stack.
        """
        # Check that the stack is not empty
        if self.empty():
            raise IndexError("Stack is empty")

        # Return the top element in the Stack
        return self.stack[len(self.stack) - 1]

    def push(self, element):
        """
        Pushes a new element onto the Stack.
        :param element: The element to be pushed to the Stack.
        :return:
        """
        self.stack.append(element)

    def pop(self):
        """
        Returns and removes the top element from the Stack.
        :return: The top element of the Stack.
        """
        # Check if the Stack is not empty
        if self.empty():
            raise IndexError("Stack is empty")

        # Get and remove element
        element = self.stack[len(self.stack)-1]

        self.stack.pop(len(self.stack)-1)

        return element
