def prime_sieve(n):
    # Initialise a dictionary to store primes, with key 0 mapped to the first prime (2)
    primes = {0: 2}
    count = 1  # Counter to assign keys to new primes
    
    # Loop through numbers from 2 to n inclusive
    for i in range(2, n + 1):
        # Check if i is divisible by any known prime
        if any(i % p == 0 for p in primes.values()):
            continue  # Not a prime, skip
        else:
            primes[count] = i  # Store the new prime
            count += 1
    
    # Initialise current_max with the first prime
    current_max = next(iter(primes.values()))
    
    # Find the largest prime in the sieve that divides n
    for j in primes.values():
        if n % j == 0 and j > current_max:
            current_max = j
        else:
            continue

    return current_max


"""

This was my first attempt, it was a direct representation of the mathematical problem in code. 
It generates all primes up to n using a dictionary and tests each integer 
for primality by dividing it by all previously found primes. Once the sieve is built, it 
searches for the largest prime factor of n by checking which primes divide n.

Time complexity: O(n^2 / log n), due to checking divisibility for every integer up to n
against an increasingly large list of previously found primes.

Space complexity: O(n / log n), since it stores all primes up to n.

"""


def largest_prime_factor(n):
    # Divide out all factors of 2 first
    while n % 2 == 0:
        n //= 2
        largest = 2
    
    # Now n is odd, try only odd factors starting from 3
    i = 3
    while i * i <= n:
        # While i divides n, divide it out completely
        while n % i == 0:
            n //= i
            largest = i
        i += 2  # Increment to next odd number

    # If any factor remains, it must be prime and the largest
    if n > 1:
        largest = n

    return largest


"""

This optimised approach avoids generating a full list of primes. Instead, it performs 
trial division: starting from 2, it repeatedly divides out prime factors from n, reducing 
n until all smaller factors are removed. After 2 is handled, it only checks odd numbers, 
since all even numbers would already be factored out. After removing the even numbers, 
the function implements a greedy, compressed factor tree to quickly 
find the prime factors. 


Time complexity: O(√n), since only divisors up to the square root of n are tested,
and each factor is divided out completely when located.

Space complexity: O(1), as it uses only a fixed number of integer variables.


"""

# Example usage
print(largest_prime_factor(600851475143))
