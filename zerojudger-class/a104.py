while 1:
    try:
        input()
        l = list(map(int,input().split()))
        l.sort()
        print(*l)
    except:
        break