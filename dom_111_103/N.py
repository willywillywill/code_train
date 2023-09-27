# LIS-dp https://web.ntnu.edu.tw/~algo/Subsequence.html

_ = int(input())
lst = list(map(int, input().split()))
n = len(lst)
length = [ 1 for i in range(n) ] #dp

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            length[i] = max(length[i], length[j]+1)

print(max(length))

"""
20 40 32 67 40 20 89 300 404 13 13
lst = list(map(int, input().split()))
dp = [ 1 for i in range(len(lst)) ]

for i in range(len(lst)):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
"""