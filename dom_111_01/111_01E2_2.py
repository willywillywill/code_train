import heapq
class node:
    def __init__(self,val):
        self.val = val
        self.vis = 0
class graph:
    def __init__(self,n,m):
        self.n = n
        self.m = m
        self.g = []
        self.v = []
        self.move_xy = [(0,-1),(-1,0),(1,0),(0,1)]
        for _ in range(n):
            self.g.append(list(map(int,input().split())))
            self.v.append([0]*m)
        self.heap_min = [[0,0,self.g[0][0]]]
        self.heap_xy = [[0,0]]
        
    def run(self, x,y):
        if (x==self.n-1 and y==self.m-1) or self.v[x][y]:
            return
        self.heap_min = heapq.nlargest(
            len(self.heap_min),
            self.heap_min,
            key=lambda x:-x[2]
                                       )
        hx,hy,hval = heapq.heappop(self.heap_min)
        self.v[x][y] = 1
        for mx,my in self.move_xy:
            nx = hx+mx
            ny = hy+my
            if 0 <= nx < self.n and 0 <= ny < self.m:
                if [nx,ny] in self.heap_xy:
                    pass
                        

                    



