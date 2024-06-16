# compute the factorial of n using only loops
# factorial of n is a product (1 * 2 * 3 * ... * n-1) * n

def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)
