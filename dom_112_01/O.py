
while 1:
    try:
        p,d = list(map(int,input().split()))
        if p>d:
            print(p)
            continue
        st = int((d*2)**0.5)
        for i in range(st,d+1):
            if (i-p+1)*(i+p) >= 2*d:
                print(i)
                break
    except:
        break