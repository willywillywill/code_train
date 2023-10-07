# ! ! ! !

"""
3
76 25
5 43
1 397
"""
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    lst = []
    out = []
    while 1:
        out.append(str(a//b))
        s = a%b
        a = s*10
        if s == 0:
            print(out[0], end=".")
            print("".join(out[1:])+"(0)")
            break
        elif s in lst:
            idx = lst.index(s)
            print(out[0],end="")

            if idx != 0:
                print("."+"".join(out[1:idx+1]),end="")
                print("("+"".join(out[idx+1:])+")")
            else:
                print(".("+"".join(out[1:])+")")
            break
        elif len(lst)==50:
            print(out[0],end=".")
            print("("+"".join(out[1:])+"...)")
            break
        lst.append(s)