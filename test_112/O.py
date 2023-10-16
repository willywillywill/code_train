while 1:
    try:
        s,d = list(map(int,input().split()))
        lst = [0]*d
        k = 1
        for i in range(d):
            lst[i] = s
            if k==s:
                s+=1
                k=1
            else:
                k+=1
        print(lst[-1])
    except:
        break