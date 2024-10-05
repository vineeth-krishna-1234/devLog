import unittest
from data_structures.queue.linked_list_queue import LinkedListQueue


class TestLinkedListQueue(unittest.TestCase):

    def setUp(self):
        # Set up a fresh instance of LinkedListQueue before each test
        self.queue = LinkedListQueue()

    def test_enqueue(self):
        # Test enqueueing elements into the queue
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.size(), 3)  # Should have 3 elements
        self.assertEqual(self.queue.peek(), 10)  # Head element should be 10

    def test_dequeue(self):
        # Test dequeuing elements from the queue
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        first = self.queue.dequeue()
        second = self.queue.dequeue()
        self.assertEqual(first, 10)  # First element dequeued should be 10
        self.assertEqual(second, 20)  # Second element dequeued should be 20
        self.assertEqual(self.queue.size(), 1)  # One element should be left
        self.assertEqual(self.queue.peek(), 30)  # The remaining element should be 30

    def test_is_empty(self):
        # Test the is_empty method
        self.assertTrue(self.queue.is_empty())  # Queue should initially be empty
        self.queue.enqueue(10)
        self.assertFalse(
            self.queue.is_empty()
        )  # Queue should not be empty after enqueue

    def test_peek(self):
        # Test peeking at the front of the queue
        self.assertIsNone(
            self.queue.peek()
        )  # Peeking an empty queue should return None
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(
            self.queue.peek(), 10
        )  # Peeking should return the first element

    def test_size(self):
        # Test the size of the queue
        self.assertEqual(self.queue.size(), 0)  # Initially, size should be 0
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.size(), 2)  # After two enqueues, size should be 2
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)  # After one dequeue, size should be 1

    def test_clear(self):
        # Test clearing the queue
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())  # Queue should be empty after clearing
        self.assertEqual(self.queue.size(), 0)  # Size should be 0 after clearing
        self.assertIsNone(
            self.queue.peek()
        )  # Peeking should return None after clearing

    def test_dequeue_empty(self):
        # Test dequeuing from an empty queue
        self.assertIsNone(
            self.queue.dequeue()
        )  # Dequeueing from an empty queue should return None


