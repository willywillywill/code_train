
while 1:
    try:
        # 第一個條件用除10的餘數，第二個用整數除法10的商來排序就會是答案了
        # 1    5.(1) 1.(3)
        # 2    (5).1 (1).3
        input()
        s = input().split()
        s.sort(key=lambda x:(int(x)%10,-int(x)//10))
        print(*s)
    except:
        break