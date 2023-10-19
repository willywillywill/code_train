
while 1:
    lst = list(map(int,input().split()))
    if sum(lst)==0:
        break
    m1 = lst[0]*60+lst[1]
    m2 = lst[2]*60+lst[3]
    if m1 > m2:
        print(60*24-m1+m2)
    else:
        print(m2-m1)