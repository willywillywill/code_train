def dfs(root, l):
    if root in l:
        l.append(root)
        out[1].append(l)
        return
    k = 1
    l.append(root)
    for i in graph[root]:
        k = 0
        dfs(i,l.copy())
    if k:
        out[0].append(l)

graph = {}
for i in range(int(input())):
    n = input()
    if n[0] not in graph:
        graph[n[0]] = []
    if n[1] not in graph:
        graph[n[1]] = []
    graph[n[0]].append(n[1])

ans = 1e9
for root in graph:
    out = {1:[],0:[]}
    dfs(root,[])
    if out[1]:
        k = [ len(i)-1 for i in out[1]]
        ans = min(min(k), ans)
if ans == 1e9:
    print(0)
else:
    print(ans)
"""
8
AB
BC
CD
DE
AC
DA
EA
EF

7
AE
ED
DE
DA
DB
BA
MB
"""