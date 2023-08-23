
def bfs(n=0):
    
    l = 2*n
    r = 2*n+1
    print(tree[l])
    print(tree[r])
    bfs(l)
    bfs(r)




tree = []
for _ in range(int(input())):
    n1,n2,n3 = list(map(int,input().split()))
    tree.append(n2)
    tree.append(n3)
print(tree)

"""
for i in range(len(tree)):
    if tree[i] == [-1,-1]:
        c = 0
    elif tree[i][0] == -1 or tree[i][1] == -1:
        c = 1
    else:
        c = 2
"""  
"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""