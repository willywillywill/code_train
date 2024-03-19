a,b,c = map(int,input().split())

if b**2-4*a*c == 0:
    print(f"Two same roots x={int(-b/(2*a))}")
elif b**2-4*a*c > 0:
    x1 = (-b+(b**2-4*a*c)**0.5) / (2*a)
    x2 = (-b-(b**2-4*a*c)**0.5) / (2*a)
    print(f"Two different roots x1={int(x1)} , x2={int(x2)}")
else:
    print("No real root")