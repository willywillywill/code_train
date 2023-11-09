while 1:
    try:
        n,m = list(map(int,input().split()))
        a = 0
        b = 0
        while 1:
            a += 1
            b += n
            n += 1
            if b > m:
                break
        print(a)
    except:
        break