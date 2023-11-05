def dfs(root, l):
    k = 1
    l.append(root)
    for i in tree[root]:
        k = 0
        dfs(i,l.copy())
    if k:
        l = [ str(i) for i in l ]
        ans.append(l[1:][::-1])

m = int(input())
tree = { i:[] for i in range(m) }
tree[99] = []
for i in range(m):
    a,b = list(map(int,input().split(",")))
    tree[b].append(a)
ans = []
dfs(99,[])
print(ans)

for i in range(len(ans)):
    if len(ans[i]) <= 2:
        print("%s:N"%(ans[i][0]))
    else:
        print("%s:{%s}"%(ans[i][0],",".join(ans[i][1:-1])))



"""
7
0,99
1,3
2,3
3,5
4,6
5,0
6,5
"""