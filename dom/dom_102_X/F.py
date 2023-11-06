def is_Tree(d):
    def dfs(root,ptr):
        if vis[root] < 2:
            vis[root] += 1
            for i in d[root]:
                if i != ptr:
                    dfs(i,root)
    vis = { i:0 for i in d }
    dfs(d[1][0],0)
    if 2 in vis.values() or 0 in vis.values():
        return False
    return True 

def f_s(s):
    global flag
    s = list(map(int,s.split("-")))

    if s[0] not in tree:
        tree[s[0]] = []
    if s[1] not in tree:
        tree[s[1]] = []
    nodes.add(s[0])
    nodes.add(s[1])
    tree[s[0]].append(s[1])
    tree[s[1]].append(s[0])

for _ in range(int(input())):
    if _:
        input()
    n = int(input())
    trees = []
    nodes = set()
    flag = False
    for i in range(n):
        tree = {}
        list(map(f_s,input().split(" ")))
        flag = not is_Tree(tree)
        trees.append(tree)

    if flag:
        print("F")
    else:
        for i in nodes:
            l = []
            for j in range(n):
                l.append(trees[j][i])
            len_ = [ len(i) for i in l ]
            if 1 not in len_: # 重內
                flag = True
                break
            s = set([ k  for j in l for k in j ]) # 重邊
            if len(s) != sum(len_):
                flag = True
                break
        print( "F" if flag else "T" )


"""
3
2
1-5 2-3 2-4 4-5 4-6
1-3 1-4 1-6 2-6 3-5

4
1-2 1-3 1-4 1-5 5-6 5-7 5-8
2-3 2-4 2-5 2-6 6-1 6-7 6-8
3-4 3-7 3-5 3-6 7-8 7-1 7-2
4-8 4-5 4-6 4-7 8-1 8-2 8-3

6
1-2 1-3 1-4 1-5 1-6 1-7 7-8 7-9 7-10 7-11 7-12
1-8 2-3 2-4 2-5 2-6 2-7 2-8 8-9 8-10 8-11 8-12
1-9 2-9 3-4 3-5 3-6 3-7 3-8 3-9 9-10 9-11 9-12
1-10 2-10 3-10 4-5 4-6 4-7 4-8 4-9 4-10 10-11 10-12
1-11 2-11 3-11 4-11 5-6 5-7 5-8 5-9 5-10 5-11 11-12
1-12 2-12 3-12 4-12 5-12 6-7 6-8 6-9 6-10 6-11 6-12

"""