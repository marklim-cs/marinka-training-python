import unittest
from .binary_search import binary_search

class TestBinary(unittest.TestCase):
    def test_binary_search(self):
        '''test binary_search function'''
        self.assertEqual(binary_search([10, 20, 30, 40, 50, 60, 70, 80], 60), 60)
        self.assertEqual(binary_search([10, 10, 20, 30, 40], 10), 10)
        self.assertEqual(binary_search([], 40), None)
        self.assertEqual(binary_search([2], 2), 2)
        self.assertEqual(binary_search([2], 4), None)
        self.assertEqual(binary_search([2, 4, 6, 8, 10], 11), None)
        self.assertEqual(binary_search([505, 506, 507, 700], 700), 700)

if __name__ == '__main__':
    unittest.main()
