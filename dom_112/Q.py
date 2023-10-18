n,q = list(map(int,input().split()))
lst = list(range(n))
for i in range(q):
    a1,a2 = list(map(int,input().split()))
    lst[a1-1],lst[a2-1] = lst[a2-1],lst[a1-1]
    ans=0

    for j in range(n):
        for k in range(j):
            if lst[j]<lst[k]:
                ans+=1
    print(ans)

