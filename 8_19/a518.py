# OK

while 1:
    a1, a2 = list(map(int, input().split()))
    if a1==-1 and a2==-1:
        break

    if a2 > a1:
        a1, a2 = a2, a1

    n1 = 0
    n1 += 100-a1
    n1 += a2

    n2 = a1-a2

    print(min(n1,n2))

