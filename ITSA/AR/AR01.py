while 1:
    try:
        lst = list(map(int,input().split()))
        print(*lst[::-1])
    except:
        break