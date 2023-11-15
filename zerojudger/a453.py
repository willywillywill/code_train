
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    if b**2 < 4*a*c:
        print("No")
    else:
        s = (b**2-4*a*c)**0.5
        if int(s)==s:
            print("Yes")
        else:
            print("No")
