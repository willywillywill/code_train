def dfs(i):
    if i in dit:
        for j in range(1,n):
            if j in dit[i]:
                val[j] = val[i]+1
                dfs(j)

for _ in range(int(input())):
    if _>0:
        input()
    n = int(input())
    dit = {}
    for _ in range(n-1):
        a,b = map(int, input().split(","))
        if b not in dit:
            dit[b] = [a]
        else:
            dit[b].append(a)
    val = [1 for i in range(n)]
    dfs(0)
    print(max(val))
"""

def dfs(x):
    for i in range(n):
        if lst[i][x]:
            d[i] = d[x]+1
            dfs(i)
for _ in range(int(input())):
    if _>0:
        input()
    n = int(input())
    lst = [[ 0 for j in range(n) ] for i in range(n)]
    for i in range(n-1):
        m = list(map(int, input().split(',')))
        lst[m[0]][m[1]] = 1
    d = [ 1 for i in range(n) ]
    dfs(0)
    print(max(d))
"""

"""
3
4
1,2
2,3
3,0

4
1,0
2,0
3,0

2
1,0

2
7
1,3
2,3
3,5
4,5
5,0
6,5

8
1,6
2,3
3,4
4,6
5,6
6,0
7,2
"""