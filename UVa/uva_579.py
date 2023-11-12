while 1:
    h,m = map(int,input().split(":"))
    if h==m==0:
        break
    t1 = h*30+m/12*6
    t2 = m*6
    if abs(t1-t2) > 180:
        print("{:.3f}".format(360-abs(t1-t2)))
    else:
        print("{:.3f}".format(abs(t1-t2)))
