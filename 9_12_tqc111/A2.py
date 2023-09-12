lst = sorted(list(map(int, input().split())))

if lst[0]+lst[1] >= lst[2]:
    if (lst[0]**2+lst[1]**2)**0.5 == lst[2]:
        print("Right triangle")
    elif (lst[0]**2+lst[1]**2)**0.5 < lst[2]:
        print("Obtuse triangle")
    elif (lst[0]**2+lst[1]**2)**0.5 > lst[2]:
        print("Acute triangle")
else:
    print("It can't be a triangle.")