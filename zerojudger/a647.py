for _ in range(int(input())):
    m,p = list(map(int,input().split()))
    k = (p-m)/m*100
    if k < 0:
        k -= 0.000001
    else:
        k += 0.000001
    if k >= 10 or k <= -7:
        print("%.2f%% dispose"%(k))
    else:
        print("%.2f%% keep"%(k))
