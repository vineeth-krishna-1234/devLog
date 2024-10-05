import unittest
from data_structures.queue.array_queue import ArrayQueue


class TestArrayQueue(unittest.TestCase):

    def setUp(self):
        self.queue = ArrayQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.size(), 3)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(100)
        self.assertFalse(self.queue.is_empty())

    def test_peek(self):
        self.assertIsNone(self.queue.peek())
        self.queue.enqueue("test")
        self.assertEqual(self.queue.peek(), "test")

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

    def test_clear(self):
        self.queue.enqueue(5)
        self.queue.enqueue(6)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_empty_queue(self):
        self.assertIsNone(self.queue.dequeue())

    def test_peek_empty_queue(self):
        self.assertIsNone(self.queue.peek())
