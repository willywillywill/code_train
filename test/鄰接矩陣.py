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
"""
n = int(input())

tree = [ [0]*9 for i in range(n) ]

for i in range(n):
    a = list(map(int, input().split()))
    if a[1] != -1:
        tree[a[0]][a[1]] = 1
    if a[2] != -1:
        tree[a[0]][a[2]] = 1

def dfs(x, l):
    l.append(x)
    r=0
    for i in range(n):
        if tree[x][i]==1:
            r+=1
            dfs(i, l.copy())
    if r==0:
        ans.append(l)

for i in range(n):
    ans = []
    dfs(i, [])
    
    print(ans)


