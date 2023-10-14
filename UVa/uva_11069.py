# ! like Fib
""" DP buttom-up
n = 40
dp = [ 0 for i in range(n) ]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3,n):
    dp[i][0] = dp[i-2][0] + dp[i-3][0]
"""
""" DP top-down
n = 77
dp = [ [0,0] for i in range(n) ]

def f(n):
    if dp[n][1]:
        return dp[n][0]
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    dp[n][0] = f(n-2) + f(n-3)
    dp[n][1] = 1
    return dp[n][0]

while 1:
    try:
        print(f(int(input())))
    except:
        break
"""
