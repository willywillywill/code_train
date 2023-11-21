from collections import deque


for _ in range(int(input())):
    m,n,sx,sy,ex,ey = map(int,input().split())
    sx,sy,ex,ey = sx-1,sy-1,ex-1,ey-1
    lst = []
    for _ in range(m):
        lst.append(list(map(int,list(input()))))
    move = [ (1,0),(0,1),(-1,0),(0,-1) ]

    qu = deque([(sx,sy,1)])
    while qu:
        x,y,w = qu.popleft()
        if lst[x][y]:
            continue
        lst[x][y] = w
        if x==ex and y==ey:
            print(w)
            break
        for dx,dy in move:
            if 0<=x+dx<m and \
            0<=y+dy<n and \
            lst[x+dx][y+dy]==0:
                qu.append((x+dx,y+dy,w+1))
    else:
        print(0)
