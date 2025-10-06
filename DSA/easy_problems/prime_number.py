def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check divisors from 5 to √n, skipping even numbers
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def main():
    try:
        n = int(input('Enter a number: '))
        ans = is_prime(n)
        print(f'Is {n} a prime number? {ans}')
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == '__main__':
    main()