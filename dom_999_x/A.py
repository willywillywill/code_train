
while 1:
    try:
        lst = list(map(int,input().split()))
        lst[0] *= 56
        lst[1] *= 24
        lst[2] *= 14
        lst[3] *= 6
        print(sum(lst))
    except:
        break

