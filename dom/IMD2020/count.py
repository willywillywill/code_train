def count(n,k):
    if n==0:
        return 0
    if k==0:
        return 1
    if dp[n][k] != -1:
        return dp[n][k]
    val = 0
    i = 0
    while i < n and k-i>=0:
        val += count(n-1, k-i)
        i+= 1
    dp[n][k] = val
    return dp[n][k]

n = int(input())
dp = [ [-1]*(n+1) for _ in range(n+1) ]

for _ in range(n):
    a,b = map(int,input().split())
    print(count(a,b))


"""
14
2 3
2 2
2 1
3 3
3 2
3 1
3 0
4 3
3 1
3 0
4 1
5 3
5 4
12 12
"""