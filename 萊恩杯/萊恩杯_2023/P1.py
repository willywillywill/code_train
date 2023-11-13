a,b,c = list(map(int,input().split()))

if a==0:
    print("NO")
else:
    l = b**2-4*a*c
    k1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    k2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    
    if l < 0:
        print("X")
    elif l==0:
        print("0.0000")
    else:
        print("{:.4f} {:.4f}".format(k2,k1))
