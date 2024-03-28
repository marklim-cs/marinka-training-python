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
            raise CannotDivideByZeroError()

        self.numer = numerator
        self.denom = denominator
        self.normalize()

    def __str__(self):
        return f"The rational number is equal to {self.numer}/{self.denom}"

    def __repr__(self):
        return f"Ratio(numerator={self.numer}, denominator={self.denom})"

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

        if self.numer == 0 or other.numer == 0:
            raise CannotDivideByZeroError()

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
        '''convert the rational number to a float'''
        return self.numer/self.denom

    def to_string(self) -> str:
        '''convert the rational number to a string'''
        return f"{self.numer}/{self.denom}"
    
    def to_dict(self) -> dict:
        '''convert the rational number to dict'''
        dict_ratio = {"numerator":f"{self.numer}", "denominator":f"{self.denom}"}
        return dict_ratio
    
    @staticmethod
    def from_dict(data: dict):
        '''convert dict to a Ratio instance'''
        numerator = int(data["numerator"])
        denominator = int(data["denominator"])
        return Ratio(numerator, denominator)

    def __add__(self, other: 'Ratio') -> 'Ratio':
        return self.add(other)

    def __sub__(self, other: 'Ratio') -> 'Ratio':
        return self.sub(other)

    def __mul__(self, other: 'Ratio') -> 'Ratio':
        return self.mul(other)

    def __floordiv__(self, other: 'Ratio') -> 'Ratio':
        return self.div(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            return self.numer == other.numer and self.denom == other.denom
        return False

    def __ne__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            return self.numer != other.numer and self.denom != other.denom
        return False

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            left_number = self.numer * other.denom
            right_number = self.denom * other.numer
            return left_number < right_number
        return False

    def __le__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            left_number = self.numer * other.denom
            right_number = self.denom * other.numer
            return left_number <= right_number
        return False

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            left_number = self.numer * other.denom
            right_number = self.denom * other.numer
            return left_number > right_number
        return False

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Ratio):
            left_number = self.numer * other.denom
            right_number = self.denom * other.numer
            return left_number >= right_number
        return False
    
    def __invert__(self) -> 'Ratio':
        if self.numer == 0:
            raise CannotDivideByZeroError()
        
        inverted_numerator = self.denom
        inverted_denominator = self.numer
        return Ratio(inverted_numerator, inverted_denominator)
    
if __name__ == '__main__':
    x = {"numerator":"5", "denominator":"7"}
    print(Ratio.from_dict(x))


class CannotDivideByZeroError(Exception):
    "Raised when a number divided by zero"

    def __init__(self, message="Operation unexecutable: the denominator is equal to zero"):
        super().__init__(message)
