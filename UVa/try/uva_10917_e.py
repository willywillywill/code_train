def dfs(root,l,d):
    l.append(root)
    if 2 in l:
        ans.append([l.copy(),d])
        return
    for i in dit[root]:
        if i not in l:
            dfs(i,l.copy(),d+le["%d,%d"%(root,i)])

n,m = list(map(int,input().split()))
dit = {}
le = {}
for i in range(m):
    a,b,d = list(map(int,input().split()))
    if a not in dit:
        dit[a] = []
    if b not in dit:
        dit[b] = []
    dit[a].append(b)
    dit[b].append(a)
    le["%d,%d"%(a,b)] = d
    le["%d,%d"%(b,a)] = d

ans = []
dfs(1,[],0)
no,le = [ i[0] for i in ans ],[ i[1] for i in ans ]




print(no)
print(le)


"""
5 6
1 3 2
1 4 2
3 4 3
1 5 2
4 2 34
5 2 24
"""