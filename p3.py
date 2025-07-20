def largest_prime_factor(n):
    while n % 2 == 0:
        n //= 2
        largest = 2
    
    # Now n is odd, try only odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            n //= i
            largest = i
        i += 2

    # If anything's left, it's prime
    if n > 1:
        largest = n

    return largest
print(largest_prime_factor(600851475143))