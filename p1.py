"""

The function sum_of_multiples computes the sum of all natural numbers below a given limit n
that are divisible by 3 or 5. It does thus by iterating over 1 to n-1,
checking divisibility, collecting the relevant numbers in a list and then summing them.

Time complexity: O(n), as each number from 1 to n-1 is checked exactly once.

Space complexity: O(n), due to the storage of all valid multiples in a list.

"""




def sum_of_multiples(n):
    # Initialise an empty list to store multiples of 3 or 5
    multiples = []
    
    # Iterate through numbers from 1 to n-1
    for i in range(1, n):
        # Check if the number is divisible by 3 or 5
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)  # Add to the list if it is

    # Compute the sum of all collected multiples
    total = sum(multiples)

    return total  # Return the final total


print(sum_of_multiples(1000))


