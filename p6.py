"""
This script computes the difference between the square of the sum and 
the sum of the squares for the first n natural numbers. 

The function sum_of_squares uses the mathematical formula for the finite sum of squares, which can easily be proven 
by induction, is used. This greatly simplifies the sum_of_squares which 
is the trickier of the two functions to define. An alternative implementation 
which does not rely on mathematical elegance is included as sum_of_squares-alt using a list 
comprehension and manual summation, though it is much less efficient.

Time complexity (using sum_of_squares): O(n) due to sum(range(...)) in square_of_sum.
Time complexity (using sum_of_squares_alt): O(n) due to explicit iteration and squaring.

Space complexity (using sum_of_squares): O(1) as no data structures are created or stored whose 
size scales with n.
Space complexity (using sum_of_squares_alt): O(n) due to list of squares created in memory.

"""




def sum_of_squares(n):
    # Uses the closed-form formula for sum of squares: 1^2 + 2^2 + ... + n^2
    return 1/6 * n * (n + 1) * (2 * n + 1)

def sum_of_squares_alt(n):
    # Computes sum of squares manually using a list comprehension and sum()
    # Equivalent to: 1^2 + 2^2 + ... + n^2 without using a closed-form formula
    return sum([i ** 2 for i in range(1, n + 1)])

def square_of_sum(n):
    # Computes the square of the sum: (1 + 2 + ... + n)^2
    x = sum(range(1, n + 1))  # sum of first n natural numbers
    return x ** 2  # square of the sum

def difference(n):
    # Returns the difference between square of sum and sum of squares
    return int(square_of_sum(n) - sum_of_squares(n))

# Prints the result for n = 100
print(difference(100))

