"""

The function fib_sum_memo is a recursive, memoised solution to the problem of summing even Fibonacci
numbers up to a limit m. It implements memoisation to reduce recomputation
of the Fibonacci numbers, which achieves linear time in theory. However, it makes multiple
calls to f(n) in each loop iteration, leading to redundant lookups. The approach is
a brute-force one born out of trying to understand the problem.

Time complexity: Due to repeated f(n) calls per iteration, runtime is around O(n log n)).

Space complexity: O(n), due to the memo dictionary storing all Fibonacci numbers up to f(n).

"""

# Initialise a memoisation dictionary with base Fibonacci values
memo = {0: 0, 1: 1}

def f(n):
    # If Fibonacci value already computed, return it
    if n in memo:
        return memo[n]
    else:
        # Otherwise, compute recursively, store in memo, and return
        memo[n] = f(n - 1) + f(n - 2)
        return memo[n]

def fib_sum_memo(m):
    # List to store even Fibonacci numbers up to m
    even_fibs = []
    n = 0
    # Loop until the nth Fibonacci number exceeds m
    while f(n) <= m:
        # If the Fibonacci number is even, store it
        if f(n) % 2 == 0:
            even_fibs.append(f(n))
        n += 1
    # Sum all even Fibonacci numbers collected
    total_even_fibs = sum(even_fibs)

    return total_even_fibs

"""

The function fib_sum is an iterative, recursion-free solution that uses constant space and runs in linear time.
It avoids memoisation, lists, and recursion entirely, making it well-suited
to large inputs. It is less easy to visualise but far superior
in performance and memory efficiency to fib_sum_memo.

Time complexity: O(n), where n is the number of Fibonacci numbers <= m.

Space complexity: O(1), since it always uses a fixed number of variables

"""


def fib_sum(m):
    a, b = 0, 1         # Initialise first two Fibonacci numbers
    total = 0           # Running total of even Fibonacci numbers

    # Loop until the current Fibonacci number exceeds m
    while a <= m:
        if a % 2 == 0:
            total += a  # Add to total if the Fibonacci number is even
        a, b = b, a + b # Generate the next Fibonacci number

    return total        # Return the sum of even Fibonacci numbers <= m


