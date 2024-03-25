"""
Create a `Ratio` class, representing the rational number 
(numerator/denominator, e.g. 1/2, 123/52 etc.).
It should have the following api:
"""


class Ratio:
    ''' represents a rational number '''
    def __init__(self, numerator: int, denominator: int):
        self.numer = numerator
        self.denom = denominator
        self.gcd = 1

    def add(self, other: 'Ratio') -> 'Ratio':
        ''' add the rational numbers '''
        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom + other.numer * self.denom

        gcd_value = self.greatest_common_divisor(new_numer, common_denom)
        return Ratio(new_numer//gcd_value, common_denom//gcd_value)

    def sub(self, other: 'Ratio') -> 'Ratio':
        ''' subtract the rational numbers '''

        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom - other.numer*self.denom

        gcd_value = self.greatest_common_divisor(new_numer, common_denom)
        return Ratio(new_numer//gcd_value, common_denom//gcd_value)

    def mul(self, other: 'Ratio') -> 'Ratio':
        ''' multiply the rational numbers '''

        multiplied_numer = self.numer * other.numer
        multiplied_denom = self.denom * other.denom

        gcd_value = self.greatest_common_divisor(multiplied_numer, multiplied_denom)
        return Ratio(multiplied_numer//gcd_value, multiplied_denom//gcd_value)

    def div(self, other: 'Ratio') -> 'Ratio':
        ''' divide the rational numbers '''

        divided_numer = self.numer * other.denom
        divided_denom = self.denom * other.numer

        gcd_value = self.greatest_common_divisor(divided_numer, divided_denom)
        return Ratio(divided_numer//gcd_value, divided_denom//gcd_value)

    def greatest_common_divisor(self, numerator: int, denominator: int) -> int:
        ''' find greatest common divisor '''

        for i in range(1, min(abs(numerator), abs(denominator)) + 1):
            if numerator % i == 0 and denominator % i == 0:
                self.gcd = i
        return self.gcd

    def to_float(self) -> float:
        ''' convert the rational number to float '''
        return self.numer/self.denom

    def to_string(self) -> str:
        ''' convert the rational number to string '''
        return f"{self.numer}/{self.denom}" #интерполяция


if __name__ == "__main__":
    x = Ratio(-3,8)
    y = Ratio(-5,9)

    #print("add result = ", x.add(y))
    #print("sub result = ", x.sub(y))
    print("mul result = ", x.mul(y).to_string())
    print("div result = ", x.div(y).to_string())
    print(x.to_string(), x.to_float())
    assert x.to_string() == "-3/8"
