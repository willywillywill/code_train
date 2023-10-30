
n = int(input())
lst = list(map(int,input().split()))
ans = 0
for i in range(len(lst)):
    for j in range(i):
        if lst[i]<lst[j]:
            ans += 1
print(ans)

"""
1 20 54 1 50 100 2000 50
"""