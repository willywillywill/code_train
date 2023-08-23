"""
3 5
.#...
.#.#.
...#.
"""

n, m = list(map(int, input().split()))
lst = []
xy = [(1,0),(0,1),(-1,0),(0,-1)]

for i in range(n):
    s = list(input())
    lst.append( [ -1 if i=="." else 0 for i in s ] )

qu = [(0, 0, 0)]

while qu:
    i,j, step = qu.pop(0)
    lst[i][j] = step
    for x,y in xy:
        nx = x+i
        ny = y+j
        if 0 <= nx < n and 0 <= ny < m:
            if lst[nx][ny] == -1:
                qu.append([nx,ny, step+1])
print(lst[-1][-1])

