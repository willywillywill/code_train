maxn = 10**12
f = [0,1]*(maxn//2+1)
f[0] = 0
f[1] = 0
f[2] = 1
for i in range(3,int(maxn**0.5)+1,2):
    if f[i]==1:
        for j in range(i*i, maxn+1, i*2):
            f[j] = 0
from sys import stdin
for s in stdin:
    n = int(s)
    if n==0: break
    print(int(not f[n]))