


def f(inl,l):
    if inl:
        a = inl.pop(0)
        l.append(a)
        for i in txt:
            k = l.copy()
            k.append(i)
            f(inl.copy(),k.copy())
    else:
        l.pop()
        if eval("".join(l)) == ans:
            c.add("".join(l))

for _ in range(int(input())):  
    txt = list("*+")
    in1,ans = input().split()
    if in1[0]=="-":
        in1 = [in1[0:2]]+list(in1[2:])
    else:
        in1 = list(in1)
    ans = int(ans)
    c = set()
    f(in1.copy(),[])
    if c:
        c = list(c)
        c.sort(key=lambda x:x[1::2])
        for i in c:
            print(i)
    else:
        print(-1)

"""
3
123 6
232 8
3456237490 9191

1*2*3
1+2+3
2*3+2
2+3*2
"""