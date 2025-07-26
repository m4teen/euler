import math

def pythag_triplet(a, b, c):
    return a < b < c and a**2 + b**2 == c**2

def triplet_decoder(n):
    triplets = []
    for i,j,k in range(n-1,n-2,n):
        if pythag_triplet(i,j,k):
            triplets.append((i,j,k))
        else:
            continue
    return triplets

def triplet_decoder(n):
    triplets = []
    for a in range(1, n//3):
        for b in range(a + 1, (n - a)//2):
            c = n - a - b
            if pythag_triplet(a, b, c):
                triplets.append((a, b, c))
    return triplets

def checker(n):
    triplet = next(x for x in triplet_decoder(n) if sum(x) == n)
    return math.prod(triplet)  

print(checker(1000)) 
