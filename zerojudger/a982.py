g=[]
for _ in range(int(input())):
    s=list(input())
    arr=[]
    for i in s:
        if i==".":
            arr.append(0)
        else:
            arr.append(i)
    g.append(arr)

dir_xy=((0, 1), (1, 0), (0, -1), (-1, 0))
g[1][1]=1
queue=[(1, 1)]
while len(queue)>0:
    r, c=queue.pop(0)
    for x, y in dir_xy:
        newr=r+x
        newc=c+y
        if g[newr][newc]==0:
            queue.append((newr, newc))
            g[newr][newc]=g[r][c]+1

print(g[-2][-2] if g[-2][-2]!=0 else "No solution!")