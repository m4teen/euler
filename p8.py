import math  # Import the math module to access math.prod

# Long string of digits taken from Project Euler Problem 8
number_string = ("73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450")


# Preprocess: Convert the string to a list of integers, avoiding repeated casting in the loop
number = [int(number_string[i]) for i in range(len(number_string))]

"""

trawler solves the problem of finding the largest product of n adjacent digits
in a long digit string. The first implementation computed the product in each iteration
by converting each character to an integer inside the loop. This was optimised by converting
the entire digit string into a list of integers before entering the loop, 
thus removing the need to type cast into int() at each step of the loop. This resulted in 
a 53% improvement in speed:

Old version: 
Time taken: 0.002019 seconds

Optimised version:
Time taken: 0.000946 seconds

Time complexity:
O(k * n), where k is the total number of digits and n is the window size. In the worst possible 
scenario, trawler will compute a product of n digits for each of (k - n) positions.

Space complexity:
O(k), where k is the number of digits stored in the preprocessed list.

"""


def trawler(n):
    biggest = 0  # Variable to store the maximum product found
    for i in range(0, int(len(number) - n)):  # Slide a window of size n across the number list
        product = math.prod([number[x] for x in range(i, i + n)])  # Compute product of n digits
        if product > biggest:
            biggest = product  # Update max if new product is bigger
        else:
            continue  # Otherwise, keep going
    return biggest

print(trawler(13))  # Find and print the maximum product of 13 adjacent digits
