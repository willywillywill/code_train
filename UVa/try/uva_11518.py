def dfs(root):
    if root in dit and vis[root]==0:
        vis[root] = 1
        for i in dit[root]:
            dfs(i)
for _ in range(int(input())):
    vis = {}
    n,m,l = list(map(int,input().split()))
    dit = { i:[] for i in range(1,n+1) }
    vis = { i:0 for i in range(1,n+1) }
    for i in range(m):
        a,b = list(map(int,input().split()))
        dit[a].append(b)

    for i in range(l):
        dfs(int(input()))
    print(list(vis.values()).count(1))




"""
100

18 50 9
1 9
2 3
2 14
2 15
3 7
3 10
3 12
3 18
4 4
4 7
4 10
4 13
4 17
7 6
7 11
8 1
8 3
8 11
9 2
9 4
9 12
9 13
9 16
10 6
10 7
10 18
11 4
11 6
12 4
12 11
12 17
13 7
13 8
13 12
13 15
13 18
14 3
14 6
14 9
14 17
15 3
15 11
16 7
16 17
16 18
18 2
18 3
18 4
18 10
18 18
17
4
11
17
3
17
10
5
12
A:18


6 6 9
1 4
1 5
3 1
3 4
3 6
5 4
3
3
5
1
2
2
2
6
2
A:6
"""