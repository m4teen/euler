def f(n):
    x = 2**n 
    x = str(x)
    x = list(x)
    x = [int(v) for v in x]
    x = sum(x)

    return x

print(f(1000))