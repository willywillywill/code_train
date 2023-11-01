x1,y1,x2,y2,x3,y3,x4,y4 = list(map(int,input().split()))

if ((y1-y2)/(x1-x2))*((y3-y4)/(x3-x4)) == -1:
    print("垂直")
elif ((y1-y2)/(x1-x2)) == ((y3-y4)/(x3-x4)):
    print("平行")
else:
    print("兩者皆非")