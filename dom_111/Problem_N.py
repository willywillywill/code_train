num = 11
cent = "20 40 32 67 40 20 89 300 404 13 13"

cent = list(map(int, cent.split()))
cent.sort()

def f(cent, n=0):
    if len(cent) == n:
        return cent
    elif cent[n] in cent[n+1:-1]:
        del cent[n]
        return f(cent,n+1)
    else:
        return f(cent,n+1)


cent = f(cent)
print(len(cent))
for i in cent:
    print(i, end=" ")