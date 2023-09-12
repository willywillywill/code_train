import math
while 1:
    try:
        lst = list(map(eval, input().split()))
        r = []
        c = math.ceil(lst[0]/lst[2])

        for i in range(lst[2]):
            r.append((lst[0]-(c*i))*((lst[1]/100)/12))
        print(int(sum(r)))
    except:
        break

