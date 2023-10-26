def f(index):
    if index<=6:
        return index
    p2 = 0
    p3 = 0
    p5 = 0
    ugly = 1
    ret = [ugly]
    
    while len(ret) < index:
        ugly = min([ret[p2]*2,ret[p3]*3,ret[p5]*5])
        ret.append(ugly)
        if ret[p2]*2 == ugly:
            p2 += 1
        if ret[p3]*3 == ugly:
            p3 += 1
        if ret[p5]*5 == ugly:
            p5 += 1
    return ret
ret = f(7000)

_ = int(input())
lst = list(map(int,input().split()))
for i in lst:
    print(i in ret)