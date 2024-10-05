import unittest
from data_structures.stack.array_stack import ArrayStack


class TestArrayStack(unittest.TestCase):

    def setUp(self):
        self.stack = ArrayStack()

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.size(), 0)
        self.assertIsNone(self.stack.pop())  # Pop from empty stack should return None

    def test_peek(self):
        self.assertIsNone(self.stack.peek())  # Peek on empty stack should return None
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(
            self.stack.peek(), 2
        )  # Peek should return the last pushed item

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_clear(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.clear()
        self.assertEqual(self.stack.size(), 0)
        self.assertTrue(self.stack.is_empty())


