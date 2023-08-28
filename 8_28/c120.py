

while 1:
    try:
        n = int(input())
        val = 1
        for i in range(1,n+1):
            val = val*i
        print("%d!"%(n))
        print(val)
    except:
        break
