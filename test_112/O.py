while 1:
    try:
        s,d = list(map(int,input().split()))
        while d>0:
            d-=s
            if d<=0:
                break
            s+=1
        print(s)
    except:
        break

"""
1 6
3 10
3 14
"""