# ! itertools

import itertools

while 1:
    try:
        in1 = list(map(int,input().split()))
        n = in1[0]
        c = in1[2:]
        v = 0
        for i in range(1,len(c)+1):
            k = [sum(ii) for ii in list(itertools.combinations(c,i))]
            for j in k:
                if j <= n:
                    v = max(v,j)
        print(v)
    except:
        break

    