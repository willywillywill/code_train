""" !!!
這題跟zerojudge b517是否為樹類似
我的想法是先判斷這張圖是不是樹，不是樹的話，再去看他有沒有形成迴圈
要符合樹的條件有以下兩點：
1. 節點(node)-1 == 邊(edge) 的數量
2. DFS拜訪完的節點數量 == 輸入時出現過的節點數量
"""

def dfs(x, px): #判斷是否為樹函式
    visited.append(x)
    for i in range(20):
        if path[x][i]==1 and i!=px and i not in visited:
            dfs(i, x)

def Cycle(x, px): #尋找形成迴圈的所有節點
    global start
    visited_cyc.append(x)
    for i in range(20):
        if path[x][i]==1 and i==start and i!=px and i in visited_cyc:
            visited_cyc.append(i)
        if path[x][i]==1 and i!=px and i not in visited_cyc:
            Cycle(i, x)
            
for _ in range(int(input())):
    s=input().split()
    path=[[0 for _ in range(20)] for _ in range(20)]
    node=[0]*20 #紀錄出現過的節點
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
        cycle=[]
        """
        如果visited==node_num，代表符合第二點條件，
        那就不可能是森林，所以必定有形成迴圈的情況。
        """
        if len(visited)==node_num:
            for i in range(20):
                if node[i]==1:
                    start=i #紀錄第一個走訪的節點
                    visited_cyc=[]
                    Cycle(i, i)
                    #如果重複走到第一個節點，代表此節點是迴圈節點之一
                    if visited_cyc.count(i)>1:
                        cycle.append(i)
            print(*cycle, sep=", ")
        
        #否則就是森林，直接輸出F
        else:
            print("F")