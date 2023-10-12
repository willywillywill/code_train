for _ in range(int(input())):
    x = int(input())
    y = int(input())
    graph_val = []
    graph_cost = [[ 0 for i in range(y)] for j in range(x)]
    graph_visited = [[ 0 for i in range(y)] for j in range(x)]
    for i in range(x):
        data = list(map(int, input().split()))
        graph_val.append(data)
    queue = [(0,0)]
    while queue:
        qx,qy = queue.pop(0)
        if graph_visited[qx][qy]==0:
            graph_visited[qx][qy]=1
            gx = 9999999 if qx-1<0 else graph_cost[qx-1][qy]
            gy = 9999999 if qy-1<0 else graph_cost[qx][qy-1]
            if not (gx==gy==9999999):
                graph_cost[qx][qy] = min(gx,gy)+graph_val[qx][qy]
            else:
                graph_cost[qx][qy] = graph_val[qx][qy]
            if qx+1 < x:
                queue.append([qx+1,qy])
            if qy+1 < y:
                queue.append([qx,qy+1])
    print(graph_cost[-1][-1])
