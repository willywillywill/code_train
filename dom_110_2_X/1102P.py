n = int(input())
lst = [0]+list(map(int,input().split()))
dp = [ [ -1 for i in range(n)] for j in range(n) ]

for i in range(n):
    for j in range(n):
        if i!=j:
            dp[i][j] = lst[i] + lst[j]
print(dp)
print(dp[-1][-1])

"""
4
4 2 2 5
"""