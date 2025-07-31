"""

Naive triangular number divisor search.

The function divisor_counter finds the first triangular number with more than m divisors
by generating each triangular number, enumerating all its divisors up to √n,
and counting them.

Time Complexity: O(k * √n) where k = number of triangular numbers checked and 
n = value of the first triangular number exceeding m divisors.

Space Complexity: O(√n) as it is storing divisors in a list for each check.

"""

import math 

def triangle(j):
    return j*(j+1)//2  # j-th triangular number

def divisor_counter(m):
    j = 1        # triangular number index
    x = 0        # number of divisors of the current triangular number
    while x <= m:
        factors = []             # reset factor list for this triangular number
        n = triangle(j)          # compute j-th triangular number
        for i in range(1, math.ceil(n**0.5)):
            if n % i == 0:       # found a divisor
                factors.append(i)
                factors.append(n//i)  # add paired divisor
        x = len(factors)         # count divisors for this n
        j += 1                   # move to next triangular number

    return triangle(j-1)         # j was incremented one too far

print(divisor_counter(500))  # Naïve solution


"""

Optimised triangular number divisor search using factorisation.

The approach used here in optimised_divisor_counter 
uses the formula for sum of naturals: T_j = j*(j+1)/2 and the coprimality of j and j+1
to compute the number of divisors via prime factorisation without enumerating
the divisors up to n. It runs much quicker than divisor_counter. 

Time Complexity: O(k * √j) where k = number of triangular numbers checked and 
j = index of the triangular number that satisfies the condition.

Space Complexity: O(1) as only stores counters and small variables, not divisor lists.

"""

def divisor_count(n):
    cnt = 1
    p = 2
    while p * p <= n:       # trial division up to √n
        exp = 0
        while n % p == 0:   # count exponent of prime p
            n //= p
            exp += 1
        cnt *= (exp + 1)    # update divisor count formula
        p += 1 if p == 2 else 2  # after 2, check only odd numbers
    if n > 1:               # leftover prime contributes factor 2
        cnt *= 2
    return cnt

def d(j):
    # Compute divisor count of triangular number using factorisation trick
    if j % 2 == 0:
        return divisor_count(j // 2) * divisor_count(j + 1)
    else:
        return divisor_count(j) * divisor_count((j + 1) // 2)

def optimised_divisor_counter(m):
    j = 1
    while True:
        x = d(j)                          # divisor count of T_j
        if x > m:
            return j * (j + 1) // 2        # return the triangular number
        j += 1

print(optimised_divisor_counter(500))  # Optimised solution
