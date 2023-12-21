
for _ in range(int(input())):
    lst = list(map(int,input().split()))[1:]
    ans = -1e9
    for i in range(len(lst)):
        k = 0
        for j in range(i,len(lst)):
            k += lst[j]
            ans = max(ans,k)
    print(ans)