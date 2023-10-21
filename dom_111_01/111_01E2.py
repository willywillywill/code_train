import heapq

for _ in range(int(input())):
    n = int(input())
    m = int(input())
    graph = []

    for i in range(n):
        l = list(map(int,input().split()))
        graph.append(l)
        
    visited = [[False for i in range(m)] for i in range(n)]
    mxy = [(1,0),(0,1),(0,-1),(-1,0)]
    heap = [(graph[0][0],0,0)]
    visited[0][0] = 1
    while heap:
        hnode = heapq.heappop(heap)
        val = hnode[0]
        x = hnode[1]
        y = hnode[2]
        for mx,my in mxy:
            nx = mx+x
            ny = my+y
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or visited[nx][ny]:
                continue
            graph[nx][ny] = val+graph[nx][ny]
            visited[nx][ny] = True
            heapq.heappush(heap, (graph[nx][ny],nx,ny))
    print(graph[-1][-1])

""" 
3
1
1
9
2
2
0 0
0 0
5
6
0 9 9 0 0 0
0 9 0 0 9 0
0 9 0 9 9 0
0 0 0 9 9 0
9 9 9 9 9 0

"""