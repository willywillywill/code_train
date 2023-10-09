for _ in range(int(input())):
    n = int(input())
    f = [0] * n
    for i in range(n):
        v,u = list(map(int,input().split()))
        f[v-1] = u-1
    out = []
    for i in range(1,n+1):
        visited = [0]*n
        k = i-1
        cnt = 0
        while not visited[k]:
            visited[k] = 1
            k = f[k]
            cnt+=1
        out.append([i,cnt])
    out.sort(key=lambda x:(x[1],-x[0]),reverse=True)
    print(out[0][0])
"""
5
6
1 2
2 3
3 4
4 5
5 1
6 3
6
2 3
3 4
4 5
5 6
6 2
1 4
7
1 2
2 3
3 4
4 5
5 1
6 3
7 6
7
2 3
3 4
4 5
5 6
6 2
7 4
1 7
7
5 4
3 4
4 6
6 7
7 1
1 2
2 1
"""