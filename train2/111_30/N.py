input()
lst = list(map(int,input().split()))
dp = [1]*len(lst)
for i in range(len(lst)):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))

"""
3
2 2 2
"""