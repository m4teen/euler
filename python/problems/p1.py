"""""

Problem: 

1. Maths theory: dealing with natural numbers and multiples, thus there may be division involved

2. Examples of theory: find lcm, find gcd, find coprime pairs, sum multiples, find modulo p numbers 

3. We are essentially dividing the numbers in the list to check if we get a 0 residue in the mod 
operation 
for 3 or 5, which is fine. 

Caution 1: But we want to consider numbers strictly below n (off by one error)
Caution 2: Don't want to double add numbers divisible by both 3 and 5 (inclusion-exclusion)

"""""

def sum_of_multiples(n):
    multiples = []
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    total = sum(multiples)

    return total


print(sum_of_multiples(1000))

