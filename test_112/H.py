def f(u):
    global ans
    if u==n:
        return
    if lst[u-1] > lst[u]:
        ans+=1
        lst[u-1],lst[u] = lst[u],lst[u-1]
    f(u+1)

for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        f(1)
    print("Optimal train swapping takes %d swaps."%(ans))

"""
3
3
1 3 2
4
4 3 2 1
2
2 1
"""