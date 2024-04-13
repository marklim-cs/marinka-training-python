class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dictionary = {}

        for i, value in enumerate(nums):
            other_index = dictionary.get(target-value)
            if other_index is not None:
                return [other_index, i]

            dictionary[value] = i

if __name__ == "__main__":
    import unittest
    class TestTwoSum(unittest.TestCase):
        '''test class Ratio'''
        def setUp(self):
            self.solution = Solution()

        def test_case1(self):
            self.assertEqual(self.solution.twoSum([2,7,11,15], 9), [0, 1])

        def test_case2(self):
            self.assertEqual(self.solution.twoSum([3,3], 6), [0, 1])
            
        def test_case3(self):
            self.assertEqual(self.solution.twoSum([3,2,4], 6), [1, 2])

    unittest.main()