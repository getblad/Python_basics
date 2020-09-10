def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        yield result



n = 4
for el in fac(n):
    print(el)