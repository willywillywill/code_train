
a1,b1,c1,a2,b2,c2 = list(map(int, input().split(",")))

if a1/a2 != b1/b2:
    X =  (b2*c1 - b1*c2)/(a1*b2 - a2*b1)
    Y =  (a1*c2 - a2*c1)/(a1*b2 - a2*b1)
    print(X,Y)

elif a1/a2 == b1/b2 != c1/c2:
    print("N")
elif a1/a2 == b1/b2 == c1/c2:
    X = (-a1*c1) / (-a1**2-b1**2)
    Y = (-(b1*c1)) / (-a1**2-b1**2)
    print(X, Y)