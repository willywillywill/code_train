
while 1:
    try:
        p,d = list(map(int,input().split()))
        n=0
        for i in range(1,int(d**0.5)+1):
            if d%i==0:
                n = i
        m = d//n
        print(n,m)
        for i in range(n,m+1):
            print(i,d,(p+i)*(i-p+1)//2, d-((p+i)*(i-p+1)//2)<=0)
            #if d-((p+i)*(i-p+1)//2)<=0:
            #    print(i)
            #    break

    except:
        break


"""
1 6
3 10
3 14
"""