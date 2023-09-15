# ??? TLE

"""
t = 1
while 1:
    x,y = list(map(int, input().split()))
    if x == -1 and y == -1:
        break
    m = [ [ 0 for j in range(y) ] for i in range(x) ]
    dp = [ [ 0 for j in range(y) ] for i in range(x) ]

    while 1:
        s1, s2 = list(map(int, input().split()))
        if s1==s2==0:
            break
        m[s1-1][s2-1] = 1

    n = 0
    for i in range(x):       # 計算球數
        for j in range(y):
            if 1 in m[i][j+1:] and 1 in [ m[ii][j] for ii in range(i+1,x) ]:
                n+=1
            if m[i][j] == 1:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print("CASE#%d:"%(t),dp[-1][-1],2**n)
    t += 1
"""

x,y = list(map(int, input().split()))

m = [ [ 0 for j in range(y) ] for i in range(x) ]
dp = [ [0 for j in range(2)] for i in range(y) ]
while 1:
    s1, s2 = list(map(int, input().split()))
    if s1==s2==0:
        break
    m[s1-1][s2-1] = 1
n = 0

for i in range(x):       # 計算球數
    for j in range(1,y):
        if m[i][j]:
            dp[j] += dp[j-1]+1
        else:
            dp[j] += dp[j-1]
    print(dp)
print(dp)        


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