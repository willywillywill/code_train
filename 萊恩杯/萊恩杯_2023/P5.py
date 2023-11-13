from itertools import combinations
n,m = map(int,input().split())
m = list(range(1,n+1))

for i in m:
    l = list(combinations(m,i))
    print(l)