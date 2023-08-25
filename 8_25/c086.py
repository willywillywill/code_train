# I do not know
g = 1
while 1:
    try:       
        str1 = list(map(int,input().split()))
        n = str1.pop(0)  #多少人參加樂透
        x = str1.pop(0)  #多少人可以休假

        n = list((range(1, n+1)))

        while len(n) > x:
            val = str1.pop(0)
            k = n[val-1::val]
            del n[val-1::val]  
            
        if len(n) != x:
            n.append(k[::-1])
            n.sort()
        print("Selection #%d"%(g))
        g+=1
        print(*n)
    except:
        break
