# I do not know
g = 1
while 1:
    try:       
        str1 = list(map(int,input().split()))
        n = str1.pop(0)  #多少人參加樂透
        x = str1.pop(0)  #多少人可以休假

        n = list((range(1, n+1)))  #建立一個從 1~n+1 的矩陣用來記錄參加樂透的人

        while len(n) > x and len(str1) > 0:      #刪到參加人數 < 休假人數
            val = str1.pop(0)  #要被刪除的 index
            k = n[val-1::val]  #紀錄被刪除的數

            for i in k:
                n.remove(i)
                if len(n) == x:
                    break
        print("Selection #%d"%(g))
        g+=1
        print(*n)
        print()
    except:
        break
