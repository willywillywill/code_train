num = 5

dp = [[0 for j in range(76)] for i in range(76)]

for i in range(num):
    for j in range(num):
        if j+2 <= num:
            dp[i][j] += 1
        if j+3 <= num:
            dp[i][j] += 1
        