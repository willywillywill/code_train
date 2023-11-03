def dfs(x,l):
    if x in l:
        return
    l.append(x)
    if x == end:
        max_val = 0
        for i in range(1,len(l)):
            max_val = max(val["%d,%d"%(l[i-1],l[i])], max_val)
        ans.append(max_val)
        return
    for i in graph[x]:
        dfs(i,l.copy())
t = 1
while 1:
    c,s,q = list(map(int,input().split()))
    if c==s==q==0:
        break
    graph = {}
    val = {}
    a2b = []
    for _ in range(s):
        a,b,cnt = list(map(int,input().split()))
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
        val["%s,%s"%(a,b)] = cnt
        val["%s,%s"%(b,a)] = cnt
    print("Case #%d"%(t))
    t+=1
    for _ in range(q):
        a,b = list(map(int,input().split()))
        ans = []
        start = a
        end = b
        dfs(start,[])
        if ans:
            print(min(ans))
        else:
            print("no path")

"""
7 9 3
1 2 50
1 3 60
2 4 120
2 5 90
3 6 50
4 6 80
4 7 70
5 7 40
6 7 140
1 7
2 6
6 2
"""