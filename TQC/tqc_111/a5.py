in1 = list(map(int,input().split()))
dp = [1 for i in range(len(in1))]

for i in range(len(in1)):
    for j in range(i):
        if in1[i] > in1[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(dp)

"""
1 3 5 4 10
1 8 3 7 2 9 6
"""