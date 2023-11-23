import copy

def bfs(x):
    gg = copy.deepcopy(g)
    del gg[x]
    for i in gg:
        if x in gg[i]:
            del gg[i][gg[i].index(x)]
    
    qu = [ g[x][0] ]
    vis = { i:0 for i in gg }
    while qu:
        root = qu.pop(0)
        if vis[root]:
            continue
        vis[root] += 1
        for i in gg[root]:
            qu.append(i)
    return vis

while 1:
    n = int(input())
    if n==0:
        break
    g = { i:[] for i in range(1,n+1) }
    nodes = set()
    for _ in range(n+1):
        l = list(map(int,input().split()))
        if l == [0]:
            break
        for i in l:
            nodes.add(i)
        for i in l[1:]:
            if i not in g[l[0]]:
                g[l[0]].append(i)
            if l[0] not in g[i]:
                g[i].append(l[0])
    ans = []
    for i in nodes:
        if 0 in bfs(i).values():
            ans.append(str(i))
    print("ans"," ".join(ans))

"""
13 
1 3 6 13 
2 6 9 10 13 
3 4 5 13 
4 5 7 12 
5 6 11 13 
6 9 
8 11 
9 10 
11 13 
12 13 
0 
20 
1 7 14 15 
2 8 11 15 
3 9 14 16 19 
4 8 
5 14 
6 7 11 15 18 
7 13 15 17 
8 16 19 
9 11 14 16 
10 12 16 19 20 
12 20 
14 19 
15 18 19 
18 19 
0 
0
"""