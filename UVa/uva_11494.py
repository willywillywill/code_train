while 1:
    qx,qy,ex,ey = map(int,input().split())
    if qx==qy==ex==ey==0:
        break
    
    if qx==ex and qy==ey:
        print(0)
    elif qx==ex:
        print(1)
    elif qy==ey:
        print(1)
    elif (qy-ey)/(qx-ex)==1 or (qy-ey)/(qx-ex)==-1:
        print(1)
    else:
        print(2)