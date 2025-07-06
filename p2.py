def f(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    elif n > 1:
        return f(n-1)+f(n-2)
    else:
        print('Negative numbers are forbidden.')

def fib_summer(m):
    fibs = []
    even_fibs = []
    n = 0
    while f(n) <= m:
        fibs.append(f(n))
        n += 1

    for i in fibs:
        if i % 2 == 0:
            even_fibs.append(i)

    total_even_fibs = sum(even_fibs)

    return total_even_fibs


print(fib_summer(4000000))