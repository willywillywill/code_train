

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
    visited[qx][qy] = 1
    min_val = 9999
    for mx,my in mxy:
        if 0 <= qx+mx < n:
            if visited[qx+mx][qy] == 0:
                queue.append((qx+mx,qy))
            min_val = min(g[qx+mx][qy],min_val)
        if 0 <= qy+my < m:
            if visited[qx][qy+my] == 0:
                queue.append((qx,qy+my))
            min_val = min(g[qx][qy+my],min_val)

    val[qx][qy] = min_val+g[qx][qy]

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
            