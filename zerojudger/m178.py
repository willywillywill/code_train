def dfs(r,px,l):
    if r in l:
        return
    l.append(r)
    if r in dit:
        for i in dit[r]:
            if px != i and r in dit[i]:
                dfs(i,r,l)


while 1:
    try:
        n,m = map(int,input().split())
        dit = {}
        for _ in range(m): 
            i,j = map(int,input().split())
            if i not in dit:
                dit[i] = []
            if j not in dit:
                dit[j] = []
            dit[i].append(j)
        ans = set()
        for i in dit:
            vis = []
            dfs(i,i,vis)
            vis.sort()
            ans.add(tuple(vis))
        out = [ len(i) for i in ans ]
        out.sort()
        print(*out)
    except:
        break


"""
3 3
1 2
2 1
2 3

5 4
1 2
2 3
3 4
4 5

3 3
1 2
2 3
3 1
"""