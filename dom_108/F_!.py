for _ in range(int(input())):
    a,b = list(map(int,input().split()))

    lst = []
    out = []

    while 1:
        s = a%b
        out.append(str(a//b))
        if s in lst:
            lst.append(s)
            break
        lst.append(s)
        a = s*10
    print(out[0],end=".")

    if lst[-1]==lst[-2]:
        print("".join(out[1:len(lst)-1]),end="")
        print("(",end="")
        print("".join(out[len(lst)-1])+")")
    else:
        if len(out) >= 51:
           print("("+"".join(out[1:51])+"..."+")")
        else:
            print("("+"".join(out[1:])+")")


"""
3
76 25
5 43
1 397

3
1 6
5 7
1 250
"""