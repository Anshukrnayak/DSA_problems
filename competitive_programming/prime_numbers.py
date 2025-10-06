import math
# Integer square root
def sqrt(n):
    if n == 0 or n == 1:
        return n
    s, e = 0, n
    ans = 0
    while s <= e:
        mid = s + (e - s) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1
    return ans

# Prime check using sqrt optimization
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, sqrt(n) + 1,2):
        # print(i)  # optional, for debugging
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    factors = {}

    # Factor out 2
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2

    # Factor out odd numbers from 3 upwards
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
        i += 2

    # If remaining n is prime
    if n > 1:
        factors[n] = 1

    return factors


# Example
n = 84
factors = prime_factors(n)
print(f"Prime factorization of {n}: ", end="")
for prime, power in factors.items():
    print(f"{prime}^{power}", end=" * " if prime != list(factors.keys())[-1] else "")

print(f'Is prime: {is_prime(31)}')
