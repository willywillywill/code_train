n = int(input())
lst = list(map(int,input().split()))
dp = [ [ int(i==0) for i in range(len(lst))] for j in range(len(lst)) ]
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(j//lst[i-1]):
            print(k)
            dp[i][j] += dp[i-1][j-k*lst[i-1]]

print(dp)

"""
4
4 2 2 5
"""