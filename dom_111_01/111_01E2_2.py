for _ in range(int(input())):
    n = int(input())
    m = int(input())
    lst = []
    visited = [[ 0 for i in range(m) ] for j in range(n)]
    val = [[ 0 for i in range(m) ] for j in range(n)]
    for i in range(n):
        lst.append(list(map(int,input().split())))
    queue = [(0,0)]
    while queue:
        x,y = queue.pop(0)
        if visited[x][y] == 0:
            visited[x][y]=1
            if x==y==0:
                val[x][y] = lst[x][y]
            elif x-1 < 0:
                val[x][y] = val[x][y-1]+lst[x][y]
            elif y-1 < 0:
                val[x][y] = val[x-1][y]+lst[x][y]
            elif val[x-1][y] >= val[x][y-1]:
                val[x][y] = val[x][y-1]+lst[x][y]
            elif val[x-1][y] <= val[x][y-1]:
                val[x][y] = val[x-1][y]+lst[x][y]

            if x+1 < n:
                queue.append([x+1,y])    
            if y+1 < m:
                queue.append([x,y+1]) 
    print(val[-1][-1])
"""
2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5
"""