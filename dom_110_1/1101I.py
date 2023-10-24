while 1:
    try:
        a,b,c,d = list(map(int,input().split()))
        m1 = []
        m2 = []
        m3 = [[ 0 for i in range(d) ] for j in range(a)]
        for i in range(a):
            m1.append(list(map(int,input().split())))
        for i in range(c):
            m2.append(list(map(int,input().split())))
        for i in range(a):
            for j in range(d):
                a1 = m1[i][::]
                a2 = [ ii[j] for ii in m2]

                s = [ a1[ii]*a2[ii] for ii in range(len(a1)) ]
                m3[i][j] = sum(s)
        for i in m3:
            print(*i)
    except:
        break
"""
2 2 2 1
1 2
3 4
5
65535
3 2 2 3
1 2
3 4
5 8
1 2 3
4 5 8
"""