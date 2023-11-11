
txt = list("+*")
in1,ans = input().split()
ans = int(ans)

def f(l):
    if len(l) == len(in1)+len(in1)-1:
        p = "".join(l).replace("/","//")
        if ans == eval(p):
            c.append(p)
        return
    
    if len(l)%2!=0:
        for i in txt:
            k = l.copy()
            k.append(i)
            f(k.copy())
    else:
        for i in in1:
            k = l.copy()
            k.append(i)
            f(k.copy())
c = []
f([])
print(c)