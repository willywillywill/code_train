while 1:
    try:
        lst = input()
        n = 1
        m = 0
        for i in range(1,len(lst)):
            if int(lst[i-1])<=int(lst[i]):
                n+= 1
            else:
                n = 1
            m = max(n,m)
        print(m)
    except:
        break
"""
1112223334444555566667777
3337777899922222222222222222
"""