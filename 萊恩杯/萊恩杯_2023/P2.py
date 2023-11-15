lst = list(map(int,input().split()))
ans = 0
k = 0
for i in range(len(lst)):
    if i<k:
        continue

    for j in range(i+1,len(lst)):
        if lst[j]<=lst[i]:
            val = lst[j-1]-lst[i]
            p = lst[j-1],lst[i]
            k = j
            break
    else:
        val = lst[j]-lst[i]
        p = lst[j],lst[i]
        k = j

    ans += val
print(ans)
"""
300 300 500 0 0 300 100 400

1 2 3 1 2
"""