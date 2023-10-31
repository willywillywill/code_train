def dfs(x,px):
    global ans
    h1 = 0
    h2 = 0
    for i in dit[x]:
        if i != px:
            h = dfs(i,x)+1
            if h>h1:
                h2 = h1
                h1 = h
            elif h>h2:
                h2 = h
    ans = max(ans,h1+h2)
    return h1

while 1:
    try:
        ans = 0
        dit = {}
        nodes = set()
        for i in range(int(input())-1):
            a,b = list(map(int,input().split()))
            if a not in dit:
                dit[a] = []
            if b not in dit:
                dit[b] = []
            dit[a].append(b)
            dit[b].append(a)
            nodes.add(a)
            nodes.add(b)
        nodes = list(nodes)
        dfs(nodes[0],nodes[0])
        print(ans)
    except:
        break

"""
8
0 1
0 2
0 3
7 0
1 4
1 5
3 6
4
0 1
0 2
2 3
"""