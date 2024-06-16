import unittest
from .binary_search_rec import binary_search_recursive

class TestBinary(unittest.TestCase):
    def test_binary_search(self):
        '''test binary_search function'''
        self.assertEqual(binary_search_recursive([1, 2, 3, 4, 5, 6, 7, 8], 6), 6)
        # x repeats
        self.assertEqual(binary_search_recursive([1, 1, 2, 3, 4], 1), 1)
        # empty list
        self.assertEqual(binary_search_recursive([], 40), None)
        # one element
        self.assertEqual(binary_search_recursive([2], 2), 2)
        # x is not in the list
        self.assertEqual(binary_search_recursive([2], 4), None)
        self.assertEqual(binary_search_recursive([2, 4, 6, 8, 10], 11), None)
        # last element
        self.assertEqual(binary_search_recursive([5, 6, 7, 8], 8), 8)
        # x = 0 is the first element
        self.assertEqual(binary_search_recursive([0, 1, 2, 3, 4], 0), 0)
        # negative numbers
        self.assertEqual(binary_search_recursive([-5, -6, -7, 8, 20], -7), -7)

if __name__ == '__main__':
    unittest.main()
