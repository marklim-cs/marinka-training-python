import unittest
from stack import Stack, Word

class TestStack(unittest.TestCase):
    '''stack test'''
    def test_stack(self):
        '''method test'''
        s = Stack()
        self.assertEqual(s.is_empty(), True)
        with self.assertRaises(IndexError):
            s.pop()
        self.assertEqual(s.push(10), [10])
        s.push(30)
        s.push(30)
        s.push(55)
        self.assertEqual(s.push(10), [10, 30, 30, 55, 10])
        self.assertEqual(s.pop(), 10)

    def test_word(self):
        '''reverse word test'''
        w = Word("denis")
        self.assertEqual(w.reverse_word(), "sined")
if __name__ == '__main__':
    unittest.main()
