while 1:
    try:
        lst = list(map(int,input().split()))[1:]
        if sum(lst)/len(lst) >59:
            print("no")
        else:
            print("yes")
    except:
        break