""" save list
date = [0]*365
n = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
o = 0
for i in range(len(date)):
    date[i] = n[o]
    o+=1
    if o==7:
        o=0
for _ in range(int(input())):
    m,d = list(map(int,input().split()))
    for i in range(1,m):
        if i==2:
            d+=28
        elif i in [1,3,5,7,8,10,12]:
            d+=31
        else:
            d+=30
    print(date[d-1])
"""
""" save int
for _ in range(int(input())):
    m,d = list(map(int,input().split()))
    for i in range(1,m):
        if i==2:
            d+=28
        elif i in [1,3,5,7,8,10,12]:
            d+=31
        else:
            d+=30
    n = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    o = 0
    for i in range(d):
        o+=1
        if o==7:
            o=0
    print(n[o-1])
"""

"""
9
1 6
2 28
4 5
5 26
8 1
11 1
12 25
12 31
3 9
"""