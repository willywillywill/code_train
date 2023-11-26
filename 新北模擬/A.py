import itertools

for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    ans = []
    for i in range(1,n+1):
        it = list(itertools.combinations(lst, i))
        m = [0]*len(it)
        for j in range(len(it)):
            m[j] = abs(1000-sum(it[j]))
        ans.append(it[m.index(min(m))])
    m = [0]*len(ans)
    for i in range(len(ans)):
        m[i] = [abs(1000-sum(ans[i])), sum(ans[i])]
    m.sort(key=lambda x:(x[0],-x[1]))
    print(m[0][1])

"""
2
4
900 500 498 4
1
1
"""