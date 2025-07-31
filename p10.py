"""

prime_sieve(limit): Implements the classic Sieve of Eratosthenes to identify all prime numbers <= limit.
prime_sum(limit): Uses prime_sieve to return the sum of all prime numbers <= limit.

Time Complexity:
- prime_sieve: O(n log log n), where n = limit.
- prime_sum:    O(n), due to the linear scan to sum the primes.

Space Complexity:
- O(n) for storing the boolean array is_prime[0..limit]

"""

def prime_sieve(limit):
    is_prime = [True] * (limit + 1)      # assume all numbers are prime initially
    is_prime[0] = is_prime[1] = False    # 0 and 1 are not prime by definition

    for p in range(2, int(limit ** 0.5) + 1):  # check up to sqrt(limit)
        if is_prime[p]:                        # if p is prime
            # mark all multiples of p from p^2 up to limit as non-prime
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    return is_prime  # boolean array: is_prime[i] == True iff i is prime


def prime_sum(limit):
    primes_mixed = prime_sieve(limit)                  # get prime flags
    primes = [i for i, j in enumerate(primes_mixed)    # extract prime numbers
              if j == True]
    return sum(primes)  # return the sum of all primes <= limit


print(prime_sum(2000000))  # prints the sum of all primes <= 2,000,000
