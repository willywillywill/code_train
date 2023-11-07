"""
測資大 -> killed
"""

def f(n,weight):
    if weight<0:
        return -1e9
    if n==0:
        return 0
    if dp[weight]:
        return dp[weight]
    dp[weight] = max(
        f(n-1, weight-w[n]) + v[n],
        f(n-1, weight)
    )
    return dp[weight]

n,max_weight = list(map(int,input().split()))
w = [0]+list(map(int,input().split()))
v = [0]+list(map(int,input().split()))
dp = [0]*(max_weight+1)
f(n,max_weight)
print(max(dp))