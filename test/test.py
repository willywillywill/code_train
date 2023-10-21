import heapq

class node:
    def __init__(self,val,x,y):
        self.val = val
        self.x = x
        self.y = y
    def __lt__(self, other): 
        return self.val < other.val


for _ in range(int(input())):
    n = int(input())
    m = int(input())
    graph = []
    visited = []
    for i in range(n):
        visited.append([0]*m)
        visited.append([0]*m)
        graph.append(list(map(int,input().split())))
    mxy = [(0,-1),(-1,0),(1,0),(0,1)]
    heap = [node(graph[0][0],0,0)]
    while heap:
        hnode = heapq.heappop(heap)
        hval,hx,hy = hnode.val,hnode.x,hnode.y
        if visited[hx][hy]:
            continue
        if hx==n-1 and hy==m-1:
            break
        visited[hx][hy]=1
        for mx,my in mxy:
            if 0<=hx+mx<n and 0<=hy+my<m:
                l = [ [i.x,i.y] for i in heap ]  # <--- 
                if [hx+mx,hy+my] in l:
                    idx = l.index([hx+mx,hy+my])
                    heap[idx].val = min(heap[idx].val,hval+graph[hx+mx][hy+my])
                else:
                    heapq.heappush(heap,node(hval+graph[hx+mx][hy+my],hx+mx,hy+my))
    print(hval)