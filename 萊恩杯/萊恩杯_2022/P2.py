def dfs(x,l):
    k = 1
    l.append(tree[x])
    if x*2<len(tree):
        k = 0
        dfs(x*2,l.copy())
    if x*2+1<len(tree):
        k = 0
        dfs(x*2+1,l.copy())
    if k:
        ans.append(l)

tree = [0]+input().split()
ans = []
dfs(1,[])
if len(ans)==1 and ans[0][0]=="x":
    print(0)
else:
    print(len(ans))

"""
3 3 x 4 2
3 1 4 3 x -1 5
"""