
"""
Feldberg 10 5
56 14 51 58 88
26 94 24 39 41
24 16 8 51 51
76 72 77 43 10
38 50 59 84 81
5 23 37 71 77
96 10 93 53 82
94 15 96 69 9
74 0 62 38 96
37 54 55 82 38
"""
# DP
def f(i,j):
    if dp[i][j]:
        return dp[i][j]
    
    t = [0]*4
    for k,xxyy in enumerate(xy):  # compute top down left right
        x,y = xxyy
        nx, ny = i+x, j+y
        if (0<= nx < xx) and (0<= ny < yy): # is index array
            if m[nx][ny] < m[i][j]: 
                t[k] = f(nx,ny)     #  if new spot is min then go to new spot
                                    #  else not go to new spot and 
                                    #       if t(time) in the end then t=0 so return 0 
                                    #       then up layer 0+1 ...

    dp[i][j] = 1+max(t)   # update dp array

    return dp[i][j]


s = list(map(str, input().split()))
name = s[0]
xx = int(s[1])
yy = int(s[2])

xy = [(1,0),(0,1),(-1,0),(0,-1)]
m = []

for i in range(xx):
    m.append(list(map(int, input().split())))

dp = [ [0 for j in range(yy)] for i in range(xx) ]
ans=0
for i in range(xx): # scan the array
    for j in range(yy):
        ans = max(ans,f(i,j))

print("%s:"%(name),ans)