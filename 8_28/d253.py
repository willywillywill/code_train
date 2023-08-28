num = 11
N = 7489
dp = [0]*(N+1)
c = [1,5,10,25,50]

def f():
    dp[0]=1
    for i in range(len(c)):
        for j in range(c[i], N+1):
            dp[j] += dp[j-c[i]]


f()
print(dp[2])
print(dp[1])