# Write a function to check if number is prime or not. Using this function print first 15 prime numbers​


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


def first_n_primes(n):
    """
    Prints the first 'n' prime numbers.

    Args:
        n: The number of prime numbers to print.
    """
    primes_found = 0
    num = 2
    prime_numbers = []

    while primes_found < n:
        if is_prime(num):
            prime_numbers.append(num)
            primes_found += 1
        num += 1
    print(f"The first {n} prime numbers are: {prime_numbers}")


n = 15
# print(first_n_primes(n))
