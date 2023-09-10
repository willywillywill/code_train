


for _ in range(int(input())):
    x1,y1,x2,y2 = list(map(int,input().split()))

    c1 = x1+y1
    c2 = x2+y2

    n = len(range(c1,c2+1))
    n = int( c1*n + (n*(n-1))/2 )

    out = n+x2

    print("Case %d:"%(_),out)