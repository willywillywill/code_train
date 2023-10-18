# https://www.youtube.com/watch?v=XqoVyBKEhac
while 1:
    try:
        p,d = list(map(int,input().split()))
        st = int((d*2)**0.5)
        for i in range(st,st+st):
            if (i-p+1)*(i+p) >= 2*d:
                print(i)
                break
    except:
        break


"""
1 6
3 10
3 14
"""