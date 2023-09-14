lst = [
    [0,1,1,0,0,0],
    [0,0,1,0,0,0],
    [0,0,1,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,1],
    [0,0,0,0,0,0],
]
val = [ 0 for i in range(6) ]

def dfs(i):
    if val[i]:
        return
    val[i] = 1 

    for j in range(6):
        if lst[i][j]:
            dfs(j)                                                             

for i in range(6):
    dfs(i)
