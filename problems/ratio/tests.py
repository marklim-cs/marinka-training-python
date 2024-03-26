import unittest

from ratio import Ratio

class TestRatio(unittest.TestCase):
    '''test class Ratio'''
    def setUp(self):
        self.ratio = Ratio(numerator=-4, denominator=9)
        self.different_denom = Ratio(numerator=6, denominator=7)
        self.equal_denom = Ratio(numerator=5, denominator=9)
        self.negative_numer = Ratio(numerator=-7, denominator=12)
    
    def test_0_add(self):
        '''different denominators: test add method'''
        result = self.ratio.add(self.different_denom).to_string()
        self.assertEqual(result, "26/63")

    def test_1_add(self):
        '''equal denominators: test add method'''
        result = self.ratio.add(self.equal_denom).to_string()
        self.assertEqual(result, "1/9")

    def test_2_add(self):
        '''negative numerators: test add method'''
        result = self.ratio.add(self.negative_numer).to_string()
        self.assertEqual(result, "-37/36")

    def test_0_sub(self):
        '''different denominators: test sub method'''
        result = self.ratio.sub(self.different_denom).to_string()
        self.assertEqual(result, "-82/63")

    def test_1_sub(self):
        '''equal denominators: test sub method'''
        result = self.ratio.sub(self.equal_denom).to_string()
        self.assertEqual(result, "-1/1")

    def test_2_sub(self):
        '''negative numerators: test sub method'''
        result = self.ratio.sub(self.negative_numer).to_string()
        self.assertEqual(result, "5/36")

    def test_0_mul(self):
        '''different denominators: test mul method'''
        result = self.ratio.mul(self.different_denom).to_string()
        self.assertEqual(result, "-8/21")

    def test_1_mul(self):
        '''negative numerators: test mul method'''
        result = self.ratio.mul(self.negative_numer).to_string()
        self.assertEqual(result, "7/27")

    def test_0_div(self):
        '''negative numerators: test div method'''
        result = self.ratio.div(self.negative_numer).to_string()
        self.assertEqual(result, "16/21")

    def test_1_div(self):
        '''different denumerators: test div method'''
        result = self.ratio.div(self.different_denom).to_string()
        self.assertEqual(result, "-14/27")

    def test_1_to_float(self):
        '''convert rational number to float'''
        result = self.ratio.to_float()
        self.assertEqual(result, -0.4444444444444444)

if __name__ == '__main__':
    unittest.main()