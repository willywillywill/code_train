while 1:
    try:
        n = input()
        lst = list(map(int,input().split()))
        print(*sorted(lst))
    except:
        break