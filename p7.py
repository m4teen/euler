"""

This function-th prime finds the n-th prime by checking successive odd numbers for primality using trial division 
against all previously found primes. It starts from 2 and tests each candidate up to the desired count.

Time complexity: O(n√p), where p is the n-th prime (since each number is tested against all prior primes)
Space complexity: O(n), for storing the list of found primes

"""

def nth_prime(n):
    primes = [2]  # start with the first prime
    m = 3         # candidate number to test
    while len(primes) < n:
        # check if m is divisible by any known prime
        if any(m % i == 0 for i in primes):
            m += 2  # skip even numbers, increment to next odd
            continue
        else:
            primes.append(m)  # m is prime, add it
            m += 2
    return primes[-1]  # return the n-th prime

print(nth_prime(10001))  # Expected: 104743


"""

This algorithm uses a sieve to precompute all primes <= limit and dynamically doubles the limit 
until it finds at least n primes. It is marginally more 
efficient than the nth_prime function.
Time complexity: Amortised O(n log log N), where N is the value of the n-th prime
Space complexity: O(N), where N is the size of the current sieve array

"""

def prime_sieve(limit):
    is_prime = [True] * (limit + 1)  # assume all numbers are prime
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            # mark all multiples of p as non-prime
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    # extract indices of all primes
    return [i for i, prime in enumerate(is_prime) if prime]


def nth_prime_new(n):
    limit = 100  # initial guess

    while True:
        primes = prime_sieve(limit)
        if len(primes) >= n:
            return primes[n - 1]  # return the n-th prime (0-indexed)
        limit *= 2  # increase the range and try again

print(nth_prime_new(10001))  # Expected: 104743
