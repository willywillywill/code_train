
n = int(input())
tree = []
for _ in range(n):
    s = list(map(int,input().split()))[1:]
    tree.append(s)


def dfs(r, n=[]):
    n.append(r)
    x=0
    for i in tree[r]:
        if i != -1:
            x+=1
            dfs(i, n.copy())
    if x==0:
        ans.append(n)

for i in range(n):
    ans = []
    print(i)
    dfs(i)
    print(ans)
