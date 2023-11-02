n,k = list(map(int,input().split()))
lst = list(map(int,input().split()))

d,p = [0]*(k+1),[0]*(k+1)
imax = 0
for v in lst:
    p[0] = max(d[0],0)+v
    for j in range(1,k+1):
        p[j] = max(d[j-1],d[j]+v)
    d,p = p,d
    imax = max(imax,d[k])
print(imax)


"""
9 2
3 1 -2 3 -2 3 -5 2 2
"""