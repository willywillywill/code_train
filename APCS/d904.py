mone,n = map(int,input().split())
co = []
for _ in range(int(n)):
    co.append(int(input()))
dp = [1e9]*(mone+1)
dp[0] = 0
for i in co:
    for j in range(i,mone+1):
        dp[j] = min(dp[j], dp[j-i]+1)
    print(dp)
print(dp[-1])

"""
93 5
25
50
10
1
5

16 2
1
5
"""