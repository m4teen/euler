

def symmetry_checker(n):
    n = str(n)
    return n == n[::-1]

def divisor_checker(x):
    for j in range(100,1000):
        if x % j ==0 and 100 <= x//j <= 999:
            return True
        else:
            continue
    return False

def palindrome_finder(m):
    current_max = 0
    for i in range(100,m):
        if symmetry_checker(i) == True and divisor_checker(i) == True:
            current_max = i       
    return current_max

print(palindrome_finder(1000000))


