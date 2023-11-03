"""
MAX_NUM = 81

def dfs(x, px): #判斷是否為樹函式
    visited.append(x)
    for i in range(MAX_NUM):
        if path[x][i]==1 and i!=px and i not in visited:
            dfs(i, x)

for _ in range(int(input())):
    s=input().split()
    path=[[0 for _ in range(MAX_NUM)] for _ in range(MAX_NUM)]
    node=[0]*MAX_NUM #紀錄出現過的節點
    edge=0 #紀錄邊的數量
    root=None
    for i in s:
        a, b=map(int, i.split(","))
        if root==None:
            root=a
    
        path[a][b]=1; path[b][a]=1
        node[a]=1; node[b]=1
        edge+=1
    
    node_num=node.count(1) #設為1的即為出現過的節點
    is_tree=True #是否為樹
    visited=[]
    dfs(root, root)
    
    #這邊用來判斷符不符合樹的條件
    if node_num-1!=edge or len(visited)!=node_num:
        is_tree=False
    
    #如果是樹就直接輸出T
    if is_tree:
        print("T")
    else:
        print("F")
"""

def dfs(x,px):
    vis.append(x)  # <- list save visited nodes
    for i in tree[x]:
        if i != px and i not in vis:
            dfs(i,x)

for _ in range(int(input())):
    edge = input().split()
    tree = {}
    root = None
    for i in edge:
        a,b = i.split(",")
        if root == None:
            root = a
        if a not in tree:
            tree[a] = []
        if b not in tree:
            tree[b] = []
        tree[a].append(b)
        tree[b].append(a)

    vis = []
    dfs(root,root)

    if len(vis) == len(tree) and len(tree)-1 == len(edge):
        print("T")
    else:
        print("F")

"""
6,8  5,3  5,2  6,4  5,6  1,2  2,0
"""