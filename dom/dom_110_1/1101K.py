
for _ in range(int(input())):
    s1 = "0"+input()
    s2 = "0"+input()

    dp = [[ 0 for i in range(len(s2))]
        for j in range(len(s1))]

    for i in range(1,len(s1)):
        for j in range(1,len(s2)):
            if s1[i]==s2[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    print(dp[-1][-1])

"""
ACCGATGCAGCGCTC
CCGATGA
"""