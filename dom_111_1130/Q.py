
def dfs_D(x):
    for i in range(n):
        if tree[x][i]:
            d[i] = d[x]+1
            dfs_D(i)
def dfs_H(x):
    h = 0
    for i in range(n):
        if tree[x][i]:
            h = max(h, dfs_H(i)+1)
    return h

n = int(input())
d = [ 0 for i in range(n) ]
tree = [[ 0 for i in range(n) ] for j in range(n)]
for _ in range(n):
    n1,n2,n3 = list(map(int,input().split()))
    if n2 != -1:
        tree[n1][n2] = 1
    if n3 != -1:
        tree[n1][n3] = 1

dfs_D(0)
info     = { "ID":0,"F":0,"K":0,"D":0,"H":0 }
info_set = [ info.copy() for i in range(n) ]
for i in range(n):
    info_set[i]["ID"] = i

    for ii in range(n):
        if tree[ii][i] == 1:
            info_set[i]["F"] = ii
            break
    else:
        info_set[i]["F"] = -1
    info_set[i]["K"] = len([ ii for ii in range(n) if tree[i][ii]==1 ])
    info_set[i]["D"] = d[i]
    info_set[i]["H"] = dfs_H(i)

    print("node %d: parent = %d, degree = %d, depth = %d, height = %d,"
          %(
            info_set[i]["ID"],
            info_set[i]["F"],
            info_set[i]["K"],
            info_set[i]["D"],
            info_set[i]["H"]
            ))



"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1

6
0 3 -1
1 -1 5
2 -1 -1
3 4 -1
4 2 1
5 -1 -1
"""