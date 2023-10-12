# me
for _ in range(1):
    n = int(input())
    m = int(input())
    mxy = [(0,-1),(-1,0),(1,0),(0,1)]
    lst = []
    visited = [[ 0 for i in range(m) ] for j in range(n)]
    val = [[ 0 for i in range(m) ] for j in range(n)]
    for i in range(n):
        lst.append(list(map(int,input().split())))
    queue = [(0,0)]
    while queue:
        x,y = queue.pop(0)
        lst2 = []
        for mx,my in mxy:
            if 0 <= mx+x < n and 0 <= my+y < n:
                pass
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