n, m = list(map(int, input().split()))

if m > n:
    print(m-n)
else:
    k = 200-n
    k+= m
    print(k)
