MN = 105
INF = 1e9
t = 1
while 1:
    c,s,q = list(map(int,input().split()))
    if c==s==q:
        break

    path = [ [0]*MN for i in range(MN) ]
    for i in range(1,c+1):
        for j in range(1,c+1):
            path[i][j] = INF
    for i in range(s):
        a1,a2,val = list(map(int,input().split()))
        path[a1][a2] = val
        path[a2][a1] = val

    for k in range(1,c+1):
        for i in range(1,c+1):
            for j in range(1,c+1):
                path[i][j] = min(path[i][j], max(path[i][k],path[j][k]))

    print("Case #%d"%(t))
    t+=1
    for i in range(q):
        c1,c2 = list(map(int,input().split()))
        if path[c1][c2]==INF:
            print("no path")
        else:
            print(path[c1][c2])
    print()


"""
7 9 3
1 2 50
1 3 60
2 4 120
2 5 90
3 6 50
4 6 80
4 7 70
5 7 40
6 7 140
1 7
2 6
6 2
7 6 3
1 2 50
1 3 60
2 4 120
3 6 50
4 6 80
5 7 40
7 5
1 7
2 4
0 0 0
"""