node_number,edge_number = list(map(int,input().split()))
nodes = {i: [] for i in range(node_number)}
for i in range(edge_number):
    l = list(map(int,input().split()))
    nodes[l[0]].append(l[1])
    nodes[l[1]].append(l[0])

def dfs(i,d):
    global ans
    ans = max(ans,d)
    for j in nodes[i]:
        if not visited[j]:
            visited[j] = 1
            dfs(j,d+1)
            visited[j] = 0
ans = 0
for i in nodes:
    visited = [0]*node_number
    visited[i] = 1
    dfs(i,0)
print(ans)
"""
3 2
0 1
1 2

?
15 16
0 2
1 2
2 3
3 4
3 5
4 6
5 7
6 8
7 8
7 9
8 10
9 11
10 12
11 12
10 13
12 14
"""