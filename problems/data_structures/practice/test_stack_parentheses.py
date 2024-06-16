import unittest
from .stack_parentheses import is_valid_parentheses

class TestStackP(unittest.TestCase):
    def test_is_valid_p(self):
        self.assertEqual(is_valid_parentheses("[(({}){})]"), True)
    def test_is_valid_p1(self):
        self.assertEqual(is_valid_parentheses("{{{{}}}}"), True)
    def test_is_valid_p2(self):
        self.assertEqual(is_valid_parentheses("[]"), True)
    def test_is_valid_p3(self):
        self.assertEqual(is_valid_parentheses("{[()]}{}"), True)
    def test_is_not_valid_p(self):
        self.assertEqual(is_valid_parentheses("[(({)})]"), False)
    def test_is_not_valid_p1(self):
        self.assertEqual(is_valid_parentheses("(){][}"), False)
    def test_is_not_valid_p2(self):
        self.assertEqual(is_valid_parentheses("}{"), False)
    def test_is_not_valid_p3(self):
        self.assertEqual(is_valid_parentheses("}{["), False)
    def test_is_not_valid_p4(self):
        self.assertEqual(is_valid_parentheses("[{({})]}"), False)

if __name__ == '__main__':
    unittest.main()