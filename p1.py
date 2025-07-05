def sum_of_multiples(n):
    multiples = []
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    total = sum(multiples)

    return total


print(sum_of_multiples(1000))

