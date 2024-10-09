import unittest
from search.linear import LinearSearch


class TestLinearSearch(unittest.TestCase):

    def setUp(self):
        self.linear_search = LinearSearch(data=[1, 2, 3, 4, 5, 3, 7, 3])

    def test_get_data(self):
        # Test if data is initialized correctly
        self.assertEqual(self.linear_search.get_data(), [1, 2, 3, 4, 5, 3, 7, 3])

    def test_add_data(self):
        # Test if add_data correctly appends an element
        self.linear_search.add_data(10)
        self.assertEqual(self.linear_search.get_data(), [1, 2, 3, 4, 5, 3, 7, 3, 10])

    def test_remove_element(self):
        # Test removing a single element
        self.linear_search.remove_element(3)
        self.assertEqual(self.linear_search.get_data(), [1, 2, 4, 5, 3, 7, 3])

    def test_remove_element_non_existent(self):
        # Test removing an element that doesn't exist
        self.linear_search.remove_element(99)
        self.assertEqual(self.linear_search.get_data(), [1, 2, 3, 4, 5, 3, 7, 3])

    def test_remove_elements(self):
        # Test removing multiple elements
        self.linear_search.remove_elements(3)
        self.assertEqual(self.linear_search.get_data(), [1, 2, 4, 5, 7])

    def test_search_found(self):
        # Test searching for an existing element
        index = self.linear_search.search(3)
        self.assertEqual(index, 2)

    def test_search_not_found(self):
        # Test searching for a non-existing element
        index = self.linear_search.search(99)
        self.assertEqual(index, -1)

    def test_search_with_repetition(self):
        # Test searching for an element with multiple occurrences
        indices = self.linear_search.search_with_repetition(3)
        self.assertEqual(indices, [2, 5, 7])

    def test_search_with_repetition_no_match(self):
        # Test searching for an element with no matches
        indices = self.linear_search.search_with_repetition(99)
        self.assertEqual(indices, [])
