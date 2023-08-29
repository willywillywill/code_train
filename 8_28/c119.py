size = 1000
dp = [0]*(size+1)
dp[0] = 1

t = 1
for i in range(1,size+1):
    t *= i
    s = str(t)
    for j in s:
        dp[i]+=int(j)


while 1:
    try:
        print(dp[int(input())])
    except:
        break

