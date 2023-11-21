def dfs(x,vis):
    if vis[x] == 2:
        return
    vis[x] += 1
    for i in graph[x]:
        dfs(i, vis)
while 1:
    n = int(input())
    if n==0:
        break
    lst = list(map(int,input().split()))
    lst = [ lst[i:i+2] for i in range(0,len(lst),2) ]
    graph = {}
    ptr = {}
    for i in lst:
        if i[0] not in graph:
            graph[i[0]] = []
        if i[1] not in graph:
            graph[i[1]] = []
        if i[0] not in ptr:
            ptr[i[0]] = []
        if i[1] not in ptr:
            ptr[i[1]] = []
        ptr[i[1]].append(i[0])
        graph[i[0]].append(i[1])

    if len(graph)-1==len(lst):
        for i in ptr:
            if len(ptr[i]) == 0:
                vis = { i:0 for i in graph }
                dfs(i,vis)
                if 0 in vis.values():
                    print("n")
                elif 2 in vis.values():
                    print("n")
                else:
                    print("y")  
                break      
        else:
            print("n")
    else:
        print("n")