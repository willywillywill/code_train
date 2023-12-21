for _ in range(int(input())):
    s,d = map(int,input().split())
    if (s+d)%2 or (s+d)//2<0 or (s-d)%2 or (s-d)//2<0:
        print("impossible")
    else:
        print((s+d)//2, (s-d)//2)