
N = 7489
dp = [0]*(N+1)
c = [1,5,10,25,50]

dp[0]=1
for i in range(len(c)):
    for j in range(c[i], N+1):
        dp[j] += dp[j-c[i]]

while 1:
    try:
        n = int(input())
        print(dp[n])
    except:
        break