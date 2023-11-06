n = int(input())
ans = []
for i in range(1,n):
    k = []
    for j in range(i,n):
        k.append(j)
        if sum(k)>n:
            break
        elif sum(k)==n:
            ans.append(k.copy())
if ans:
    print(",".join([str(i[0])+"~"+str(i[-1]) for i in ans ]))
else:
    print(-1)