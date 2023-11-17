paths=[]
Articulation=[] #關節點
tree_leval=0
v=[]
up=[]
def dfs(p,t):
    global paths,Articulation,tree_leval,v,up
    tree_leval+=1
    v[t]=tree_leval
    up[t]=tree_leval
    child=0 #P點有幾個兒子
    AP=False
    nexp_point=0
    for i in range(0,len(paths[t])):
        nexp_point=paths[t][i]
        if nexp_point!=p:
            if v[nexp_point]>0:
                up[t]=min(up[t],v[nexp_point])
            else:
                child+=1
                dfs(t,nexp_point)
                up[t]=min(up[t],up[nexp_point])
                if up[nexp_point]>=v[t]:
                    AP=True
    if (t==p and child>1) or (t!=p and AP==True):
        Articulation.append(t)
while 1:
    n=int(input())
    if n==0:
        break
    root=0
    paths=[[] for i in range(n+1)]
    v=[0 for i in range(n+1)]
    up=[0 for i in range(n+1)]
    Articulation=[]
    while 1:
        x=[int(i) for i in input().split()]
        if root==0:
            root=x[0]
        if x[0]==0:
            break
            
        for i in range(1,len(x)):
            if x[i] not in paths[x[0]]:
                paths[x[0]].append(x[i])
            if x[0] not in paths[x[i]]:
                paths[x[i]].append(x[0])
    dfs(root,root)
    print(len(Articulation))
    v=[0 for i in range(0,n+1)]

"""
6
2 1 3
5 4 6 2
0
6
1 2 4 6
2 1 3 5
3 2 4
4 1 3
5 2 6
6 5 1
0
"""