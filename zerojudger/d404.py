"""
Feldberg 5 5
1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9
"""


def f(i,j):
    if dp[i][j]:
        return dp[i][j]
    
    t = [0]*4
    for k,xxyy in enumerate(xy):
        x,y = xxyy
        nx = i+x
        ny = j+y
        if (0<= nx < xx) and (0<= ny < yy):
            if m[nx][ny] < m[i][j]:
                t[k] = f(nx,ny)

    dp[i][j] = 1+max(t)

    return dp[i][j]

for _ in range(int(input())):

    s = list(map(str, input().split()))
    name = s[0]
    xx = int(s[1])
    yy = int(s[2])
    xy = [(1,0),(0,1),(-1,0),(0,-1)]

    m = []
    for i in range(xx):
        l = list(map(int, input().split()))
        m.append(l)

    dp = [ [0 for j in range(yy)] for i in range(xx) ]

    ans=0
    for i in range(xx):
        for j in range(yy):
            ans = max(ans,f(i,j))
    print("%s:"%(name),ans)