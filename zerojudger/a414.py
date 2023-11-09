import sys

for i in sys.stdin:
    n = int(i)
    if n==0:
        break

    b = bin(n)
    x = len(b)
    y = len(b.rstrip("1"))
    print(x-y)  # new(n)-old(n+1)


