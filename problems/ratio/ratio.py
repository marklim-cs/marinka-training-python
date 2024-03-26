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

        if self.denom == 0 or self.denom < 0:
            raise ValueError("Denominator cannot be equal to 0 or negative")

    def add(self, other: 'Ratio') -> 'Ratio':
        ''' add the rational numbers '''
        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom + other.numer * self.denom

        new_numer, common_denom = self.normalize(new_numer, common_denom)
        return Ratio(new_numer, common_denom)

    def sub(self, other: 'Ratio') -> 'Ratio':
        ''' subtract the rational numbers '''

        common_denom = self.denom * other.denom
        new_numer = self.numer * other.denom - other.numer*self.denom

        new_numer, common_denom = self.normalize(new_numer, common_denom)
        return Ratio(new_numer, common_denom)

    def mul(self, other: 'Ratio') -> 'Ratio':
        ''' multiply the rational numbers '''

        multiplied_numer = self.numer * other.numer
        multiplied_denom = self.denom * other.denom

        multiplied_numer, multiplied_denom = self.normalize(multiplied_numer, multiplied_denom)
        return Ratio(multiplied_numer, multiplied_denom)

    def div(self, other: 'Ratio') -> 'Ratio':
        ''' divide the rational numbers '''

        divided_numer = self.numer * other.denom
        divided_denom = self.denom * other.numer

        divided_numer, divided_denom = self.normalize(divided_numer, divided_denom)
        return Ratio(divided_numer, divided_denom)

    def normalize(self, numerator: int, denominator: int) -> tuple[int, int]:
        ''' find greatest common divisor and eliminate '-' if bothe numer and denom are negative'''
        gcd = 1

        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)
        
        for i in range(1, min(abs(numerator), abs(denominator)) + 1):
            if numerator % i == 0 and denominator % i == 0:
                gcd = i
        normalized_numer = numerator//gcd
        normalized_denom = denominator//gcd
        return normalized_numer, normalized_denom

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
    assert(x.to_string() == "-3/8")
