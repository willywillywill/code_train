k = 1
while 1:
    try:
        str1 = list(map(int,input().split()))
        n = str1.pop(0)  #多少人參加樂透
        x = str1.pop(0)  #多少人可以休假

        n = [ i+1 for i in range(n) ]

        while len(n)>x:
            val = str1.pop(0)
            n = [ n[i-1] for i in range(len(n)+1) if i%val!=0 and i!=0 ]
            print(n)

        print("Selection #%d"%(k))
        print(*n)
        k+=1
    except:
        break






    
    
    