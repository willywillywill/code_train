import pprint

x,y = list(map(int, input().split()))
m = [ [ 0 for j in range(y) ] for i in range(x) ]
dp = [ [ 0 for j in range(y) ] for i in range(x) ]

while 1:
    s1, s2 = list(map(int, input().split()))
    if s1==s2==0:
        break
    m[s1-1][s2-1] = 1

for i in range(x):   
    for j in range(y):
        if m[i][j] == 1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

pprint.pprint(dp)


# Q2 ??

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
"""