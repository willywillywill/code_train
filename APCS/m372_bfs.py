
#dstr = ["HFLX","F7IX","H7JX","LIJX"]
def bfs(r,c,mat,m,n):
    que = [(r,c,mat[r][c])]; head = 0
    mat[r][c] = '0'
    while head < len(que):
        r,c,me = que[head]; head += 1
        if c<n-1 and me in "HFLX" and mat[r][c+1] in "H7JX":
            que.append((r,c+1,mat[r][c+1]))
            mat[r][c+1] = '0'
        if c>0 and me in "H7JX" and mat[r][c-1] in "HFLX":
            que.append((r,c-1,mat[r][c-1]))
            mat[r][c-1] = '0'
        if r<m-1 and me in "F7IX" and mat[r+1][c] in "LIJX":
            que.append((r+1,c,mat[r+1][c]))
            mat[r+1][c] = '0'
        if r>0 and me in "LIJX" and mat[r-1][c] in "F7IX":
            que.append((r-1,c,mat[r-1][c]))
            mat[r-1][c] = '0'
            
    return len(que)

m,n = [int(t) for t in input().split()]
mat = []
for i in range(m):
    mat.append(list(input()))
#print(mat)
imax = 0
for i in range(m):
    for j in range(n):
        if mat[i][j]=='0': continue
        imax = max(imax,bfs(i,j,mat,m,n))
#
print(imax)

"""
3 4
FHH7
IIII
LHHJ

tube = {
    "X":[1,1,1,1],
    "I":[1,1,0,0],
    "H":[0,0,1,1],
    "L":[1,0,0,1],
    "7":[0,1,1,0],
    "F":[0,1,0,1],
    "J":[1,0,1,0],
    "0":[0,0,0,0]
}
next_tube = [1,0,3,2]
move = [(-1,0),(1,0),(0,-1),(0,1)] # T B L R


def bfs(init_x,init_y):
    queue = [(init_x,init_y)]
    vis = [ [0]*m for _ in range(n) ]
    max_num = 0
    while queue:
        x,y = queue.pop(0)
        if vis[x][y] or lst[x][y]=="0":
            continue
        vis[x][y] = 1
        for i in range(4):
            dx,dy = move[i]
            if x+dx<0 or y+dy<0 or\
                x+dx>=n or y+dy>=m:
                continue
            if tube[lst[x][y]][i] and \
                tube[lst[dx+x][dy+y]][next_tube[i]]:
                max_num += 1
                
                queue.append((dx+x,dy+y))
    for i in vis:
        print(*i)
    return max_num
lst = []
n,m = list(map(int,input().split()))
for _ in range(n):
    lst.append(list(input()))

for i in range(n):
    for j in range(m):
        print(bfs(i,j))
"""