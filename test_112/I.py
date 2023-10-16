
while 1:
    h1,m1,h2,m2 = list(map(int,input().split()))
    if h1==h2==m1==m2==0:
        break
    if h1 > h2:
        m = (23-h1)*60+(60-m1)+h2*60+m2
        print(m)
    else:
        t1 = h1*60+m1
        t2 = h2*60+m2
        print(t2-t1)

"""
1 5 3 5
23 59 0 34
21 33 21 10
23 59 23 59
0 0 0 1
0 0 0 0
"""