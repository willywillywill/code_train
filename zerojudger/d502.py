while 1:
    try:
        a,b,c,d = map(int,input().split())
        s = d

        k = c
        if a > k*37:
            a -= k*37
        else:
            a = 0
        s += k

        k = b//8
        b -= k*8
        if b:
            if b*56 < a:
                a -= b*56
            else:
                a = 0
        s += k+ (1 if b else 0)

        k = a//64
        a -= k*64
        s += k+ (1 if a else 0)

        print(s)
    except:
        break