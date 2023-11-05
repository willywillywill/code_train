for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    lst = []
    out = []
    while 1:
        out.append(str(a//b))
        s = a%b
        a = s*10

        if s==0:
            print("%s.%s(0)"%(out[0],"".join(out[1:])))
            break
        elif s in lst:
            idx = lst.index(s)

            print("%s.%s(%s)"%(out[0],"".join(out[1:idx+1]),"".join(out[idx+1:])))
            break
        elif len(lst) == 50:
            print("%s.(%s...)"%(out[0],"".join(out[1:])))
            break
        lst.append(s)