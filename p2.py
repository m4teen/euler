"""

fib_sum_memo is a memoised, recursion-based algorithm.

"""

memo = {0:0, 1:1}

def f(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = f(n-1) + f(n-2)
        return memo[n]

def fib_sum_memo(m):
    even_fibs = []
    n = 0
    while f(n) <= m:
        if f(n) % 2 == 0:
            even_fibs.append(f(n))
        n += 1
    total_even_fibs = sum(even_fibs)

    return total_even_fibs


"""

fib_sum is a recursion-free algorithm

"""


def fib_sum(m):
    a, b = 0, 1
    total = 0
    while a <= m:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total
