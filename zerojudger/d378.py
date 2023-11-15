t = 1

while 1:
    try:
        n,m = map(int,input().split())
        lst = []
        for _ in range(n):
            lst.append(list(map(int,input().split())))

        for i in range(1,n):
            lst[i][0] = lst[i-1][0]+lst[i][0]
        for i in range(1,m):
            lst[0][i] = lst[0][i-1]+lst[0][i]

        for i in range(1,n):
            for j in range(1,m):
                lst[i][j] = min(lst[i-1][j],lst[i][j-1])+lst[i][j]
        print("Case #%d :"%(t))
        t+=1
        print(lst[-1][-1])
    except:
        break
