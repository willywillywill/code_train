# top bottom left right
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


lst = []
move = [(-1,0),(1,0),(0,-1),(0,1)] # T B L R
n,m = list(map(int,input().split()))
for _ in range(n):
    lst.append(list(input()))
vis_lst = [ [0]*m for _ in range(n) ]

def dfs(i,j):
    global max_num
    if vis[i][j] or lst[i][j]=="0":
        return
    vis[i][j] = 1
    vis_lst[i][j] = 1
    max_num += 1
    for k in range(4):
        if tube[lst[i][j]][k] == 1:
            dx,dy = move[k]
            if 0<=dx+i<n and 0<=dy+j<m:
                if tube[lst[dx+i][dy+j]][next_tube[k]]:
                    dfs(i+dx,j+dy)
ans = 0
for i in range(n):
    for j in range(m):
        if vis_lst[i][j] == 0:
            max_num = 0
            vis = [ [0]*m for _ in range(n) ]
            dfs(i,j)
            ans = max(ans,max_num)
print(ans)

"""
4 7
0F70000
FXJ0000
II700X7
LJ0HHLJ
"""