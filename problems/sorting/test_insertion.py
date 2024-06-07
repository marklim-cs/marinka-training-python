import unittest
from .insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion(self):
        arr = [-100, 8, -2, 10, 3, -101]
        insertion_sort(arr)
        self.assertEqual(arr, [-101, -100, -2, 3, 8, 10])

if __name__ == '__main__':
    unittest.main()
