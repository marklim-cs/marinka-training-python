# # gcd solved with a loop
# def gcd(a: int, b: int) -> int:
#     '''compute the greatest common divisor of 2 non-negative integers'''
#     if a == 0 or b == 0:
#         return 1

#     if a < b:
#         a, b = b, a

#     while b > 0:
#         a, b = b, a % b

#     return a

# outter (public) function which can accept any positive a and b
def gcd(a: int, b: int) -> int:
    # inner (private) recursive function which is only called with a >= b
    def gcd_rec(a: int, b: int) -> int:
        '''compute the greatest common divisor of 2 non-negative integers'''
        if b == 0:
            return a

        return gcd_rec(b, a % b)

    if a < b:
        a, b = b, a

    # call inner function with correct arguments
    return gcd_rec(a, b)
