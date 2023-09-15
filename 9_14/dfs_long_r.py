lst = [
    [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
]

val_1 = [ 0 for i in range(len(lst)) ]
val_2 = [ 0 for i in range(len(lst)) ]


def dfs_1(x,px):
    for i in range(len(lst)):
        if lst[x][i] and px != i: # 單向
            val_1[i] = val_1[x]+1
            dfs_1(i,x)

def dfs_2(x,px):
    for i in range(len(lst)):
        if (x==2**i or y==2**x+1) and px != i: # 單向
            val_2[i] = val_2[x]+1
            dfs_2(i,x)

dfs_1(0,0)
dfs_2(0,0)
print(val_1)
print(val_2)