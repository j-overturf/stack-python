import unittest
import stack


class StackUnitTests(unittest.TestCase):
    """
    Class that contains all the Stack unit tests.
    """

    def test_empty_isEmpty(self):
        """
        Creates a new Stack and then calls the empty function
        :return: True since the Stack should be empty.
        """
        new_stack = stack.Stack()
        self.assertTrue(new_stack.empty())

    def test_empty_isNotEmpty(self):
        """
        Creates a new Stack, pushes an element, and then calls the empty function
        :return: False since the Stack should not be empty.
        """
        new_stack = stack.Stack()
        new_stack.push(1)
        self.assertFalse(new_stack.empty())

    def test_size(self):
        """
        Creates a new Stack, pushes a few elements, and then calls the size function
        :return: True since the Stack should be empty.
        """
        new_stack = stack.Stack()

        # Push elements
        new_stack.push(3)
        new_stack.push(10)
        new_stack.push(89)

        self.assertEqual(new_stack.size(), 3)

    def test_peek_isEmpty(self):
        """
        Creates a new Stack, and then calls the peek function
        :return: IndexError since the Stack is empty.
        """
        new_stack = stack.Stack()

        # Ensure peek returns an error since the Stack is empty.
        with self.assertRaises(IndexError):
            new_stack.peek()

    def test_peek_isNotEmpty(self):
        """
        Creates a new Stack, pushes a few elements, and then calls the peek function
        :return: The top element.
        """
        new_stack = stack.Stack()

        # Push elements
        new_stack.push("hello")
        new_stack.push("test")
        new_stack.push(True)

        self.assertEqual(new_stack.peek(), True)

    def test_push(self):
        """
        Creates a new Stack, pushes a new element
        :return: The element that was pushed.
        """
        new_stack = stack.Stack()

        # Push elements
        new_stack.push("hello")

        self.assertEqual(new_stack.peek(), "hello")

    def test_pop_isEmpty(self):
        """
        Creates a new Stack, pops an element
        :return: Error since the Stack is empty.
        """
        new_stack = stack.Stack()

        # Ensure pop returns an error since the Stack is empty.
        with self.assertRaises(IndexError):
            new_stack.pop()

    def test_pop_isNotEmpty(self):
        """
        Creates a new Stack, pops an element
        :return: Error since the Stack is empty.
        """
        new_stack = stack.Stack()

        # Pushes elements
        new_stack.push("hello")
        new_stack.push("test")

        self.assertEqual(new_stack.pop(), "test")


if __name__ == '__main__':
    unittest.main()
