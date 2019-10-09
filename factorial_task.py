def fac(n):
    test = 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
