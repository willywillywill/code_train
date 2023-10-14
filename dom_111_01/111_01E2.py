

n = int(input())
m = int(input())
g = []
mxy = [(0,1),(1,0),(0,-1),(-1,0)]
for i in range(n):
    g.append(list(map(int,input().split())))
queue = [(0,0)]
visited = [[ 0 for j in range(m) ] for i in range(n)]
val = [[ 0 for j in range(m) ] for i in range(n)]

while queue:
    qx,qy = queue.pop(0)
    if visited[qx][qy]:
        continue
    visited[qx][qy] = 1
    v = [ [g[qx+i[0]][qy+i[1]],i[0],i[1]] for i in mxy if (0<=i[0]<n and 0<=i[1]<m) ]
    v.sort(key=lambda x:x[0])
    print(v)



print(val)


"""
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
5
6
0 9 9 0 0 0
0 9 0 0 9 0
0 9 0 9 9 0
0 0 0 9 9 0
9 9 9 9 9 0
"""
            