
while 1:
    try:
        graph = {}
        val = {}
        vis = {}
        for i in range(int(input())):
            a,b,v = input().split()
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
            val[f"{a}-{b}"] = int(v)
            val[f"{b}-{a}"] = int(v)
            vis[a] = 0
            vis[b] = 0
        start, end = input().split()
        ans = {}
        qu = [(start,0)]
        while qu:
            qu.sort(key=lambda x:x[-1])
            root, v = qu.pop(0)
            if vis[root]:
                continue
            vis[root] = 1
            ans[root] = v
            
            for i in graph[root]:
                
                qu.append((i, v+val[f"{root}-{i}"]))

        if start in ans and end in ans:
            print(ans[end])
        else:
            print("NoRoute")
    except:
        break

"""
5
A B 7
B C 6
A C 5
B D 2
C D 3
A D
"""