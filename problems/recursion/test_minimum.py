import unittest
from .minimum import minimum, minimum_index

class TestMinimum(unittest.TestCase):
    def test_minimum(self):
        self.assertEqual(minimum([2, 4, 5, 1]), 1)
        self.assertEqual(minimum([24, 40, 550, 20]), 20)
        self.assertEqual(minimum([24, 40, 550, 45]), 24)
        self.assertEqual(minimum([]), None)
        self.assertEqual(minimum([2]), 2)

    def test_minimum_index(self):
        self.assertEqual(minimum_index([2, 4, 5, 1]), 3)
        self.assertEqual(minimum_index([24, 40, 550, 20]), 3)
        self.assertEqual(minimum_index([24, 40, 550, 45]), 0)
        self.assertEqual(minimum_index([]), None)
        self.assertEqual(minimum_index([24, -40, -550, 45]), 2)
        self.assertEqual(minimum_index([2, 1, 2, 3, 1]), 1)

if __name__ == '__main__':
    unittest.main()