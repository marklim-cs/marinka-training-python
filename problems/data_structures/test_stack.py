import unittest
from .stack_struct import Stack

class TestStack(unittest.TestCase):
    '''stack test'''
    def test_push(self):
        '''method test'''
        s = Stack()
        s.push(30)
        s.push(40)
        s.push(50)
        self.assertEqual(s.to_list(), [30, 40, 50])
        s.push(10)
        self.assertEqual(s.to_list(), [30, 40, 50, 10])

    def test_pop(self):
        s = Stack()
        self.assertEqual(s.pop(), None)
        s.push(30)
        self.assertEqual(s.to_list(), [30])
        self.assertEqual(s.pop(), 30)
        s.push(30)
        s.push(40)
        s.push(50)
        s.push(60)
        self.assertEqual(s.to_list(), [30, 40, 50, 60])
        self.assertEqual(s.pop(), 60)
        self.assertEqual(len(s), 3)

if __name__ == '__main__':
    unittest.main()
