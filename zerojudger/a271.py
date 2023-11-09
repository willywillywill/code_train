for _ in range(int(input())):

    x,y,z,w,n,m = list(map(int,input().split()))
    lst = list(map(int,input().split()))
    eat = [0,x,y,-z,-w]
    gg = 0
    for i in lst:

        m -= gg*n
        if m <= 0: break
        if i == 4: gg += 1
        m += eat[i]
        if m <= 0: break

    if m <= 0:
        print("bye~Rabbit")
    else:
        print("%dg"%(m))




"""
5 3 2 4 3 10
1 1 2 3 3 3 3 4 3 3
"""