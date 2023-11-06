from datetime import datetime

d1 = list(map(int,input().split("/")))
d2 = list(map(int,input().split("/")))
try:
    t1 = datetime(d1[0],d1[1],d1[2])
    t2 = datetime(d2[0],d2[1],d2[2])
    print((t2-t1).days+1)
except:
    print(-1)

"""
2022/2/29 
2022/3/1
"""