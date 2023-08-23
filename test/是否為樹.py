def dfs(x):
    visited.append(x)
    for i in tree[x]:
        if i not in visited:
            dfs(i)

for _ in range(int(input())):
    s=input().split()
    edge=0
    tree=[[] for _ in range(81)] #建陣列表示樹
    node=[0]*81 #紀錄共有幾個節點
    root=None
    for i in s:
        a, b=list(map(int, i.split(",")))
        edge+=1
        if root==None:
            root=a #隨便找一個root
        tree[a].append(b) #A可以到達B
        tree[b].append(a) #B可以到達A
        node[a]=1
        node[b]=1

    visited=[]
    dfs(root)
    is_tree=True
    node_num=node.count(1)
    visited_node=len(visited)
    if node_num-1!=edge or node_num!=visited_node: #1. 出現環路 2. A點無法到B點
        is_tree=False
    
    print("T" if is_tree else "F")