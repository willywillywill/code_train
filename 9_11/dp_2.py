import pprint

n = 8

"""
dp = [ [0 for i in range(n)] for j in range(n) ]
dp[0] = [1]*n
for i in range(n):
    dp[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
"""


dp_ = [ 0 for i in range(n) ]
dp_[0] = 1
for i in range(n):
    for j in range(1,n):
        dp_[j] += dp_[j-1]

pprint.pprint(dp_)