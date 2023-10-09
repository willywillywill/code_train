""" ???
for i in range(1,n+1): # YES
        visited = [0]*n
        k = i-1
        cnt = 0
        mx = 0
        while not visited[k]:
            visited[k] = 1
            k = f[k]
            cnt+=1
        out.append([i,cnt])

def dfs(i):  # !!!! NO
    if not visited[i-1]:
        visited[i-1]=1
        if i in dit:
            dfs(dit[i])
"""
def dfs(i):  # !!!! NO
    if not visited[i-1]:
        visited[i-1]=1
        if i in dit:
            dfs(dit[i])
for _ in range(int(input())):
    dit = {}
    n = int(input())
    for i in range(n):
        u,v = list(map(int, input().split()))
        dit[u] = v
    out = []
    for i in range(1,n+1):
        visited = [0]*n
        dfs(i)
        v = [i,len([ ii for ii in visited if ii ])]
        out.append(v)
    out.sort(key=lambda x:[x[1],-x[0]], reverse=True)

    print(out[0][0])

"""
3
3
1 2
2 3
3 1
4
1 2
2 1
4 3
3 2
5
1 2
2 1
5 3
3 4
4 5
"""