def p(x, d):
    for i in range(2,x):
        if x %i==0:
            d[i] = d.get(i,0)+1
            p(x//i, d)
            break
    else:
        d[x] = d.get(x,0)+1

while 1:
    lst = list(map(int,input().split()))
    if lst == [0]:
        break
    s = 1
    for i in range(0,len(lst),2):
        s *= lst[i]**lst[i+1] 
    dit = {}
    p(s-1, dit)
    for i in sorted(list(dit.items()))[::-1]:
        print(i[0],i[1], end=" ")
    print()
