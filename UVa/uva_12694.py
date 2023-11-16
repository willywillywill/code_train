
for _ in range(int(input())):
    lst =[]
    while 1:
        s,f = map(int,input().split())
        if s==f==0:
            break
        lst.append([s,f])
    lst.sort(key=lambda x:x[1])

    s,e = -1,0
    t = 1
    while lst:
        s_,e_ = lst.pop(0)
        if s==-1:
            s = s_
            e = e_
            continue
        if e <= s_:
            e = e_
            t+=1
    print(t)

"""
3

0 6
5 7
8 9
5 9
1 2
3 4
0 5
0 0

6 10
5 6
0 3
0 5
3 5
4 5
0 0

1 5
3 9
0 0
"""