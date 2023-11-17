lst = { 1:1, 2:5, 3:8, 4:9, 5:10, 6:12, 7:17, 8:20, 9:24, 10:25 }

n = int(input())
dp = [0]*(n+1)
for i in lst:
    for j in range(i,n+1):
        dp[j] = max(dp[j], dp[j-i]+lst[i])
print(dp[-1])