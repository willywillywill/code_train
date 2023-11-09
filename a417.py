for _ in range(int(input())):
    n,s = list(map(int,input().split()))
    num = n*n
    turn = 1
    x,y = 0,0
    x1,y1 = 0,0
    x2,y2 = n-1,n-1
    output = [ [0]*n for i in range(n) ]

    for i in range(1,num+1):
        if s==1:    output[y][x] = i
        else:       output[x][y] = i
        
        if i == num:    break

        if turn == 1: x += 1
        if turn == 2: y += 1
        if turn == 3: x -= 1
        if turn == 4: y -= 1

        if x==x2 and y==y1 and turn==1:
            turn = 2
            y1 += 1
        if x==x2 and y==y2 and turn==2:
            turn = 3
            x2 -= 1
        if x==x1 and y==y2 and turn==3:
            turn = 4
            y2 -= 1
        if x==x1 and y==y1 and turn==4:
            turn = 1
            x1 += 1
    for i in output:
        for j in i:
            print("%5d"%(j),end="")
        print()
