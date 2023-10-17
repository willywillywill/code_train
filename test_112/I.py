

while 1:
    in1 = list(map(int,input().split()))
    if not sum(in1):
        break
    t1,t2 = in1[0]*60+in1[1],in1[2]*60+in1[3]
    print(60*24-t1+t2 if t1>t2 else t2-t1)


"""
1 5 3 5
23 59 0 34
21 33 21 10
23 59 23 59
0 0 0 1
0 0 0 0
"""