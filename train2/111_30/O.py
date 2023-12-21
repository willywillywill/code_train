
n, m = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0]*(m+1)
dp[0] = 1
for i in lst:
    for j in range(i, m+1):
        dp[j] += dp[j-i]
print(dp)

"""
3 10
2 3 5
"""