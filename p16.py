def f(n):
    """
    Compute the sum of the digits of a power of two.

    Given an exponent n, compute 2**n, then sum all the decimal digits of that result.

    Example:
        For n = 15: 2**15 = 32768 → digit sum = 3 + 2 + 7 + 6 + 8 = 26

    Parameters:
        n (int): non-negative integer exponent

    Returns:
        int: sum of decimal digits of 2 to the power n

    Problem:
        What is the sum of the digits of the number 2**1000?
    """

    x = 2**n 
    x = str(x)
    x = list(x)
    x = [int(v) for v in x]
    x = sum(x)

    return x

print(f(1000))