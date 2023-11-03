tree = {}
for i in input().split():
    a,b = i.split(",")
    a = int(a); b = int(b)
    if a not in tree:
        tree[a] = []
    if b not in tree:
        tree[b] = []
    tree[a].append(b)
    tree[b].append(a)
print(tree)
vis = [0]*10
def dfs(x,ptr):
    vis[x] += 1
    for i in tree[x]:
        if i != ptr and vis[i]<2:
            dfs(i,x)
dfs(0,0)
print(vis)

"""
1,2  2,0  5,2  5,3  6,4  5,6  6,8
T
1,0  4,3  1,2 
F
3,8  6,8  6,4  5,3  5,6  8,2  2,0
F

A,B,6 A,E,9 B,C,3 B,D,5 C,D,7 B,F,8 D,E,10 D,F,11 A,F,12 E,F,15
A,B B,C C,D 
1,2 2,3 3,4
"""
