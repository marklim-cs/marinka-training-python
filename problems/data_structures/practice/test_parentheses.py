import unittest
from .parentheses import is_valid_parentheses

class TestParentheses(unittest.TestCase):
    def test_is_valid_p(self):
        self.assertEqual(is_valid_parentheses("()()()"), True)
        self.assertEqual(is_valid_parentheses("((((((()))))))"), True)
        self.assertEqual(is_valid_parentheses("(()(()()))"), True)

    def test_is_not_valid(self):
        self.assertEqual(is_valid_parentheses(")"), False)
        self.assertEqual(is_valid_parentheses("("), False)
        self.assertEqual(is_valid_parentheses("())("), False)

if __name__ == '__main__':
    unittest.main()