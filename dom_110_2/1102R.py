def dfs(i):
    visited[i-1] = 1
    if tree[i]:
        for j in tree[i]:
            if visited[j-1]==0:
                dfs(j)

n,m = list(map(int,input().split()))
tree = { i:[] for i in range(1,n+1) }
for i in range(m):
    a,b = list(map(int,input().split()))
    tree[a].append(b)

start,end = list(map(int,input().split()))
visited = [0]*n
dfs(start)

if visited[end-1]:
    print("Yes")
else:
    print("No")

"""
5 8
1 2
1 4
2 1
2 3
2 4
3 5
4 2
5 4
1 3
"""