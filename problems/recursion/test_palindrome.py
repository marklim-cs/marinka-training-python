import unittest
from .palindrome_r import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_polidrome(self):
        self.assertEqual(is_palindrome("abcba"), True)

if __name__ == '__main__':
    unittest.main()
