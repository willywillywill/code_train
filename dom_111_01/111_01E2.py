import heapq

for _ in range(int(input())):
    n = int(input())
    m = int(input())
    graph = []
    visited = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        graph.append(list(map(int,input().split())))
    mxy = [(0,-1),(-1,0),(1,0),(0,1)]
    heap = []
    heapq.heappush(heap,(0,0,graph[0][0]))
    while heap:
        heap = heapq.nlargest(len(heap),heap,key=lambda x:-x[2])
        lx,ly,lval = heapq.heappop(heap)
        if lx==n-1 and ly==m-1:
            break
        visited[lx][ly]=1
        for mx,my in mxy:
            if 0<=lx+mx<n and 0<=ly+my<m:
                if visited[lx+mx][ly+my] == 0:
                    l = [ [i[0],i[1]] for i in heap ]
                    if [lx+mx,ly+my] in l:
                        idx = l.index([lx+mx,ly+my])
                        heap[idx][2] = min(heap[idx][2],lval+graph[lx+mx][ly+my])
                    else:
                        heapq.heappush(heap,[lx+mx,ly+my,lval+graph[lx+mx][ly+my]])
    print(lval)


"""
2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5
"""
            