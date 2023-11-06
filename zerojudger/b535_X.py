
def dfs(x,ptr,vis):
    vis[x] += 1
    for i in tree[x]:
        if i!=ptr and vis[i]<2:   
            dfs(i,x,vis)
flag = True
trees = []
for i in range(int(input())):
    tree = {}
    vis = {}
    lst = [ list(map(int,i.split("-"))) for i in input().split()]
    for a,b in lst:
        if a not in tree:
            tree[a] = []
        if b not in tree:
            tree[b] = []
        tree[a].append(b); tree[b].append(a)
        vis[a] = 0;        vis[b] = 0
    dfs(1,1,vis)
    flag = 2 in list(vis.values()) or 0 in list(vis.values())

"""
2
1-5 2-3 2-4 4-5 4-6
1-3 1-4 1-6 2-6 3-5
"""