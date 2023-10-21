def dfs(i,j,l): # i:node ,j:tree
    if tree[i][j] != 999:
        l.append(tree[i][j])
        dfs(tree[i][j],j,l.copy())
    else:
        ans.append(str(len(l.copy())))

for _ in range(int(input())):
    lst = list(map(int,input().split(",")))
    tree = [[0 for i in range(lst[1])]for j in range(lst[0])]
    for i in range(lst[0]):
        l = list(map(int,input().split()))
        tree[i] = l[1:]
    ans = []
    for i in range(lst[1]):
        dfs(lst[2],i,[])
    print(",".join(ans))



"""
2
7,4,6
0 999 999 999 999
1 0 2 6 3
2 1 0 4 3
3 1 2 4 5
4 3 2 6 5
5 3 4 6 0
6 1 4 0 5
7,4,2
0 999 999 999 999
1 0 2 6 3
2 1 0 3 4
3 1 2 4 5
4 3 2 6 5
5 3 4 6 0
6 1 4 0 5

"""