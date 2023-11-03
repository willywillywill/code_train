while 1:
    try:
        lst = list(map(int,input().split(",")))
        a1 = []
        a2 = []
        for i in range(len(lst)):
            if i%2==0:
                a1.append(lst[i])
            else:
                a2.append(lst[i])
        a1.sort() 
        a2.sort() 
        ans = []
        for i in range(len(lst)):
            if i%2==0:
                ans.append(str(a1.pop(0)))
            else:
                ans.append(str(a2.pop(0)))
        print(",".join(ans))
    except:
        break