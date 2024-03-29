import unittest

from ratio import Ratio, DividingByZeroError

class TestRatio(unittest.TestCase):
    '''test class Ratio'''
    def setUp(self):
        self.ratio = Ratio(numerator=-4, denominator=9)
        self.different_denom = Ratio(numerator=6, denominator=7)
        self.equal_denom = Ratio(numerator=5, denominator=9)
        self.negative_numer = Ratio(numerator=-7, denominator=12)
        self.negative_denom = Ratio(numerator=8, denominator=-12)
        self.equal_to_ratio = Ratio(numerator=-4, denominator=9)

    def test_0_magic_add(self):
        '''different denominators: test __add__ method'''
        result = self.ratio + (self.different_denom)
        self.assertEqual(result.to_string(), "26/63")
    
    def test_1_magic_add(self):
        '''negative numerators: test __add__ method'''
        result = self.ratio + self.equal_denom
        self.assertEqual(result.to_string(), "1/9")

    def test_0_magic_sub(self):
        '''different denominators: test __sub__ method'''
        result = self.ratio - self.different_denom
        self.assertEqual(result.to_string(), "-82/63")

    def test_0_magic_mul(self):
        '''negative numerators: test __mul__ method'''
        result = self.ratio * self.negative_numer
        self.assertEqual(result.to_string(), "7/27")

    def test_0_magic_div(self):
        '''negative denominator: test __div__ method'''
        result = self.ratio // self.negative_denom
        self.assertEqual(result.to_string(), "2/3")

    def test_0_magic_notequal(self):
        ''' not equal: test __ne__ method'''
        self.assertTrue(self.ratio != self.negative_denom)

    def test_1_magic_equal(self):
        ''' equal: test __eq__ method'''
        self.assertTrue(self.ratio == self.equal_to_ratio)

    def test_0_magic_less_than(self):
        ''' is less than: test __lt__ method'''
        self.assertTrue(self.ratio < self.equal_denom)

    def test_1_magic_less_than(self):
        ''' not less than: test __lt__ method'''
        self.assertFalse(self.ratio < self.equal_to_ratio)

    def test_0_magic_less_equal(self):
        ''' is less equal: test __le__ method'''
        self.assertTrue(self.ratio <= self.equal_to_ratio)

    def test_1_magic_less_equal(self):
        ''' not less equal: test __le__ method'''
        self.assertFalse(self.negative_numer <= self.negative_denom)

    def test_2_magic_less_equal(self):
        '''equal: test __le__ method'''
        self.assertTrue(self.ratio <= self.equal_to_ratio)

    def test_0_magic_greater_than(self):
        ''' is greater than: test __gt__ method'''
        self.assertTrue(self.negative_numer > self.negative_denom)

    def test_1_magic_greater_than(self):
        ''' not greater than: test __gt__ method'''
        self.assertFalse(self.ratio > self.different_denom)

    def test_0_magic_greater_equal(self):
        ''' is greater equal: test __ge__ method'''
        self.assertTrue(self.ratio >= self.equal_to_ratio)

    def test_1_magic_greater_equal(self):
        ''' not greater equal: test __ge__ method'''
        self.assertFalse(self.ratio >= self.equal_denom)

    def test_2_magic_greater_equal(self):
        '''equal: test __ge__ method'''
        self.assertTrue(self.ratio >= self.equal_to_ratio)

    def test_0_magic_invert(self):
        '''check if the rational number was inverted'''
        inverted_ratio = ~self.different_denom
        self.assertEqual(inverted_ratio.to_string(), "7/6")

    def test_new_ratio_is_normal(self):
        '''check if newly constructed ratio is normalized'''
        self.assertEqual(Ratio(2, 4).to_string(), "1/2")

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

    def test_denom_is_positive_after_div(self):
        '''denominator remains positive after dividing by a ratio with a negative numerator'''
        a = Ratio(1, 2)
        b = Ratio(-1, 2)
        result = a.div(b)
        self.assertEqual(result.to_string(), "-1/1")

    def test_0_to_float(self):
        '''convert rational number to float'''
        result = self.ratio.to_float()
        self.assertAlmostEqual(result, -0.4444444444444444)

    def test_0_to_dict(self):
        '''provide rational in a dict form'''
        self.assertEqual(self.equal_denom.to_dict(), {"numerator":"5", "denominator":"9"})

    def test_0_from_dict(self):
        '''convert dict to rational number'''
        ratio_dict = {"numerator":"5", "denominator":"7"}
        result = Ratio.from_dict(ratio_dict)
        self.assertEqual(result, Ratio(5, 7))

    def test_0_denominator_is_zero_error(self):
        '''checks if the DividingByZeroError is raised when denominator = 0'''
        ugly_ratio = Ratio(7, 0)
        self.assertRaises(DividingByZeroError, ugly_ratio)
    
    def test_0_div_zero_numerator_error(self):
        '''checks if the DividingByZeroError is raised when numerator = 0 in division'''
        zero_numerator = Ratio(0, 6)
        result = self.ratio.div(zero_numerator)
        self.assertRaises(DividingByZeroError, result)

if __name__ == '__main__':
    unittest.main()
