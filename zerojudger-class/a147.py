while 1:
    n = int(input())
    if n == 0:
        break
    l = []
    for i in range(n):
        if (i>0) and (i%7!=0):
            l.append(i)
    print(*l)