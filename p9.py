"""

The algorithm finds a Pythagorean triplet (a, b, c) such that a + b + c = n
It then returns the product abc of the first such triplet found whose sum is exactly n.

Time complexity: O(n^2) in the worst case due to the nested loops over a and b
Space complexity: O(1) if returning a single triplet (or O(k) if collecting k solutions)
"""

import math

# Check whether a triplet (a, b, c) satisfies the Pythagorean condition and a < b < c
def pythag_triplet(a, b, c):
    return a < b < c and a**2 + b**2 == c**2

# Generate all valid Pythagorean triplets such that a + b + c = n
def triplet_decoder(n):
    triplets = []
    # a must be less than n/3 because a < b < c and a + b + c = n
    for a in range(1, n // 3):
        # b must be less than (n - a)/2 because b < c
        for b in range(a + 1, (n - a) // 2):
            c = n - a - b  # derive c directly
            if pythag_triplet(a, b, c):  # check if this is a valid Pythagorean triplet
                triplets.append((a, b, c))  # store the triplet
    return triplets

# Find the first valid triplet whose sum is exactly n and return its product
def checker(n):
    # next() extracts the first triplet whose sum is exactly n
    triplet = next(x for x in triplet_decoder(n) if sum(x) == n)
    return math.prod(triplet)  # return a*b*c

# Compute the product of the triplet whose sum is 1000
print(checker(1000))  
