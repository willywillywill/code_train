inf = 1e9

n,m = list(map(int,input().split()))
lst = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            lst[i][j] = 0
        else:
            lst[i][j] = inf
for i in range(m):
    a,b,val = list(map(int,input().split()))
    lst[a-1][b-1] = val

for k in range(n):
    for i in range(n):
        for j in range(n):
            if lst[i][j] > lst[i][k]+lst[k][j]:
                lst[i][j] = lst[i][k]+lst[k][j]

for i in lst:
    print(*i)


"""
test data:
4 8
1 2 2
1 3 6
1 4 4
2 3 3
3 1 7
3 4 1
4 1 5
4 3 12
"""