# 硬幣 -> 背包
n,x = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0]*(x+1)
dp[0] = 1
for i in range(n):
    for j in range(lst[i], x+1):
        dp[j] += dp[j-lst[i]]
print(dp)


"""
3 9
2 3 5

3 10
2 3 5
"""