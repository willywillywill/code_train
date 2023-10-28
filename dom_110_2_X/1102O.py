in1 = "0"+input()
in2 = "0"+input()
in3 = "0"+input()

dp = [[[0 for i in range(len(in3))] for j in range(len(in2))] for i in range(len(in1))]

for i in range(1, len(in1)):
    for j in range(1, len(in2)):
        for k in range(1, len(in3)):
            if in1[i]==in2[j] and in2[j]==in3[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1]+1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
print(dp[-1][-1][-1])

"""
abcdbceea
cabdefga
dcea

abe
acb
babcd
"""