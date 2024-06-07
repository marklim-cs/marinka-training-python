'''test'''
import unittest
from .fibonacci_r import fibonacci

class TestFibonacci(unittest.TestCase):
    '''test'''
    def test_fibonacci(self):
        '''test fibonacci function'''
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(10), 55)
        with self.assertRaises(TypeError):
            fibonacci(-10)

if __name__ == "__main__":
    unittest.main()
