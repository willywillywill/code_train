lst = list(map(int,input().split()))
lst.sort()

if lst[-1] <= lst[0]+lst[1]:
    n = (lst[0]**2+lst[1]**2)**0.5
    if n == lst[-1]:
        print("Right triangle")
    elif n < lst[-1]:
        print("Obtuse triangle")
    else:
        print("Acute triangle")
else:
    print("It can't be a triangle.")