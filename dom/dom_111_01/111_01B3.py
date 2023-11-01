
while 1:
    try:
        lst = list(map(float,input().split()))
        xy = [lst[:2],lst[2:4],lst[4:6],lst[6:8]]
        for i in range(4):
            txy = xy[0:i]+xy[i+1:]
            if xy[i] in txy:
                cxy = xy[i]
                idx = txy.index(cxy)
                mxy = txy[0:idx]+txy[idx+1:]
                break
        xy1 = mxy[0]
        xy2 = mxy[1]

        x = xy2[0]+xy1[0]-cxy[0]
        y = xy2[1]+xy1[1]-cxy[1]
        print("%.3f %.3f"%(x,y))
    except:
        break
