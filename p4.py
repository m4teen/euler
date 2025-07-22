def symmetry_checker(n):
    # Convert number to string and compare with its reverse
    n = str(n)
    return n == n[::-1]

def divisor_checker(x):
    # Check if x is a product of two 3-digit numbers
    for j in range(100, 1000):
        if x % j == 0 and 100 <= x // j <= 999:
            return True  # Found valid 3-digit divisor pair
        else:
            continue
    return False  # No valid 3-digit factors found

def palindrome_finder(m):
    # Initialise variable to store the largest valid palindrome found
    current_max = 0

    # Iterate through all numbers from 100 up to m
    for i in range(100, m):
        # Check if the number is a palindrome and has two 3-digit factors
        if symmetry_checker(i) == True and divisor_checker(i) == True:
            current_max = i  # Update current max palindrome
    return current_max  # Return the largest valid palindrome found

print(palindrome_finder(1000000))

"""

This algorithm finds the largest palindrome less than a given upper bound m
that is simultaneously a product of two 3-digit numbers. It does this by checking each number
in the range [100, m) to see if its palindromic and if it can be factored into
two 3-digit integers.

Time complexity: O(n * k), where n is the length of [100, m) and 
k = 900 is the number of 3-digit divisors checked for each candidate.

Space complexity: O(1), as only scalar values are being used for tracking the result.

"""
