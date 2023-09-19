# ??? TLE
x,y = list(map(int, input().split()))
g = [[ 0 for i in range(y) ] for j in range(x)]
while 1:
    n,m = list(map(int, input().split()))
    if n==m==0:
        break
    g[n-1][m-1] = 1
print(g)


def dfs(n,m,k):
    h = k
    if 1 in g[n][m::]:
        if g[n][m]:
            h = max(h,k+1)
        else:
            dfs(n,m+1,h)
    if 1 in [ g[i][n] for i in range(len(g))]:
        if g[n][m]:
            h = max(h,k+1)
        else:
            dfs(n+1,m,h)
    return h

print(dfs(0,0,0))

"""
6 7
1 2
1 4
2 4
2 6
4 4
4 7
6 6
0 0

4 4
1 1
2 2
3 3
4 4
0 0
-1 -1
"""