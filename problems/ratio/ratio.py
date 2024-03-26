"""
Create a `Ratio` class, representing the rational number
(numerator/denominator, e.g. 1/2, 123/52 etc.).
"""

def gcd(a: int, b: int) -> int:
    '''compute the greatest common divisor of 2 non-negative integers'''
    if a == 0 or b == 0:
        return 1

    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a

class Ratio:
    ''' represents a rational number '''
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be 0")

        self.numer = numerator
        self.denom = denominator
        self.normalize()

    def add(self, other: 'Ratio') -> 'Ratio':
        ''' add the rational numbers '''
        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom + other.numer * self.denom

        return Ratio(new_numer, common_denom)

    def sub(self, other: 'Ratio') -> 'Ratio':
        ''' subtract the rational numbers '''

        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom - other.numer*self.denom

        return Ratio(new_numer, common_denom)

    def mul(self, other: 'Ratio') -> 'Ratio':
        ''' multiply the rational numbers '''

        multiplied_numer = self.numer * other.numer
        multiplied_denom = self.denom * other.denom

        return Ratio(multiplied_numer, multiplied_denom)

    def div(self, other: 'Ratio') -> 'Ratio':
        ''' divide the rational numbers '''

        divided_numer = self.numer * other.denom
        divided_denom = self.denom * other.numer

        return Ratio(divided_numer, divided_denom)

    def normalize(self):
        ''' normalize the ratio:
            - divides numerator and denominator by their gcd
            - moves minus sign from denominator to numerator
        '''

        abs_gcd = gcd(abs(self.numer), abs(self.denom))
        self.numer //= abs_gcd
        self.denom //= abs_gcd

        if self.denom < 0:
            self.numer = -self.numer
            self.denom = -self.denom

    def to_float(self) -> float:
        ''' convert the rational number to float '''
        return self.numer/self.denom

    def to_string(self) -> str:
        ''' convert the rational number to string '''
        return f"{self.numer}/{self.denom}"