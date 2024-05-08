'''test SelectionSort'''
import unittest
from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_sort(self):
        '''checks selection sort functionality'''
        arr = [4, 7, 1, -10, 5]
        selection_sort(arr)
        self.assertEqual(arr, [-10, 1, 4, 5, 7])

if __name__ == '__main__':
    unittest.main()
