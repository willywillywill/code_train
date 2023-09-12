for _ in range(int(input())):
    s = input()
    l = []
    for i in s:
        if "A"<=i<="Z":
            l.append(i)
        else:
            l[-1]+=i
    for i in l:
        print(i[0]*int(i[1::]), end="")
    print()
