"""
def dfs(x):
    for i in range(n):
        if lst[x][i]:
            d[i] = d[x]+1
            dfs(i)

for _ in range(int(input())):
    n = int(input())
    lst = [[ 0 for j in range(n) ] for i in range(n)]
    for i in range(n-1):
        m = list(map(int, input().split(',')))
        lst[m[1]][m[0]] = 1
    d = [ 1 for i in range(n) ]
    dfs(0)
    print(max(d))
"""
dit = {}
n = int(input())


"""
3
4
1,2
2,3
3,0
4
1,0
2,0
3,0
2
1,0
"""