"""

The function smallest_multiple calculates the smallest positive number that is evenly divisible.
by all integers from 1 to n using the least common multiple (LCM) of the range.

Time complexity: O(n (log n) * log (log n)) due to repeated LCM via prime factorisation internally.
Space complexity: O(1) since no additional space used beyond constant-size variables.

"""


import math

def smallest_multiple(n):
    # Create a range of numbers from 1 to n inclusive
    numbers = range(1, n + 1)
    
    # Compute the least common multiple (LCM) of all numbers in the range
    d = math.lcm(*numbers)
    
    # Return the result
    return d

# Print the smallest number divisible by all integers from 1 to 20
print(smallest_multiple(20))