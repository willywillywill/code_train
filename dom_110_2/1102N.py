in1 = input()
in2 = input()
dp = [ [ 0 for i in range(len(in2)+1) ] for j in range(len(in1)+1)  ]
dp [0] = [ i for i in range(len(in2)+1) ]

for i in range(len(in1)+1):
    dp[i][0] = i

for i in range(1, len(in1)+1):
    for j in range(1, len(in2)+1):
        if in1[i-1]==in2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
print(dp[-1][-1]) 