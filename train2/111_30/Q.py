def dfs(x,px):
    data[x]["parent"] = px
    data[x]["degree"] = len(tree[x])+(0 if x==0 else -1)
    data[x]["depth"] = data[px]["depth"]+1
    data[x]["height"] = 0
    for i in tree[x]:
        if px != i:
            data[x]["height"] = max(dfs(i, x)+1,data[x]["height"])
    return data[x]["height"]


n = int(input())
tree = { i:[] for i in range(n)}
info = { "parent":0, "degree":0, "depth":-1, "height":0 }
data = [info.copy() for _ in range(n)]
for __ in range(n):
    _,a,b = map(int,input().split())
    if a != -1:
        tree[_].append(a)
        tree[a].append(_)
    if b != -1:
        tree[_].append(b)
        tree[b].append(_)
dfs(0,-1)
for i in data:
    print(i)


"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""