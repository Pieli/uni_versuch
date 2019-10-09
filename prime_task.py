import math

def is_prime(n):
    if n == 1:
        return '1 is the multiplicative identity'
    for t in range(2, int(math.sqrt(n)) + 1):
        if n % t == 0:
            b = str(n // t)
            return f'{str(n)} is not a prime number ({str(t)} * {b} = {str(n)})'
    return f'{n} is prime'
