cnt = 1
while 1:
    z,i,m,l = list(map(int, input().split()))
    if z==0 and i==0 and m==0 and l==0:
        break
    u = [l]
    while True:
        n_L = (z*l+i)%m
        if n_L in u:
            idx=u.index(n_L)
            break
        l = n_L
    print(len(u[idx:]))
