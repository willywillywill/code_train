def fun(n):
    print(n)
    if n>100:
        return n-5
    return fun(fun(n+11))

print(fun(40))
