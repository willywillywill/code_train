def dfs(root, l):
    k = 1
    l.append(root)
    for i in tree[root]:
        k = 0
        dfs(i,l.copy())
    if k:
        l = [ str(i) for i in l ]
        ans.append(l[1:][::-1])
for _ in range(int(input())):
    m = int(input())
    tree = { i:[] for i in range(m) }
    tree[99] = []
    for i in range(m):
        a,b = list(map(int,input().split(",")))
        tree[b].append(a)
    ans = []
    dfs(99,[])

    ans.sort(key=lambda x:int(x[0]))
    for i in range(len(ans)):
        if ans[i][1:-1]:
            print("%s:{%s}"%(ans[i][0], ",".join(ans[i][1:-1]) ))
        else:
            print("%s:N"%(ans[i][0]))



"""

7
0,99
1,3
2,3
3,5
4,6
5,0
6,5

4
0,99
1,0
2,0
3,0

1
0,99

"""