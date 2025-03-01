def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = {n for n in range(1, 51) if is_prime(n)}
sorted_primes = sorted(prime_numbers)
print(sorted_primes)
