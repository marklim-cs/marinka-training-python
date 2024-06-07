import unittest
from .stars import Solution

class TestStars(unittest.TestCase):
    def test_stars(self):
        s = Solution()
        self.assertEqual(s.remove_stars("leet**cod*e"), "lecoe")
        self.assertEqual(s.remove_stars("erase*****"), "")
        self.assertEqual(s.remove_stars("erase"), "erase")
        self.assertEqual(s.remove_stars("*"), "")
        self.assertEqual(s.remove_stars(""), "")

if __name__ == '__main__':
    unittest.main()