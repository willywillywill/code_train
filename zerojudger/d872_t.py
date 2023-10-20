while 1:
    try:
        n = int(input())
        str_lst = list(map(int,input().split()))
        end_lst = []
        str_lst.sort()
        ans = 0
        if n==1:
            print(str_lst[0])
            continue
        while n>=4 and str_lst[0]+str_lst[n-2] > str_lst[1]<<1:
            ans += (str_lst[1] << 1) + str_lst[0] + str_lst[n-1]
            n -= 2
        while n>2:
            ans += str_lst[0]+str_lst[n-1]
            n-=1
        print(ans+str_lst[1])
    except:
        break
