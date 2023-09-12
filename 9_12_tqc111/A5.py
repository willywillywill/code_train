lst = list(map(int, input().split()))
dp = [ 1 for i in range(len(lst)) ]

for i in range(len(lst)):
    for j in range(i):
        if lst[i] > lst[j]:
            print(lst[j], end=" ")
            dp[i] = max(dp[i],dp[j]+1)
    print()
print(max(dp))

"""
1 3 5 4 10
1 8 3 7 2 9 6
1 4 2 4 2 3
"""