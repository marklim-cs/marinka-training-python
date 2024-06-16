# compute n-th fibonacci number using only loops
# fibonacci(0) = 0, fibonacci(1) = 1
# every next fibonacci number is a sum of two previous fibonacci numbers

def fibonacci(n: int) -> int:
    if n < 0:
        raise TypeError('negative numbers are not supported')
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 2) + fibonacci(n - 1)

