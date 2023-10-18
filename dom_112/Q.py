n,q = list(map(int,input().split()))
lst = list(range(n))

a1,a2 = list(map(int,input().split()))
lst[a1-1],lst[a2-1] = lst[a2-1],lst[a1-1]
num = 0
ans = 0
for i in range(len(lst)):
    if lst[i] > num:
        num+=lst[i]
        ans+=1
print(ans)
"""
5 4
4 5
"""

