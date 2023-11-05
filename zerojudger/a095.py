
while 1:
    try:
        n,m = list(map(int,input().split()))
        if n==m:
            print(n)
        else:
            print(m+1)
    except:
        break