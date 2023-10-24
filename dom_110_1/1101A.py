while 1:
    try:
        a,b,c = list(map(int,input().split()))
        print(24*a+14*b+6*c)
    except:
        break