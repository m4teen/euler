
def nth_prime(n):
    primes = [2]
    m = 3
    while len(primes) < n:
        if any(m % i == 0 for i in primes):
            m += 2
            continue
        else:
            primes.append(m)
            m += 2
    return primes[-1]

print(nth_prime(10001))


def prime_sieve(n):
    pass