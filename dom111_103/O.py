# Coin Change Problem

m = list(map(int,input().split()))[1]
c = list(map(int,input().split()))

dp = [ 0 for i in range(m+1) ]
dp[0] = 1
for i in range(len(c)):
    for j in range(c[i], m+1):
        dp[j] += dp[j-c[i]]
dp[0] = 0
print(dp[m])

"""
3 6
2 3 5
"""