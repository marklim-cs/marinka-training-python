"""
Create a `Ratio` class, representing the rational number (numerator/denominator, e.g. 1/2, 123/52 etc.).
It should have the following api:
"""

from typing import Self

class Ratio:
    def __init__(self, numerator: int, denominator: int):
        self.numer = numerator
        self.denom = abs(denominator)

    def add(self, other: Self) -> Self:         
        self.common_denom = self.denom * other.denom
        self.new_numer = self.numer * other.denom + other.numer * self.denom

        gcd_value = self.greatest_common_diviser(self.new_numer, self.common_denom)
        return f"{self.new_numer//gcd_value}/{self.common_denom//gcd_value}"

    def sub(self, other: Self) -> Self:
        self.common_denom = self.denom * other.denom
        self.new_numer = self.numer * other.denom - other.numer*self.denom

        gcd_value = self.greatest_common_diviser(self.new_numer, self.common_denom)
        return f"{self.new_numer//gcd_value}/{self.common_denom//gcd_value}"

    def mul(self, other: Self) -> Self:
        self.multiplied_numer = self.numer * other.numer
        self.multiplied_denom = self.denom * other.denom

        gcd_value = self.greatest_common_diviser(self.multiplied_numer, self.multiplied_denom)
        return f"{self.multiplied_numer//gcd_value}/{self.multiplied_denom//gcd_value}"

    def div(self, other: Self) -> Self:
        self.divied_numer = self.numer * other.denom
        self.divied_denom = self.denom * other.numer

        gcd_value = self.greatest_common_diviser(self.divied_numer, self.divied_denom)
        return f"{self.divied_numer//gcd_value}/{self.divied_denom//gcd_value}"

    def greatest_common_diviser(self, numerator: int, denominator: int) -> int:
        self.numerator = numerator
        self.denominator = denominator
        self.gcd = 1

        for i in range(1, min(abs(self.numerator), abs(self.denominator)) + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                self.gcd = i 
        return self.gcd

    def to_float(self) -> float:
        return self.numer/self.denom

    def to_string(self) -> str:
        return f"{self.numer}/{self.denom}" #интерполяция


if __name__ == "__main__":
    x = Ratio(-3,8)
    y = Ratio(-5,9)

    #print("add result = ", x.add(y))
    #print("sub result = ", x.sub(y))
    print("mul result = ", x.mul(y))
    print("div result = ", x.div(y))
    print(x.to_string(), x.to_float())
    assert(x.to_string() == "-3/8")
