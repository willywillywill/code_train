lst = [0,5,7,2,4,8,4]

k = 1
while k:
    k = 0
    for i in range(1,len(lst)):
        if lst[i-1] > lst[i]:
            lst[i-1], lst[i] = lst[i],lst[i-1]
            k = 1
    print(lst)
