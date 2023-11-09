def isTree():
    def dfs(x,px):
        if vis[x] > 1:
            return
        vis[x] += 1
        for i in range(len(tree)):
            if tree[x][i] and i != px:
                dfs(i,x)
    vis = [0]*MAX_N
    n = list(nodes)
    dfs(n[0],n[0])
    return vis[1:max(nodes)+1]

def f_s(x):
    a,b = list(map(int,x.split("-")))
    tree[a][b] = 1
    tree[b][a] = 1
    nodes.add(a)
    nodes.add(b)
for _ in range(int(input())):
    if _:
        input()
    trees = []
    MAX_N = 61
    flag = 0
    nodes = set()
    v_lst = []
    for i in range(int(input())):
        tree = [ [0]*MAX_N for i in range(MAX_N) ]
        list(map(f_s, input().split()))
        v = isTree()
        if v.count(2) or 0 in v:
            flag = 1

        v_lst.append(v)
        trees.append(tree)

    if not flag:
        for i in range(MAX_N):
            for j in range(MAX_N):
                a = []
                for k in range(len(trees)):
                    a.append(trees[k][i][j])
                if a.count(1) > 1:
                    flag = 1
                    break
            if flag:
                break
        if not flag:
            j_lst = [0]*MAX_N
            for i in range(len(trees)):
                for j in range(MAX_N):
                    if trees[i][j].count(1) > 1:
                        if j_lst[j]:
                            flag = 1
                            break
                        else:
                            j_lst[j] = 1
                if flag:
                    break

    print( "F" if flag else "T")


"""
2
1-5 2-3 2-4 4-5 4-6
2-5 1-3 2-6 4-1 5-6

2
1-5 2-3 2-4 4-5 4-6
1-3 1-4 1-6 2-6 3-5

1
1-2 2-3 3-1
"""