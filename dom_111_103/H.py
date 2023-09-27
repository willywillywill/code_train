while 1:
    m = list(map(str,input().split()))

    if m[0]=="0":
        break

    n,s = m[0],m[1]

    s = list(s)
    n = int(n)
    n = len(s)//n

    k = []
    g=""
    while s:
        g+=s.pop(0)
        if len(g) == n:
            k.append(g)
            g=""
    for i in k:
        print(i[::-1],end="")
    print()

