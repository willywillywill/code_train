

g = []
for i in range(int(input())):
    l = list(map(str,input().split()))
    for i in range(len(l)):
        if l[i] == ".":
            l[i] = 0
    g.append(l)

def dfs(x,y,n):
    if y==4:
        y=0
        x+=1
    if x==4:
        print(g)
        return
    if y+1 < len(g):
        if not g[x][y] and g[x][y+1]=="X":
            g[x][y] = "P"
            dfs(x,y+1,n+1)
            g[x][y] = 0
            
    dfs(x,y+1,n)

dfs(0,0,0)
"""
4
. X . .
. . . .
X X . .
. . . .
"""